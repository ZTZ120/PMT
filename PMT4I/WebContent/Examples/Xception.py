import datetime
import os

from keras.preprocessing import image

from keras.applications.xception import Xception
from keras.applications.vgg16 import VGG16
from keras.applications.vgg19 import VGG19
from keras.applications.resnet50 import ResNet50
from keras.applications.inception_v3 import InceptionV3
from keras.applications.inception_resnet_v2 import InceptionResNetV2
from keras.applications.mobilenet import MobileNet
from keras.applications.densenet import DenseNet121
from keras.applications.densenet import DenseNet169
from keras.applications.densenet import DenseNet201
from keras.applications.nasnet import NASNetMobile

from keras.applications.xception import preprocess_input,decode_predictions
#from keras.applications.vgg16 import preprocess_input,decode_predictions
#from keras.applications.vgg19 import preprocess_input,decode_predictions
#from keras.applications.resnet50 import preprocess_input,decode_predictions
#from keras.applications.inception_v3 import preprocess_input,decode_predictions
#from keras.applications.inception_resnet_v2 import preprocess_input,decode_predictions
#from keras.applications.mobilenet import preprocess_input,decode_predictions
#from keras.applications.densenet import preprocess_input,decode_predictions
#from keras.applications.nasnet import preprocess_input,decode_predictions

import numpy as np

def testAPI(test_routes):
    #AlexNet
    #ShuffleNet
    #YOLO
    h5file = os.path.dirname(os.path.realpath(__file__)) + '/cfg/xception_weights_tf_dim_ordering_tf_kernels.h5'
    model = Xception(weights=h5file)
    #model = VGG16(weights='imagenet')
    #model = VGG19(weights='imagenet')
    #model = ResNet50(weights='imagenet')
    #model = InceptionV3(weights='imagenet')
    #model = InceptionResNetV2(weights='imagenet')
    #model = MobileNet(weights='imagenet')
    #model = DenseNet121(weights='imagenet')
    #model = DenseNet169(weights='imagenet')
    #model = DenseNet201(weights='imagenet')
    #model = NASNetMobile(weights='imagenet')
    batch_size=16
    # 用于存储结果
    result = []

    # 批次处理
    for i in range(0, len(test_routes), batch_size):
        print("执行所有图像:", i + 1, '/', len(test_routes))

        # 加载批次图像
        batch_images = []
        for j in range(i, min(i + batch_size, len(test_routes))):
            img = image.load_img(test_routes[j], target_size=(299, 299))
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

