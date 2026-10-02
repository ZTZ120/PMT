from unittest import TestCase
from VGG16 import testAPI
import numpy as np

class VGG16Test(TestCase):


    def test_testAPI(self):
        """
        测试testAPI函数，验证其返回结果的值是否与期望的值相等。
        """
        # 调用testAPI函数并获取结果

        result = testAPI(["/mnt/c/data/MNIST/test/4/4.png"])
        result_softmax = result[0]

        expected_softmax = np.array([[2.1442526e-09, 3.5427895e-08, 7.5539326e-09, 2.8227469e-09,
       9.9933559e-01, 1.1920253e-07, 3.0026129e-07, 2.0675081e-06,
       1.4504462e-07, 6.6178781e-04]])
        # 使用numpy的allclose方法检查两个数组是否近似相等
        self.assertTrue(np.allclose(result_softmax, expected_softmax, atol=1e-6),
                        "Softmax output does not match the expected result.")



