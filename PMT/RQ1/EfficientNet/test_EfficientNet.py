from unittest import TestCase
from EfficientNet import testAPI
import numpy as np

class DemoTest(TestCase):

    def test_testAPI(self):
        """
        测试testAPI函数，验证其返回结果的值是否与期望的值相等。
        """
        # 调用testAPI函数并获取结果

        result = testAPI(["/mnt/c/data/MNIST/test/4/4.png"])
        result_softmax = result[0]
        expected_softmax = np.array([[1.7461275e-04, 3.5015377e-04, 6.1660691e-04, 5.5469620e-05,
       9.6555203e-01, 1.3481149e-03, 6.4515229e-04, 3.2899580e-03,
       2.9486776e-04, 2.7673008e-02]])
        # 使用numpy的allclose方法检查两个数组是否近似相等
        self.assertTrue(np.allclose(result_softmax, expected_softmax, atol=1e-6),
                        "Softmax output does not match the expected result.")

#if __name__ == '__main__':
#    test_testAPI()
