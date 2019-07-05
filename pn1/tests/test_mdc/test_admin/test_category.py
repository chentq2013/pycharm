import unittest
from page.admin import *
from tests.test_mdc.test_admin.init import *

'''类目相关的接口'''


class CateGory(Init,unittest.TestCase):



    def test_admin_10(self):
        '''类目列表'''
        r = self.obj.get(row=10)
        print(r.text)

    def test_admin_11(self):
        '''类目保存'''
        r = self.obj.post(category(name='test-005', parentId=5, sort=100, row=11), row=11)
        print(r.text)

    def test_admin_12(self):
        '''类目修改'''
        r = self.obj.put(category(name='test-3', parentId=0, sort=1, id=2, status='Y', row=11), row=11)
        print(r.text)





if __name__ == '__main__':
    unittest.main(verbosity=2)