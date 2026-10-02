from unittest import TestCase
from demo import testAPI
import numpy as np

class DemoTest(TestCase):

    # def testthree_mut(self):
    #
    #     # self.assertEqual(testthreeAPI("E:/Program Files/PyCharm Community Edition 2020.1.1/projects/CNN/train/","E:/Program Files/PyCharm Community Edition 2020.1.1/projects/CNN/test/",0), 1)
    #     self.assertEqual(testAPI(["F:/program/ImageProbability/code/python/testCNN/image/test/0/101000.png"]),([[0.06923394,0.30828208,0.5230204,0.06048951,0.03897413]],[[-2.6702642,-1.1767402,-0.6481349,-2.8052855,-3.2448573]]))
    def test_testAPI(self):
        """
        测试testAPI函数，验证其返回结果的值是否与期望的值相等。
        """
        # 调用testAPI函数并获取结果

        result_softmax, result_log_softmax = testAPI(['/mnt/c/image/test/2/170072.png'])
        expected_softmax = np.array([[0.00494512, 0.0027433 , 0.98493576, 0.00364801, 0.00372775]])
        expected_log_softmax = np.array([[-5.3093534 , -5.898594  , -0.01517889, -5.6135745 , -5.5919495 ]])
        # 使用numpy的allclose方法检查两个数组是否近似相等
        self.assertTrue(np.allclose(result_softmax, expected_softmax, atol=1e-6),
                        "Softmax output does not match the expected result.")

        self.assertTrue(np.allclose(result_log_softmax, expected_log_softmax, atol=1e-6),
                        "Log Softmax output does not match the expected result.")

# if __name__ == '__main__':
#     test_testAPI()

