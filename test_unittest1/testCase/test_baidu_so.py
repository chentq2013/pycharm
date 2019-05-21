from selenium import webdriver
import unittest

class baidulink(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.driver.get("http://www.baidu.com")


    def tearDown(self):
        self.driver.quit()



    def test_baiduso_enabled(self):
        '''百度搜索框元素是否存在'''

        so=self.driver.find_element_by_id('kw')

        self.assertTrue(so.is_enabled())
    def test_baiduso(self):
        '''测试百度搜索结果页'''
        so=self.driver.find_element_by_id('kw')
        so.send_keys('selenium')
        self.driver.find_element_by_id('su').click()
        self.assertEqual(so.get_attribute('value'),'webdirver')


if __name__ == '__main__':
    unittest.main(verbosity=2)
