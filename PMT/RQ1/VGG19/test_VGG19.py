from unittest import TestCase
from VGG19 import testAPI
import numpy as np

class VGG19Test(TestCase):


    def test_testAPI(self):
        """
        测试testAPI函数，验证其返回结果的值是否与期望的值相等。
        """
        # 调用testAPI函数并获取结果

        result = testAPI(["/mnt/c/data/MNIST/test/4/4.png"])
        result_softmax = result[0]
        expected_softmax = np.array([[1.9976099e-10, 3.4455567e-09, 7.1508275e-09, 2.0124095e-10,
       9.9987876e-01, 1.0002873e-07, 2.4222112e-07, 1.5295385e-07,
       1.9088169e-07, 1.2057687e-04]])
        # 使用numpy的allclose方法检查两个数组是否近似相等
        self.assertTrue(np.allclose(result_softmax, expected_softmax, atol=1e-6),
                        "Softmax output does not match the expected result.")

#if __name__ == '__main__':
#    test_testAPI()

