import unittest
from selenium import webdriver
from time import sleep
option=webdriver.ChromeOptions()
option.add_argument('disable-infobars')
class f6(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(options=option)
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(30)
        cls.driver.get('http://www.baidu.com')
        print("已上线")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print('已退出')


    def test_001(self):
        '''百度首页连接测试，验证新闻'''
        self.driver.find_element_by_link_text('新闻').click()
        self.driver.back()


    def test_002(self):
        '''百度首页连接测试，验证地图'''
        self.driver.find_element_by_link_text('地图').click()
        self.driver.back()

    def test_003(self):
        '''百度首页连接测试，验证关键字'''

        self.driver.find_element_by_id('kw').send_keys('赵志权')

        self.driver.find_element_by_id('su').click()
        sleep(2)
        self.driver.back()




if __name__ == '__main__':
    suite=unittest.TestSuite()
    suite.addTest(f6('test_003'))
    suite.addTest(f6('test_001'))
    suite.addTest(f6('test_002'))
