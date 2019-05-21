import unittest
from selenium import webdriver

class baiduso(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.driver.get('http://www.baidu.com')
    def tearDown(self):
        self.driver.quit()

    def test_baidu_news(self):
        self.driver.find_element_by_id('kw').send_keys('selenium')
    def test_baidu_map(self):
        self.driver.find_element_by_id('su').click()

    #静态方法
    @staticmethod
    def suite():
        suite = unittest.TestLoader().loadTestsFromModule('test-f8.py')  # py模块测试用例执行
        print('测试套件',suite)
        return suite

if __name__ == '__main__':

   unittest.TextTestRunner(verbosity=2).run(baiduso.suite())
