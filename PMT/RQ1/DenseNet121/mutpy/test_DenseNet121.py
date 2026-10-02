from unittest import TestCase
from DenseNet121 import testAPI
import numpy as np

class DemoTest(TestCase):

    def test_testAPI(self):
        """
        测试testAPI函数，验证其返回结果的值是否与期望的值相等。
        """
        # 调用testAPI函数并获取结果

        result = testAPI(["D:\\data\\MNIST\\test\\4\\4.png"])
        result_softmax = result[0]
        expected_softmax = np.array([[4.6233159e-05, 4.8737544e-05, 3.3360473e-05, 3.6371092e-04,
       9.9741226e-01, 1.6956852e-05, 1.5138825e-04, 1.6270239e-04,
       1.6804817e-05, 1.7478412e-03]])
        # 使用numpy的allclose方法检查两个数组是否近似相等
        self.assertTrue(np.allclose(result_softmax, expected_softmax, atol=1e-6),
                        "Softmax output does not match the expected result.")

#if __name__ == '__main__':
#    test_testAPI()
