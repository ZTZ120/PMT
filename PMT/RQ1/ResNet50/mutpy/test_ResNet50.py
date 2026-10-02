from unittest import TestCase
from ResNet50 import testAPI
import numpy as np

class DemoTest(TestCase):

    def test_testAPI(self):
        """
        测试testAPI函数，验证其返回结果的值是否与期望的值相等。
        """
        # 调用testAPI函数并获取结果
        result = testAPI(["D:\\data\\MNIST\\test\\4\\4.png"])
        result_softmax = result[0]
        expected_softmax = np.array([[3.87029537e-08, 1.40210235e-08, 1.31374849e-08, 1.56789497e-08,
       9.99994636e-01, 5.61645663e-07, 8.68355130e-08, 4.17158965e-08,       
       3.48192884e-06, 1.01133344e-06]])
        # 使用numpy的allclose方法检查两个数组是否近似相等
        self.assertTrue(np.allclose(result_softmax, expected_softmax, atol=1e-6),
                        "Softmax output does not match the expected result.")

#if __name__ == '__main__':
#    test_testAPI()
