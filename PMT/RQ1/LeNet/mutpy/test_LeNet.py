from unittest import TestCase
from LeNet import testAPI
import numpy as np

class LeNetTest(TestCase):

    def test_testAPI(self):
        """
        测试testAPI函数，验证其返回结果的值是否与期望的值相等。
        """
        # 调用testAPI函数并获取结果

        result = testAPI(["D:\\data\\MNIST\\test\\4\\4.png"])
        result_softmax = result[0]
        expected_softmax = np.array([[1.5687661e-08, 5.2518129e-07, 5.7097554e-07, 9.0370457e-07,
       9.9763858e-01, 1.7803581e-04, 7.8367316e-07, 4.6769346e-05,
       8.4706187e-07, 2.1330470e-03]])
        # 使用numpy的allclose方法检查两个数组是否近似相等
        self.assertTrue(np.allclose(result_softmax, expected_softmax, atol=1e-6),
                        "Softmax output does not match the expected result.")

