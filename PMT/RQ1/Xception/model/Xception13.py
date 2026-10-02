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

@keras_export(
    [
        "keras.applications.xception.Xception",
        "keras.applications.Xception",
    ]
)
def Xception(
    include_top=True,
    weights=None,
    input_tensor=None,
    input_shape=(71,71,3),
    pooling=None,
    classes=10,
    classifier_activation="softmax",
    name="xception",
):

    img_input = layers.Input(shape=input_shape)

    channel_axis = 1 if backend.image_data_format() == "channels_first" else -1

    x = layers.Conv2D(
        32, (3, 3), strides=2, use_bias=False, name="block1_conv1"
    )(img_input)
    x = layers.BatchNormalization(axis=channel_axis)(x)
    x = layers.Activation("relu")(x)
    #x = layers.Conv2D(64, (3, 3), use_bias=False, name="block1_conv2")(x)
    x = layers.Conv2D(64, (4, 3), use_bias=False, name="block1_conv2")(x) #变体13-27
    x = layers.BatchNormalization(axis=channel_axis)(x)
    x = layers.Activation("relu")(x)

    residual = layers.Conv2D(
        128, (1, 1), strides=2, padding="same", use_bias=False
    )(x)
    residual = layers.BatchNormalization(axis=channel_axis)(residual)

    x = layers.SeparableConv2D(
        128, (3, 3), padding="same", use_bias=False, name="block2_sepconv1"
    )(x)
    x = layers.BatchNormalization(axis=channel_axis)(x)
    x = layers.Activation("relu")(x)
    x = layers.SeparableConv2D(
        128, (3, 3), padding="same", use_bias=False, name="block2_sepconv2"
    )(x)
    x = layers.BatchNormalization(axis=channel_axis)(x)

    x = layers.MaxPooling2D(
        (3, 3), strides=2, padding="same"
    )(x)
    x = layers.add([x, residual])

    residual = layers.Conv2D(
        256, (1, 1), strides=2, padding="same", use_bias=False
    )(x)
    residual = layers.BatchNormalization(axis=channel_axis)(residual)

    x = layers.Activation("relu")(x)
    x = layers.SeparableConv2D(
        256, (3, 3), padding="same", use_bias=False, name="block3_sepconv1"
    )(x)
    x = layers.BatchNormalization(axis=channel_axis)(x)
    x = layers.Activation("relu")(x)
    x = layers.SeparableConv2D(
        256, (3, 3), padding="same", use_bias=False, name="block3_sepconv2"
    )(x)
    x = layers.BatchNormalization(axis=channel_axis)(x)

    x = layers.MaxPooling2D(
        (3, 3), strides=2, padding="same"
    )(x)
    x = layers.add([x, residual])

    residual = layers.Conv2D(
        728, (1, 1), strides=2, padding="same", use_bias=False
    )(x)
    residual = layers.BatchNormalization(axis=channel_axis)(residual)

    x = layers.Activation("relu")(x)
    x = layers.SeparableConv2D(
        728, (3, 3), padding="same", use_bias=False, name="block4_sepconv1"
    )(x)
    x = layers.BatchNormalization(axis=channel_axis)(x)
    x = layers.Activation("relu")(x)
    x = layers.SeparableConv2D(
        728, (3, 3), padding="same", use_bias=False, name="block4_sepconv2"
    )(x)
    x = layers.BatchNormalization(axis=channel_axis)(x)

    x = layers.MaxPooling2D(
        (3, 3), strides=2, padding="same"
    )(x)
    x = layers.add([x, residual])

    for i in range(8):
        residual = x
        prefix = f"block{i + 5}"

        x = layers.Activation("relu")(x)
        x = layers.SeparableConv2D(
            728,
            (3, 3),
            padding="same",
            use_bias=False,
            name=f"{prefix}_sepconv1",
        )(x)
        x = layers.BatchNormalization(
            axis=channel_axis
        )(x)
        x = layers.Activation("relu")(x)
        x = layers.SeparableConv2D(
            728,
            (3, 3),
            padding="same",
            use_bias=False,
            name=f"{prefix}_sepconv2",
        )(x)
        x = layers.BatchNormalization(
            axis=channel_axis
        )(x)
        x = layers.Activation("relu")(x)
        x = layers.SeparableConv2D(
            728,
            (3, 3),
            padding="same",
            use_bias=False,
            name=f"{prefix}_sepconv3",
        )(x)
        x = layers.BatchNormalization(
            axis=channel_axis
        )(x)

        x = layers.add([x, residual])

    residual = layers.Conv2D(
        1024, (1, 1), strides=2, padding="same", use_bias=False
    )(x)
    residual = layers.BatchNormalization(axis=channel_axis)(residual)

    x = layers.Activation("relu")(x)
    x = layers.SeparableConv2D(
        728, (3, 3), padding="same", use_bias=False, name="block13_sepconv1"
    )(x)
    x = layers.BatchNormalization(
        axis=channel_axis
    )(x)
    x = layers.Activation("relu")(x)
    x = layers.SeparableConv2D(
        1024, (3, 3), padding="same", use_bias=False, name="block13_sepconv2"
    )(x)
    x = layers.BatchNormalization(
        axis=channel_axis
    )(x)

    x = layers.MaxPooling2D(
        (3, 3), strides=2, padding="same"
    )(x)
    x = layers.add([x, residual])

    x = layers.SeparableConv2D(
        1536, (3, 3), padding="same", use_bias=False, name="block14_sepconv1"
    )(x)
    x = layers.BatchNormalization(
        axis=channel_axis
    )(x)
    x = layers.Activation("relu")(x)

    x = layers.SeparableConv2D(
        2048, (3, 3), padding="same", use_bias=False, name="block14_sepconv2"
    )(x)
    x = layers.BatchNormalization(
        axis=channel_axis
    )(x)
    x = layers.Activation("relu")(x)
    # Classification
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
            img = image.load_img(img_path.numpy().decode('utf-8'), target_size=(71, 71), color_mode="rgb")
            img = img.point(lambda i: 255 - i)
            arr = np.divide(np.array(img, dtype=np.float32), 255.0)
            return arr

        img = tf.py_function(py_load_img, [img_path], tf.float32)
        img.set_shape([71, 71, 3])
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
    model = Xception(input_shape=(71,71,3),classes=n_classes)


    epochs=1
    # 训练
    #model.fit(dataset, epochs=epochs)

    # 保存 h5 权重文件
    base_name = os.path.splitext(os.path.basename(__file__))[0]
    ck_dir = os.path.join('/mnt/c/RQ1/Xception', f'checkpoint{base_name}')
    #ck_dir = '/mnt/c/RQ1/Xception/checkpointXception'
    os.makedirs(ck_dir, exist_ok=True)
    weights_path = os.path.join(ck_dir, 'Xception_model.weights.h5')
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
        img_test = image.load_img(img_path, target_size=(71, 71), color_mode="rgb")
        img_test = img_test.point(lambda i: 255 - i)
        image_test = np.divide(np.array(img_test, dtype=np.float32), 255.0)
        batch_imgs.append(image_test)
    batch_imgs = np.array(batch_imgs)
    # 预测
    preds = model.predict(batch_imgs, batch_size=300)
    result.extend(preds)
    return result


