from unittest import TestCase
from MobileNet import testAPI
import numpy as np

class DemoTest(TestCase):

    def test_testAPI(self):
        """
        测试testAPI函数，验证其返回结果的值是否与期望的值相等。
        """
        # 调用testAPI函数并获取结果
        result = testAPI(["/mnt/c/data/MNIST/test/4/4.png"])
        result_softmax = result[0]
        expected_softmax = np.array([[1.1652440e-04, 7.2019495e-05, 2.0351620e-04, 1.8072222e-05,
       9.5042533e-01, 1.3195537e-04, 6.0217251e-04, 3.6874305e-02,
       2.4157856e-05, 1.1531985e-02]])
        # 使用numpy的allclose方法检查两个数组是否近似相等
        self.assertTrue(np.allclose(result_softmax, expected_softmax, atol=1e-6),
                        "Softmax output does not match the expected result.")

#if __name__ == '__main__':
#    test_testAPI()
