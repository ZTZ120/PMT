from unittest import TestCase
from VGG19 import testAPI
import numpy as np

class VGG19Test(TestCase):


    def test_testAPI(self):
        """
        测试testAPI函数，验证其返回结果的值是否与期望的值相等。
        """
        # 调用testAPI函数并获取结果

        result = testAPI(["D:\\data\\MNIST\\test\\4\\4.png"])
        result_softmax = result[0]
        expected_softmax = np.array([[2.00004180e-10, 3.44885676e-09, 7.15788140e-09, 2.01464428e-10,
       9.99878645e-01, 1.00113645e-07, 2.42445765e-07, 1.53065898e-07,
       1.91034260e-07, 1.20614815e-04]])
        # 使用numpy的allclose方法检查两个数组是否近似相等
        self.assertTrue(np.allclose(result_softmax, expected_softmax, atol=1e-6),
                        "Softmax output does not match the expected result.")

#if __name__ == '__main__':
#    test_testAPI()

