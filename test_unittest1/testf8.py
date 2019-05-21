import unittest
from selenium import webdriver

class baidulink(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.driver.get('http://www.baidu.com')
    def tearDown(self):
        self.driver.quit()

    def test_baidu_news(self):
        self.driver.find_element_by_link_text('新闻').click()
    def test_baidu_map(self):
        self.driver.find_element_by_link_text('地图').click()


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

if __name__ == '__main__':
   suite=unittest.TestLoader().loadTestsFromModule('test-f8.py')#执行py文件全部测试用例
   unittest.TextTestRunner(verbosity=2).run(suite)
