from unittest import TestCase
from DenseNet121 import testAPI
import numpy as np

class DemoTest(TestCase):

    def test_testAPI(self):
        """
        测试testAPI函数，验证其返回结果的值是否与期望的值相等。
        """
        # 调用testAPI函数并获取结果

        result = testAPI(["/mnt/c/data/MNIST/test/4/4.png"])
        result_softmax = result[0]
        expected_softmax = np.array([[4.5903274e-05, 4.8423542e-05, 3.3145763e-05, 3.6191492e-04,
       9.9742222e-01, 1.6889706e-05, 1.5146095e-04, 1.6228977e-04,
       1.6628617e-05, 1.7411292e-03]])
        # 使用numpy的allclose方法检查两个数组是否近似相等
        self.assertTrue(np.allclose(result_softmax, expected_softmax, atol=1e-6),
                        "Softmax output does not match the expected result.")

#if __name__ == '__main__':
#    test_testAPI()
