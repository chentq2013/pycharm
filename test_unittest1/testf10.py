import unittest

from init import Init
class baidulink(Init):

    def test_baidu_news(self):
        self.driver.find_element_by_link_text('新闻').click()
    def test_baidu_map(self):
        self.driver.find_element_by_link_text('地图').click()


    # 静态方法
    @staticmethod
    def suite():
        suite = unittest.TestSuite(unittest.makeSuite(baidulink))
        return suite


if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(baidulink.suite())



