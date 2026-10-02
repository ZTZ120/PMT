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
        "keras.applications.inception_v3.InceptionV3",
        "keras.applications.InceptionV3",
    ]
)
def InceptionV3(
    include_top=True,
    weights=None,
    input_tensor=None,
    input_shape=(75,75,3),
    pooling=None,
    classes=10,
    classifier_activation="softmax",
    name="inception_v3",
):

    img_input = layers.Input(shape=input_shape)

    if backend.image_data_format() == "channels_first":
        channel_axis = 1
    else:
        channel_axis = 3

    x = conv2d_bn(img_input, 32, 3, 3, strides=(2, 2), padding="valid")
    x = conv2d_bn(x, 32, 3, 3, padding="valid")
    x = conv2d_bn(x, 64, 3, 3)
    x = layers.MaxPooling2D((3, 3), strides=(2, 2))(x)

    x = conv2d_bn(x, 80, 1, 1, padding="valid")
    x = conv2d_bn(x, 192, 3, 3, padding="valid")
    x = layers.MaxPooling2D((3, 3), strides=(2, 2))(x)

    # mixed 0
    branch1x1 = conv2d_bn(x, 64, 1, 1)

    branch5x5 = conv2d_bn(x, 48, 1, 1)
    branch5x5 = conv2d_bn(branch5x5, 64, 5, 5)

    branch3x3dbl = conv2d_bn(x, 64, 1, 1)
    branch3x3dbl = conv2d_bn(branch3x3dbl, 96, 3, 3)
    branch3x3dbl = conv2d_bn(branch3x3dbl, 96, 3, 3)

    branch_pool = layers.AveragePooling2D(
        (3, 3), strides=(1, 1), padding="same"
    )(x)
    branch_pool = conv2d_bn(branch_pool, 32, 1, 1)
    x = layers.concatenate(
        [branch1x1, branch5x5, branch3x3dbl, branch_pool],
        axis=channel_axis,
        name="mixed0",
    )

    # mixed 1
    #branch1x1 = conv2d_bn(x, 64, 1, 1)
    branch1x1 = conv2d_bn(x, 65, 1, 1)  #变体37-83

    branch5x5 = conv2d_bn(x, 48, 1, 1)
    branch5x5 = conv2d_bn(branch5x5, 64, 5, 5)

    branch3x3dbl = conv2d_bn(x, 64, 1, 1)
    branch3x3dbl = conv2d_bn(branch3x3dbl, 96, 3, 3)
    branch3x3dbl = conv2d_bn(branch3x3dbl, 96, 3, 3)

    branch_pool = layers.AveragePooling2D(
        (3, 3), strides=(1, 1), padding="same"
    )(x)
    branch_pool = conv2d_bn(branch_pool, 64, 1, 1)
    x = layers.concatenate(
        [branch1x1, branch5x5, branch3x3dbl, branch_pool],
        axis=channel_axis,
        name="mixed1",
    )

    # mixed 2
    branch1x1 = conv2d_bn(x, 64, 1, 1)

    branch5x5 = conv2d_bn(x, 48, 1, 1)
    branch5x5 = conv2d_bn(branch5x5, 64, 5, 5)

    branch3x3dbl = conv2d_bn(x, 64, 1, 1)
    branch3x3dbl = conv2d_bn(branch3x3dbl, 96, 3, 3)
    branch3x3dbl = conv2d_bn(branch3x3dbl, 96, 3, 3)

    branch_pool = layers.AveragePooling2D(
        (3, 3), strides=(1, 1), padding="same"
    )(x)
    branch_pool = conv2d_bn(branch_pool, 64, 1, 1)
    x = layers.concatenate(
        [branch1x1, branch5x5, branch3x3dbl, branch_pool],
        axis=channel_axis,
        name="mixed2",
    )

    # mixed 3
    branch3x3 = conv2d_bn(x, 384, 3, 3, strides=(2, 2), padding="valid")

    branch3x3dbl = conv2d_bn(x, 64, 1, 1)
    branch3x3dbl = conv2d_bn(branch3x3dbl, 96, 3, 3)
    branch3x3dbl = conv2d_bn(
        branch3x3dbl, 96, 3, 3, strides=(2, 2), padding="valid"
    )

    branch_pool = layers.MaxPooling2D((3, 3), strides=(2, 2))(x)
    x = layers.concatenate(
        [branch3x3, branch3x3dbl, branch_pool], axis=channel_axis, name="mixed3"
    )

    # mixed 4
    branch1x1 = conv2d_bn(x, 192, 1, 1)

    branch7x7 = conv2d_bn(x, 128, 1, 1)
    branch7x7 = conv2d_bn(branch7x7, 128, 1, 7)
    branch7x7 = conv2d_bn(branch7x7, 192, 7, 1)

    branch7x7dbl = conv2d_bn(x, 128, 1, 1)
    branch7x7dbl = conv2d_bn(branch7x7dbl, 128, 7, 1)
    branch7x7dbl = conv2d_bn(branch7x7dbl, 128, 1, 7)
    branch7x7dbl = conv2d_bn(branch7x7dbl, 128, 7, 1)
    branch7x7dbl = conv2d_bn(branch7x7dbl, 192, 1, 7)

    branch_pool = layers.AveragePooling2D(
        (3, 3), strides=(1, 1), padding="same"
    )(x)
    branch_pool = conv2d_bn(branch_pool, 192, 1, 1)
    x = layers.concatenate(
        [branch1x1, branch7x7, branch7x7dbl, branch_pool],
        axis=channel_axis,
        name="mixed4",
    )

    # mixed 5, 6
    for i in range(2):
        branch1x1 = conv2d_bn(x, 192, 1, 1)

        branch7x7 = conv2d_bn(x, 160, 1, 1)
        branch7x7 = conv2d_bn(branch7x7, 160, 1, 7)
        branch7x7 = conv2d_bn(branch7x7, 192, 7, 1)

        branch7x7dbl = conv2d_bn(x, 160, 1, 1)
        branch7x7dbl = conv2d_bn(branch7x7dbl, 160, 7, 1)
        branch7x7dbl = conv2d_bn(branch7x7dbl, 160, 1, 7)
        branch7x7dbl = conv2d_bn(branch7x7dbl, 160, 7, 1)
        branch7x7dbl = conv2d_bn(branch7x7dbl, 192, 1, 7)

        branch_pool = layers.AveragePooling2D(
            (3, 3), strides=(1, 1), padding="same"
        )(x)
        branch_pool = conv2d_bn(branch_pool, 192, 1, 1)
        x = layers.concatenate(
            [branch1x1, branch7x7, branch7x7dbl, branch_pool],
            axis=channel_axis,
            name="mixed{0}".format(5 + i),
        )

    # mixed 7
    branch1x1 = conv2d_bn(x, 192, 1, 1)

    branch7x7 = conv2d_bn(x, 192, 1, 1)
    branch7x7 = conv2d_bn(branch7x7, 192, 1, 7)
    branch7x7 = conv2d_bn(branch7x7, 192, 7, 1)

    branch7x7dbl = conv2d_bn(x, 192, 1, 1)
    branch7x7dbl = conv2d_bn(branch7x7dbl, 192, 7, 1)
    branch7x7dbl = conv2d_bn(branch7x7dbl, 192, 1, 7)
    branch7x7dbl = conv2d_bn(branch7x7dbl, 192, 7, 1)
    branch7x7dbl = conv2d_bn(branch7x7dbl, 192, 1, 7)

    branch_pool = layers.AveragePooling2D(
        (3, 3), strides=(1, 1), padding="same"
    )(x)
    branch_pool = conv2d_bn(branch_pool, 192, 1, 1)
    x = layers.concatenate(
        [branch1x1, branch7x7, branch7x7dbl, branch_pool],
        axis=channel_axis,
        name="mixed7",
    )

    # mixed 8
    branch3x3 = conv2d_bn(x, 192, 1, 1)
    branch3x3 = conv2d_bn(branch3x3, 320, 3, 3, strides=(2, 2), padding="valid")

    branch7x7x3 = conv2d_bn(x, 192, 1, 1)
    branch7x7x3 = conv2d_bn(branch7x7x3, 192, 1, 7)
    branch7x7x3 = conv2d_bn(branch7x7x3, 192, 7, 1)
    branch7x7x3 = conv2d_bn(
        branch7x7x3, 192, 3, 3, strides=(2, 2), padding="valid"
    )

    branch_pool = layers.MaxPooling2D((3, 3), strides=(2, 2))(x)
    x = layers.concatenate(
        [branch3x3, branch7x7x3, branch_pool], axis=channel_axis, name="mixed8"
    )

    # mixed 9
    for i in range(2):
        branch1x1 = conv2d_bn(x, 320, 1, 1)

        branch3x3 = conv2d_bn(x, 384, 1, 1)
        branch3x3_1 = conv2d_bn(branch3x3, 384, 1, 3)
        branch3x3_2 = conv2d_bn(branch3x3, 384, 3, 1)
        branch3x3 = layers.concatenate(
            [branch3x3_1, branch3x3_2],
            axis=channel_axis,
            name=f"mixed9_{i}",
        )

        branch3x3dbl = conv2d_bn(x, 448, 1, 1)
        branch3x3dbl = conv2d_bn(branch3x3dbl, 384, 3, 3)
        branch3x3dbl_1 = conv2d_bn(branch3x3dbl, 384, 1, 3)
        branch3x3dbl_2 = conv2d_bn(branch3x3dbl, 384, 3, 1)
        branch3x3dbl = layers.concatenate(
            [branch3x3dbl_1, branch3x3dbl_2], axis=channel_axis
        )

        branch_pool = layers.AveragePooling2D(
            (3, 3), strides=(1, 1), padding="same"
        )(x)
        branch_pool = conv2d_bn(branch_pool, 192, 1, 1)
        x = layers.concatenate(
            [branch1x1, branch3x3, branch3x3dbl, branch_pool],
            axis=channel_axis,
            name=f"mixed{9 + i}",
        )
    # Classification block
    x = layers.GlobalAveragePooling2D(name="avg_pool")(x)
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

def conv2d_bn(
    x, filters, num_row, num_col, padding="same", strides=(1, 1), name=None
):

    if name is not None:
        bn_name = f"{name}_bn"
        conv_name = f"{name}_conv"
    else:
        bn_name = None
        conv_name = None
    if backend.image_data_format() == "channels_first":
        bn_axis = 1
    else:
        bn_axis = 3
    x = layers.Conv2D(
        filters,
        (num_row, num_col),
        strides=strides,
        padding=padding,
        use_bias=False,
        name=conv_name,
    )(x)
    x = layers.BatchNormalization(axis=bn_axis, scale=False, name=bn_name)(x)
    x = layers.Activation("relu", name=name)(x)
    return x

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
            img = image.load_img(img_path.numpy().decode('utf-8'), target_size=(75, 75), color_mode="rgb")
            img = img.point(lambda i: 255 - i)
            arr = np.divide(np.array(img, dtype=np.float32), 255.0)
            return arr

        img = tf.py_function(py_load_img, [img_path], tf.float32)
        img.set_shape([75, 75, 3]) 
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
    model = InceptionV3(input_shape=(75,75,3),classes=n_classes)


    epochs=2
    #训练
    #model.fit(dataset, epochs=epochs)

    base_name = os.path.splitext(os.path.basename(__file__))[0]
    ck_dir = os.path.join('/mnt/c/RQ1/InceptionV3', f'checkpoint{base_name}')
    #ck_dir = '/mnt/c/RQ1/InceptionV3/checkpoint'
    os.makedirs(ck_dir, exist_ok=True)
    weights_path = os.path.join(ck_dir, 'InceptionV3_model.weights.h5')
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
        img_test = image.load_img(img_path, target_size=(75, 75), color_mode="rgb")
        img_test = img_test.point(lambda i: 255 - i)
        image_test = np.divide(np.array(img_test, dtype=np.float32), 255.0)
        batch_imgs.append(image_test)
    batch_imgs = np.array(batch_imgs)
    # 预测
    preds = model.predict(batch_imgs, batch_size=300)
    result.extend(preds)
    return result


