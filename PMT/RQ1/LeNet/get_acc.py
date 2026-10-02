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

random.seed(1)

def lenet(input_shape=(28,28,1), n_classes=10):
    init=tf.keras.initializers.GlorotUniform(seed=1)
    inputs = layers.Input(shape=input_shape)
    # Conv1 5x5 -> 6
    x = layers.Conv2D(6, (5,5), activation='relu', padding='valid',
                        kernel_initializer=init)(inputs)
    x = layers.AveragePooling2D(pool_size=(2,2), strides=2)(x)
    # Conv2 5x5 -> 16
    x = layers.Conv2D(16, (5,5), activation='relu', padding='valid',
                        kernel_initializer=init)(x)
    x = layers.AveragePooling2D(pool_size=(2,2), strides=2)(x)
    # FC
    x = layers.Flatten()(x)
    x = layers.Dense(120, activation='relu',
                        kernel_initializer=init)(x)
    x = layers.Dense(84, activation='relu',
                        kernel_initializer=init)(x)
    outputs = layers.Dense(n_classes, activation='softmax',
                            kernel_initializer=init)(x)
    return models.Model(inputs, outputs, name='lenet')

def testAPI(teststr):
    K.clear_session()

    #训练数据集
    train = "/mnt/c/data/MNIST/train"
    classes = ['0','1','2','3','4','5','6','7','8','9']
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
        label = [0]*n_classes
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
    model.summary()
    epochs=1
    # 训练
    #model.fit(dataset, epochs=epochs)

    # 保存 h5 权重文件
    #base_name = os.path.splitext(os.path.basename(__file__))[0]
    #ck_dir = os.path.join('/mnt/c/RQ1/LeNet', f'checkpoint{base_name}')
    ck_dir = '/mnt/c/RQ1/LeNet/checkpointLeNet'
    os.makedirs(ck_dir, exist_ok=True)
    weights_path = os.path.join(ck_dir, 'LeNet_model.weights.h5')
    #model.save_weights(weights_path)
    model.load_weights(weights_path)

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
        img_test = image.load_img(img_path, target_size=(28, 28), color_mode="grayscale")
        img_test = img_test.point(lambda i: 255 - i)
        image_test = np.array(img_test, dtype=np.float32)
        image_test = np.expand_dims(image_test, axis=-1)
        batch_imgs.append(image_test)

    # 转换为 NumPy 数组
    batch_imgs = np.array(batch_imgs, dtype=np.float32)

    # 一次性预测所有图片
    result = model(batch_imgs, training=False).numpy()
    # 预测
    y_true = np.argmax(labels, axis=1)
    pred_top1 = np.argmax(result, axis=1)

    acc1 = np.mean(pred_top1 == y_true)
    top5_preds = np.argsort(result, axis=1)[:, -5:]
    acc5 = np.mean([y_true[i] in top5_preds[i] for i in range(len(y_true))])

    # 打印预测错误的样本
    for i in range(len(img_paths)):
        if pred_top1[i] != y_true[i]:
            print(f"Sample {i}: Path = {img_paths[i]}, True Label = {y_true[i]}, Predicted = {pred_top1[i]}, Probabilities = {result[i]}")

    print(f"Top-1 Accuracy on {len(img_paths)} samples: {acc1:.4f}")
    print(f"Top-5 Accuracy on {len(img_paths)} samples: {acc5:.4f}")
    return acc1, acc5

if __name__ == '__main__':
    test_dir = "/mnt/c/data/MNIST/test"
    acc1, acc5 = testAPI(test_dir)