import unittest
class f1(unittest.TestCase):

    def setUp(self):
        print("我已经准备好了")

    def tearDown(self):
        print("测试结束了")

    def test_001(self):
        admin
        print("已处理")

    def test_002(self):
        print('test')

    def test_003(self):
        print('test003')
        self.assertEqual(1,'1')

if __name__ == '__main__':
    unittest.main(verbosity=2)