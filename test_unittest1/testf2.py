import unittest
from selenium import webdriver
'''setup和setupclass,teardown和teardownclass区别
1.setupclass,只打开一次浏览器。但是得配合driver .back和@classmethod使用
'''
class f3(unittest.TestCase):
    # @classmethod
    # def setUpClass(cls):
    #     cls.driver=webdriver.Chrome()
    #     cls.driver.maximize_window()
    #     cls.driver.implicitly_wait(30)
    #     cls.driver.get('http://www.baidu.com')
    #     print("已上线")
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.driver.get('http://www.baidu.com')
        print("已上线")




    # @classmethod
    # def tearDownClass(cls):
    #     cls.driver.quit()
    #     print('已退出')
    def tearDown(self):
        self.driver.quit()
        print('已退出')


    def test_baidu_news(self):
        self.driver.find_element_by_link_text('新闻').click()
        self.driver.back()

    def test_baidu_map(self):
        self.driver.find_element_by_link_text('地图').click()
        self.driver.back()



if __name__ == '__main__':
    unittest.main(verbosity=2)