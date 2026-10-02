from unittest import TestCase
from EfficientNet import testAPI
import numpy as np

class DemoTest(TestCase):

    def test_testAPI(self):
        """
        测试testAPI函数，验证其返回结果的值是否与期望的值相等。
        """
        # 调用testAPI函数并获取结果

        result = testAPI(["D:\\data\\MNIST\\test\\4\\4.png"])
        result_softmax = result[0]
        expected_softmax = np.array([[1.7370534e-04, 3.4997737e-04, 6.1617669e-04, 5.5388664e-05,
       9.6557647e-01, 1.3482699e-03, 6.4487034e-04, 3.2824553e-03,
       2.9534832e-04, 2.7657270e-02]])
        # 使用numpy的allclose方法检查两个数组是否近似相等
        self.assertTrue(np.allclose(result_softmax, expected_softmax, atol=1e-6),
                        "Softmax output does not match the expected result.")

#if __name__ == '__main__':
#    test_testAPI()
