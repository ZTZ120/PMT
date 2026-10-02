import os
import math
import glob
import random
from pathlib import Path
import numpy as np
from PIL import Image
import tensorflow as tf
from keras.preprocessing import image
from keras import layers, models, backend as K

def lenet(input_shape=(28,28,1), n_classes=10):
    inputs = layers.Input(shape=input_shape)
    # Conv1 5x5 -> 6
    x = layers.Conv2D(6, (5,5), activation='relu', padding='valid',
                        kernel_initializer=tf.keras.initializers.GlorotUniform(seed=1))(inputs)
    x = layers.AveragePooling2D(pool_size=(2,2), strides=2)(x)
    # Conv2 5x5 -> 16
    x = layers.Conv2D(16, (5,5), activation='relu', padding='valid',
                        kernel_initializer=tf.keras.initializers.GlorotUniform(seed=1))(x)
    x = layers.AveragePooling2D(pool_size=(2,2), strides=2)(x)
    # FC
    x = layers.Flatten()(x)
    x = layers.Dense(120, activation='relu',
                        kernel_initializer=tf.keras.initializers.GlorotUniform(seed=1))(x)
    x = layers.Dense(84, activation='relu',
                        kernel_initializer=tf.keras.initializers.GlorotUniform(seed=1))(x)
    outputs = layers.Dense(n_classes, activation='softmax',
                            kernel_initializer=tf.keras.initializers.GlorotUniform(seed=1))(x)
    return models.Model(inputs, outputs, name='lenet')

def testAPI(teststr):
    K.clear_session()
    # 固定随机种子
    tf.random.set_seed(1)
    np.random.seed(1)
    random.seed(1)
    #训练数据集
    train = "/mnt/c/data/MNIST/train"
    #classes = ['0','1','2','3','4','5','6','7','8','9']
    classes = ['0','1','2','3','4','5','6','7','','9']#变体40-66
    n_classes = len(classes)

    def preprocess_img(img_path, label):
        def py_load_img(img_path):
            img = image.load_img(img_path.numpy().decode('utf-8'), target_size=(28, 28), color_mode="grayscale")
            img = img.point(lambda i: 255 - i)
            arr = np.array(img, dtype=np.float32)
            arr = np.expand_dims(arr, axis=-1)
            return arr
        img = tf.py_function(py_load_img, [img_path], tf.float32)
        img.set_shape([28, 28, 1]) 
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
    model = lenet(input_shape=(28,28,1),n_classes=n_classes)
    model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=1e-4),
                  loss='categorical_crossentropy',
                  metrics=['accuracy'])

    epochs=1
    # 训练
    model.fit(dataset, epochs=epochs)
    # 保存 h5 权重文件
    base_name = os.path.splitext(os.path.basename(__file__))[0]
    ck_dir = os.path.join('/mnt/c/RQ1/LeNet', f'checkpoint{base_name}')
    #ck_dir = '/mnt/c/RQ1/LeNet/checkpoint'
    os.makedirs(ck_dir, exist_ok=True)
    weights_path = os.path.join(ck_dir, 'LeNet_model.weights.h5')
    model.save_weights(weights_path)
    #model.load_weights(weights_path)

    # 处理测试图片路径列表
    test_paths = teststr
    result = []
    batch_imgs = []
    for img_path in test_paths:
        label_test = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        img_test = image.load_img(img_path, target_size=(28, 28), color_mode="grayscale")
        img_test = img_test.point(lambda i: 255 - i)
        image_test = np.array(img_test, dtype=np.float32)
        image_test = np.expand_dims(image_test, axis=-1)
        batch_imgs.append(image_test)
    batch_imgs = np.array(batch_imgs, dtype=np.float32)
    # 预测
    preds = model(batch_imgs, training=False).numpy()
    result.extend(preds)
    return result

if __name__ == '__main__':
    result = testAPI(["/mnt/c/data/MNIST/test/4/4.png"])
    print(result)
