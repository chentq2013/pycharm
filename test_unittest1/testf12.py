import unittest
from init import Init

#测试用例断言
class baidulink(Init):

    def test_baidu_news(self):
        try:
            self.assertEqual(self.driver.title, '百度一下你就知道')
            print(self.driver.title)
        except Exception as e:
            print("fail info{0}".format(e.args))

    # @unittest.skip
    # def test_baidu_login(self):
    #     so=self.driver.find_element_by_id('kw')
    #     self.assertTrue(so.is_enabled())
    #
    #
    # def test_baidu_title(self):
    #     self.assertIn('百度',self.driver.title)
    #     print(self.driver.title)


if __name__ == '__main__':
    unittest.main(verbosity=2)
