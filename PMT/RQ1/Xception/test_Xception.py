from unittest import TestCase
from Xception import testAPI
import numpy as np

class XceptionTest(TestCase):

    def test_testAPI(self):
        """
        测试testAPI函数，验证其返回结果的值是否与期望的值相等。
        """
        # 调用testAPI函数并获取结果

        result = testAPI(["/mnt/c/data/MNIST/test/4/4.png"])
        result_softmax = result[0]

        expected_softmax = np.array([[3.8439254e-07, 1.2280929e-06, 1.9525887e-06, 1.4167428e-05,
       9.9987805e-01, 2.6778850e-06, 8.5631814e-07, 7.7918339e-05,
       1.7797277e-07, 2.2571601e-05]])
        # 使用numpy的allclose方法检查两个数组是否近似相等
        self.assertTrue(np.allclose(result_softmax, expected_softmax, atol=1e-6),
                        "Softmax output does not match the expected result.")

