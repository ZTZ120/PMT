from unittest import TestCase
from LeNet import testAPI
import numpy as np

class LeNetTest(TestCase):

    def test_testAPI(self):
        """
        测试testAPI函数，验证其返回结果的值是否与期望的值相等。
        """
        # 调用testAPI函数并获取结果

        result = testAPI(["/mnt/c/data/MNIST/test/4/4.png"])
        result_softmax = result[0]
        expected_softmax = np.array([[1.29201702e-07, 1.02468810e-06, 1.56674555e-07, 1.37543306e-06,
       9.99725365e-01, 2.72165380e-06, 1.42751531e-06, 8.20035924e-06,
       2.26352678e-07, 2.59372917e-04]])
        # 使用numpy的allclose方法检查两个数组是否近似相等
        self.assertTrue(np.allclose(result_softmax, expected_softmax, atol=1e-6),
                        "Softmax output does not match the expected result.")

#if __name__ == '__main__':
#    test_testAPI()
