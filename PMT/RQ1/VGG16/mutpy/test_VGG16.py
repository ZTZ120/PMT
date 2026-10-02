from unittest import TestCase
from VGG16 import testAPI
import numpy as np


class VGG16Test(TestCase):

    def test_testAPI(self):
        """
        测试testAPI函数，验证其返回结果的值是否与期望的值相等。
        """
        # 调用testAPI函数并获取结果

        result = testAPI(["D:\\data\\MNIST\\test\\4\\4.png"])
        result_softmax = result[0]

        expected_softmax = np.array([[2.1464568e-09, 3.5459106e-08, 7.5614688e-09, 2.8260319e-09,
       9.9933511e-01, 1.1931269e-07, 3.0047084e-07, 2.0692210e-06,
       1.4517326e-07, 6.6220452e-04]])
        # 使用numpy的allclose方法检查两个数组是否近似相等
        self.assertTrue(np.allclose(result_softmax, expected_softmax, atol=1e-6),
                        "Softmax output does not match the expected result.")

