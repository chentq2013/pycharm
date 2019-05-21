import unittest
from init import Init

#跳过测试用例执行 ：@unittest.skip()
class baidulink(Init):
    @unittest.skip('该功能已经取消，请忽略')
    def test_baidu_news(self):
        self.driver.find_element_by_link_text('新闻').click()
    def test_baidu_map(self):
        self.driver.find_element_by_link_text('地图').click()


if __name__ == '__main__':
    unittest.main(verbosity=2)



