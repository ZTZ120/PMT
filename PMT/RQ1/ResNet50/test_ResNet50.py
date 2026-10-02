from unittest import TestCase
from ResNet50 import testAPI
import numpy as np

class DemoTest(TestCase):

    def test_testAPI(self):
        """
        测试testAPI函数，验证其返回结果的值是否与期望的值相等。
        """
        # 调用testAPI函数并获取结果
        result = testAPI(["/mnt/c/data/MNIST/test/4/4.png"])
        result_softmax = result[0]
        expected_softmax = np.array([[3.8703394e-08, 1.4033303e-08, 1.3193885e-08, 1.5695765e-08,
       9.9999464e-01, 5.5825626e-07, 8.7030834e-08, 4.1474234e-08,
       3.4720210e-06, 1.0071936e-06]])
        # 使用numpy的allclose方法检查两个数组是否近似相等
        self.assertTrue(np.allclose(result_softmax, expected_softmax, atol=1e-6),
                        "Softmax output does not match the expected result.")

#if __name__ == '__main__':
#    test_testAPI()
