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

def dense_block(x, blocks, name):

    for i in range(blocks):
        x = conv_block(x, 32, name=f"{name}_block{i + 1}")
    return x

def transition_block(x, reduction, name):

    bn_axis = 3 if backend.image_data_format() == "channels_last" else 1
    x = layers.BatchNormalization(
        axis=bn_axis, epsilon=1.001e-5
    )(x)
    x = layers.Activation("relu")(x)
    x = layers.Conv2D(
        int(x.shape[bn_axis] * reduction),
        1,
        use_bias=False,
        name=f"{name}_conv",
    )(x)
    x = layers.AveragePooling2D(2, strides=2)(x)
    return x

def conv_block(x, growth_rate, name):

    bn_axis = 3 if backend.image_data_format() == "channels_last" else 1
    x1 = layers.BatchNormalization(
        axis=bn_axis, epsilon=1.001e-5
    )(x)
    x1 = layers.Activation("relu")(x1)
    x1 = layers.Conv2D(
        4 * growth_rate, 1, use_bias=False, name=f"{name}_1_conv"
    )(x1)
    x1 = layers.BatchNormalization(
        axis=bn_axis, epsilon=1.001e-5
    )(x1)
    x1 = layers.Activation("relu")(x1)
    x1 = layers.Conv2D(
        growth_rate, 3, padding="same", use_bias=False, name=f"{name}_2_conv"
    )(x1)
    x = layers.Concatenate(axis=bn_axis)([x, x1])
    return x

def DenseNet(
    blocks,
    include_top=True,
    weights=None,
    input_tensor=None,
    input_shape=(32,32,3),
    pooling=None,
    classes=10,
    classifier_activation="softmax",
    name="densenet",
):

    # Determine proper input shape
    input_shape = imagenet_utils.obtain_input_shape(
        input_shape,
        default_size=224,
        min_size=32,
        data_format=backend.image_data_format(),
        require_flatten=include_top,
        weights=weights,
    )

    img_input = layers.Input(shape=input_shape)

    bn_axis = 3 if backend.image_data_format() == "channels_last" else 1

    x = layers.ZeroPadding2D(padding=((3, 3), (3, 3)))(img_input)
    x = layers.Conv2D(64, 7, strides=2, use_bias=False, name="conv1_conv")(x)
    x = layers.BatchNormalization(
        axis=bn_axis, epsilon=1.001e-5
    )(x)
    x = layers.Activation("relu")(x)
    x = layers.ZeroPadding2D(padding=((1, 1), (1, 1)))(x)
    x = layers.MaxPooling2D(3, strides=2, name="pool1")(x)

    x = dense_block(x, blocks[0], name="conv2")
    x = transition_block(x, 0.5, name="pool2")
    x = dense_block(x, blocks[1], name="conv3")
    x = transition_block(x, 0.5, name="pool3")
    x = dense_block(x, blocks[2], name="conv4")
    x = transition_block(x, 0.5, name="pool4")
    x = dense_block(x, blocks[3], name="conv5")

    x = layers.BatchNormalization(axis=bn_axis, epsilon=1.001e-5)(x)
    x = layers.Activation("relu")(x)
    #Classification
    x = layers.GlobalAveragePooling2D()(x)

    imagenet_utils.validate_activation(classifier_activation, weights)
    x = layers.Dense(
        classes, activation=classifier_activation, name="predictions"
    )(x)

    # Ensure that the model takes into account
    if input_tensor is not None:
        inputs = operation_utils.get_source_inputs(input_tensor)
    else:
        inputs = img_input

    # Create model.
    model = Functional(inputs, x, name=name)

    return model

@keras_export(["keras.applications.densenet.DenseNet121","keras.applications.DenseNet121",])
def DenseNet121(
    include_top=True,
    weights=None,
    input_tensor=None,
    input_shape=None,
    pooling=None,
    classes=10,
    classifier_activation="softmax",
    name="densenet121",
):
    """Instantiates the Densenet121 architecture."""
    return DenseNet(
        [6, 12, 24, 16],
        include_top,
        weights,
        input_tensor,
        input_shape,
        pooling,
        classes,
        classifier_activation,
        name=name,
    )

def testAPI(teststr):
    K.clear_session()
    # 固定随机种子
    tf.random.set_seed(1)
    np.random.seed(1)
    random.seed(1)
    #训练数据集
    train = "/mnt/c/data/MNIST/train"
    #classes = ['0','1','2','3','4','5','6','7','8','9']
    classes = ['0','1','2','3','4','5','6','mutpy','8','9'] #变体58-138
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
    model = DenseNet121(input_shape=(32,32,3),classes=n_classes)


    epochs=1
    # 训练
    #model.fit(dataset, epochs=epochs)

    # 保存 h5 权重文件
    base_name = os.path.splitext(os.path.basename(__file__))[0]
    ck_dir = os.path.join('/mnt/c/RQ1/DenseNet121', f'checkpoint{base_name}')
    #ck_dir = '/mnt/c/RQ1/DenseNet121/checkpoint'
    os.makedirs(ck_dir, exist_ok=True)
    weights_path = os.path.join(ck_dir, 'DenseNet121_model.weights.h5')
    #model.save_weights(weights_path)
    model.load_weights(weights_path)
    for layer in model.layers:
        if isinstance(layer, tf.keras.layers.BatchNormalization):
            layer.trainable = False

    # 处理测试图片路径列表
    test_paths = teststr
    result = []
    batch_imgs = []
    for img_path in test_paths:
        label_test = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        img_test = image.load_img(img_path, target_size=(32, 32), color_mode="rgb")
        img_test = img_test.point(lambda i: 255 - i)
        image_test = np.divide(np.array(img_test, dtype=np.float32), 255.0)
        batch_imgs.append(image_test)
    batch_imgs = np.array(batch_imgs)
    # 预测
    preds = model.predict(batch_imgs, batch_size=300)
    result.extend(preds)
    return result


