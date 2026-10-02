import os
import glob
import numpy as np
from PIL import Image
import tensorflow as tf
from keras.preprocessing import image
from keras.src import backend
from keras.src import layers
from keras.src.api_export import keras_export
from keras.src.applications import imagenet_utils
from keras.src.models import Functional
from keras.src.ops import operation_utils
from keras.src.utils import file_utils
from keras import backend as K
import shutil
import random

def ResNet(
    stack_fn,
    preact,
    use_bias,
    include_top=True,
    weights=None,
    input_tensor=None,
    input_shape=(32,32,3),
    pooling=None,
    classes=10,
    classifier_activation="softmax",
    name="resnet",
    weights_name=None,
):

    img_input = layers.Input(shape=input_shape)

    if backend.image_data_format() == "channels_last":
        bn_axis = 3
    else:
        bn_axis = 1

    x = layers.ZeroPadding2D(padding=((3, 3), (3, 3)))(
        img_input
    )
    x = layers.Conv2D(64, 7, strides=2, use_bias=use_bias, name="conv1_conv")(x)

    if not preact:
        x = layers.BatchNormalization(
            axis=bn_axis, epsilon=1.001e-5
        )(x)
        x = layers.Activation("relu")(x)

    x = layers.ZeroPadding2D(padding=((1, 1), (1, 1)))(x)
    x = layers.MaxPooling2D(3, strides=2, name="pool1_pool")(x)

    x = stack_fn(x)

    if preact:
        x = layers.BatchNormalization(
            axis=bn_axis, epsilon=1.001e-5
        )(x)
        x = layers.Activation("relu")(x)

    x = layers.GlobalAveragePooling2D(name="avg_pool")(x)

    # Validate activation for the classifier layer
    imagenet_utils.validate_activation(classifier_activation, weights)

    x = layers.Dense(
        classes, activation=classifier_activation, name="predictions"
    )(x)

    # Ensure that the model takes into account
    # any potential predecessors of `input_tensor`.
    if input_tensor is not None:
        inputs = operation_utils.get_source_inputs(input_tensor)
    else:
        inputs = img_input

    # Create model.
    model = Functional(inputs, x, name=name)

    return model

def residual_block_v1(
    x, filters, kernel_size=3, stride=1, conv_shortcut=True, name=None
):

    if backend.image_data_format() == "channels_last":
        bn_axis = 3
    else:
        bn_axis = 1

    if conv_shortcut:
        shortcut = layers.Conv2D(
            4 * filters, 1, strides=stride, name=f"{name}_0_conv"
        )(x)
        shortcut = layers.BatchNormalization(
            axis=bn_axis, epsilon=1.001e-5
        )(shortcut)
    else:
        shortcut = x

    x = layers.Conv2D(filters, 1, strides=stride, name=f"{name}_1_conv")(x)
    x = layers.BatchNormalization(
        axis=bn_axis, epsilon=1.001e-5
    )(x)
    x = layers.Activation("relu")(x)

    x = layers.Conv2D(
        filters, kernel_size, padding="SAME", name=f"{name}_2_conv"
    )(x)
    x = layers.BatchNormalization(
        axis=bn_axis, epsilon=1.001e-5
    )(x)
    x = layers.Activation("relu")(x)

    x = layers.Conv2D(4 * filters, 1, name=f"{name}_3_conv")(x)
    x = layers.BatchNormalization(
        axis=bn_axis, epsilon=1.001e-5
    )(x)

    x = layers.Add()([shortcut, x])
    x = layers.Activation("relu")(x)
    return x

def stack_residual_blocks_v1(x, filters, blocks, stride1=2, name=None):

    x = residual_block_v1(x, filters, stride=stride1, name=f"{name}_block1")
    for i in range(2, blocks + 1):
        x = residual_block_v1(
            x, filters, conv_shortcut=False, name=f"{name}_block{i}"
        )
    return x

def residual_block_v2(
    x, filters, kernel_size=3, stride=1, conv_shortcut=False, name=None
):

    if backend.image_data_format() == "channels_last":
        bn_axis = 3
    else:
        bn_axis = 1

    preact = layers.BatchNormalization(
        axis=bn_axis, epsilon=1.001e-5
    )(x)
    preact = layers.Activation("relu")(preact)

    if conv_shortcut:
        shortcut = layers.Conv2D(
            4 * filters, 1, strides=stride, name=f"{name}_0_conv"
        )(preact)
    else:
        shortcut = (
            layers.MaxPooling2D(1, strides=stride)(x) if stride > 1 else x
        )

    x = layers.Conv2D(
        filters, 1, strides=1, use_bias=False, name=f"{name}_1_conv"
    )(preact)
    x = layers.BatchNormalization(
        axis=bn_axis, epsilon=1.001e-5
    )(x)
    x = layers.Activation("relu")(x)

    x = layers.ZeroPadding2D(padding=((1, 1), (1, 1)))(x)
    x = layers.Conv2D(
        filters,
        kernel_size,
        strides=stride,
        use_bias=False,
        name=f"{name}_2_conv",
    )(x)
    x = layers.BatchNormalization(
        axis=bn_axis, epsilon=1.001e-5
    )(x)
    x = layers.Activation("relu")(x)

    x = layers.Conv2D(4 * filters, 1, name=f"{name}_3_conv")(x)
    x = layers.Add()([shortcut, x])
    return x

def stack_residual_blocks_v2(x, filters, blocks, stride1=2, name=None):

    x = residual_block_v2(x, filters, conv_shortcut=True, name=f"{name}_block1")
    for i in range(2, blocks):
        x = residual_block_v2(x, filters, name=f"{name}_block{i}")
    x = residual_block_v2(
        x, filters, stride=stride1, name=f"{name}_block{str(blocks)}"
    )
    return x

@keras_export(
    [
        "keras.applications.resnet50.ResNet50",
        "keras.applications.resnet.ResNet50",
        "keras.applications.ResNet50",
    ]
)
def ResNet50(
    include_top=True,
    weights=None,
    input_tensor=None,
    input_shape=(32,32,3),
    pooling=None,
    classes=10,
    classifier_activation="softmax",
    name="resnet50",
):
    """Instantiates the ResNet50 architecture."""

    def stack_fn(x):
        x = stack_residual_blocks_v1(x, 64, 3, stride1=1, name="conv2")
        x = stack_residual_blocks_v1(x, 128, 4, name="conv3")
        x = stack_residual_blocks_v1(x, 256, 6, name="conv4")
        return stack_residual_blocks_v1(x, 512, 3, name="conv5")

    return ResNet(
        stack_fn,
        preact=False,
        use_bias=True,
        weights_name=None,
        name=name,
        include_top=include_top,
        weights=weights,
        input_tensor=input_tensor,
        input_shape=input_shape,
        pooling=pooling,
        classes=classes,
        classifier_activation=classifier_activation,
    )

def testAPI(teststr):
    K.clear_session()
    # 固定随机种子
    tf.random.set_seed(1)
    np.random.seed(1)
    random.seed(1)

    #训练数据集
    train = "/mnt/c/data/MNIST/train"
    classes = ['0','1','2','3','4','5','6','7','8','9']
    n_classes = len(classes)

    def preprocess_img(img_path, label):
        def py_load_img(img_path):
            img = image.load_img(img_path.numpy().decode('utf-8'), target_size=(32, 32), color_mode="rgb")
            img = img.point(lambda i: 255 - i)
            arr = np.divide(np.array(img, dtype=np.float32), 255.0)
            return arr
        img = tf.py_function(py_load_img, [img_path], tf.float32)
        img.set_shape([32, 32, 3]) 
        return img, label

    img_paths = []
    labels = []
    for index, class_ in enumerate(classes):
        class_dir = os.path.join(train, class_)
        files = glob.glob(os.path.join(class_dir, '*.png'))
        label = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        label[index] = 1
        for img_path in files:
            img_paths.append(img_path)
            labels.append(label.copy())
    batch_size_train=16
    # 构建 tf.data.Dataset，自动打乱和分批
    dataset = tf.data.Dataset.from_tensor_slices((img_paths, labels))
    dataset = dataset.shuffle(buffer_size=len(img_paths),seed=1)
    dataset = dataset.map(preprocess_img, num_parallel_calls=tf.data.AUTOTUNE)
    dataset = dataset.batch(batch_size_train).prefetch(tf.data.AUTOTUNE)

    # 构建模型并编译
    model = ResNet50(input_shape=(32,32,3),classes=n_classes)
    model.summary()
    epochs=3
    # 训练
    #model.fit(dataset, epochs=epochs)

    # 保存 h5 权重文件
    #base_name = os.path.splitext(os.path.basename(__file__))[0]
    #ck_dir = os.path.join('/mnt/c/RQ1/ResNet50', f'checkpoint{base_name}')
    ck_dir = '/mnt/c/RQ1/ResNet50/checkpointResNet50'
    os.makedirs(ck_dir, exist_ok=True)
    weights_path = os.path.join(ck_dir, 'ResNet50_model.weights.h5')
    #model.save_weights(weights_path)
    model.load_weights(weights_path)

    # 确保 BatchNormalization 层在推理模式下
    for layer in model.layers:
        if isinstance(layer, tf.keras.layers.BatchNormalization):
            layer.trainable =False
    # 收集测试图片路径和标签
    img_paths = []
    labels = []
    for idx, cls in enumerate(classes):
        cls_dir = os.path.join(test_dir, cls)
        if not os.path.isdir(cls_dir):
            continue
        files = glob.glob(os.path.join(cls_dir, '*.png'))
        label = [0]*n_classes
        label[idx] = 1
        for img_path in files:
            img_paths.append(img_path)
            labels.append(label.copy())

    if len(img_paths) == 0:
        raise ValueError(f"No test images found in {test_dir}")

    # 按 batch 处理测试图片
    result = []
    batch_imgs = []

    # 加载所有测试图片
    for img_path in img_paths:
        img_test = image.load_img(img_path, target_size=(32, 32), color_mode="rgb")
        img_test = img_test.point(lambda i: 255 - i)
        image_test = np.divide(np.array(img_test, dtype=np.float32), 255.0)
        batch_imgs.append(image_test)

    # 转换为 NumPy 数组
    batch_imgs = np.array(batch_imgs, dtype=np.float32)

    # 一次性预测所有图片
    result = model(batch_imgs,training=False)

    # 预测
    y_true = np.argmax(labels, axis=1)
    pred_top1 = np.argmax(result, axis=1)

    acc1 = np.mean(pred_top1 == y_true)
    top5_preds = np.argsort(result, axis=1)[:, -5:]
    acc5 = np.mean([y_true[i] in top5_preds[i] for i in range(len(y_true))])


    # 打印预测错误的样本
    for i in range(len(img_paths)):
        if pred_top1[i] != y_true[i]:
            print(f"Sample {i}: True Label = {y_true[i]}, Predicted = {pred_top1[i]}, Probabilities = {result[i]}")

    print(f"Top-1 Accuracy on {len(img_paths)} samples: {acc1:.4f}")
    print(f"Top-5 Accuracy on {len(img_paths)} samples: {acc5:.4f}")
    return acc1, acc5

if __name__ == '__main__':
    test_dir = "/mnt/c/data/MNIST/test"
    acc1, acc5 = testAPI(test_dir)