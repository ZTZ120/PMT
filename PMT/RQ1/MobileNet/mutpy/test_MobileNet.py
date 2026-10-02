from unittest import TestCase
from MobileNet import testAPI
import numpy as np

class DemoTest(TestCase):

    def test_testAPI(self):
        """
        测试testAPI函数，验证其返回结果的值是否与期望的值相等。
        """
        # 调用testAPI函数并获取结果

        result = testAPI(["D:\\data\\MNIST\\test\\4\\4.png"])
        result_softmax = result[0]
        expected_softmax = np.array([[1.1866205e-04, 7.1287897e-05, 2.0312506e-04, 1.8049637e-05,
       9.5055664e-01, 1.3217170e-04, 6.0152105e-04, 3.6658652e-02,
       2.4324974e-05, 1.1615527e-02]])
        # 使用numpy的allclose方法检查两个数组是否近似相等
        self.assertTrue(np.allclose(result_softmax, expected_softmax, atol=1e-6),
                        "Softmax output does not match the expected result.")

#if __name__ == '__main__':
#    test_testAPI()
