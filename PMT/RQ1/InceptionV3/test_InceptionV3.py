from unittest import TestCase
from InceptionV3 import testAPI
import numpy as np

class DemoTest(TestCase):

    def test_testAPI(self):
        """
        测试testAPI函数，验证其返回结果的值是否与期望的值相等。
        """
        # 调用testAPI函数并获取结果

        result = testAPI(["/mnt/c/data/MNIST/test/4/4.png"])
        result_softmax = result[0]
        expected_softmax = np.array([[3.7693357e-10, 3.0085561e-05, 7.5727430e-10, 4.0715322e-12,
       9.9996901e-01, 1.4929494e-13, 1.3802648e-10, 2.2609855e-08,
       5.1972449e-10, 9.8971475e-07]])
        # 使用numpy的allclose方法检查两个数组是否近似相等
        self.assertTrue(np.allclose(result_softmax, expected_softmax, atol=1e-6),
                        "Softmax output does not match the expected result.")

#if __name__ == '__main__':
#    test_testAPI()
