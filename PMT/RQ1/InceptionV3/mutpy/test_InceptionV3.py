from unittest import TestCase
from InceptionV3 import testAPI
import numpy as np

class DemoTest(TestCase):

    def test_testAPI(self):
        """
        测试testAPI函数，验证其返回结果的值是否与期望的值相等。
        """
        # 调用testAPI函数并获取结果

        result = testAPI(["D:\\data\\MNIST\\test\\4\\4.png"])
        result_softmax = result[0]
        expected_softmax = np.array([[3.7817699e-10, 3.0605112e-05, 7.7861961e-10, 4.3630013e-12,
       9.9996841e-01, 1.5803184e-13, 1.4184152e-10, 2.2904088e-08,
       5.3994548e-10, 1.0194605e-06]])
        # 使用numpy的allclose方法检查两个数组是否近似相等
        self.assertTrue(np.allclose(result_softmax, expected_softmax, atol=1e-6),
                        "Softmax output does not match the expected result.")

#if __name__ == '__main__':
#    test_testAPI()
