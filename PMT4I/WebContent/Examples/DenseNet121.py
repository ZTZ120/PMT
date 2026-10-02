import datetime
import os
from keras.preprocessing import image
from keras.applications.densenet import DenseNet121, preprocess_input
import numpy as np
import tensorflow as tf

def testAPI(test_routes):
    h5file = os.path.dirname(os.path.realpath(__file__)) + '/cfg/densenet121_weights_tf_dim_ordering_tf_kernels.h5'
    # 选择模型
    model = DenseNet121(weights=h5file)

    batch_size=16
    # 用于存储结果
    result = []

    # 批次处理
    for i in range(0, len(test_routes), batch_size):
        print("执行所有图像:", i + 1, '/', len(test_routes))

        # 加载批次图像
        batch_images = []
        for j in range(i, min(i + batch_size, len(test_routes))):
            img = image.load_img(test_routes[j], target_size=(224, 224))
            x = image.img_to_array(img)
            batch_images.append(x)

        # 转换为numpy数组
        batch_images = np.array(batch_images)

        # 预处理输入数据
        batch_images = preprocess_input(batch_images)

        # 执行批量预测
        preds = model.predict(batch_images)

        # 将每张图片的预测结果保存到 result 中
        result.extend(preds)

    return result
