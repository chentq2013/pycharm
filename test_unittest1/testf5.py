import unittest
from selenium import webdriver

option=webdriver.ChromeOptions()
option.add_argument('disable-infobars')
class f5(unittest.TestCase):
    def test_user_001(self):
        '''添加用户'''
        print('del')
    def test_user_002(self):
        '''删除用户'''
        print('add')






if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(f5)
    unittest.TextTestRunner(verbosity=2).run(suite)



