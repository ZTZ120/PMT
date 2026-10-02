
import os
from keras.preprocessing import image
from keras.applications.nasnet import NASNetMobile
from keras.applications.nasnet import preprocess_input
import numpy as np


def testAPI(test_routes):
    """
    使用 NASNetMobile 模型对指定路径的图像进行分类预测。

    :param test_routes: 包含图像文件路径的列表
    :return: 包含每张图像预测结果的列表
    """
    model = NASNetMobile(weights='imagenet')
    batch_size=16
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
