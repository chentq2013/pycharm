import unittest
from base.method import Method,IsContent
from page.admin import *
import json


token=None
class Admin(unittest.TestCase):
    def setUp(self):
        self.obj=Method()
        self.p=IsContent()


    def statusCode(self,r):
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["token_type"],"bearer")

    def isContent(self,r,row):
        self.statusCode(r=r)
        self.assertTrue(self.p.isContent(row=row, str2=r.text))

    # def test_admin_001(self):
    #
    #     '''admin登录'''
    #     r=self.obj.post_01(row=1)
    #     self.isContent(r=r,row=1)
    #     print(r.text)

    def test_admin_002(self):
        """登录接口"""
        r = self.obj.post(data=Login('cici',123456),row=1)
        data=json.loads(r.text)
        global token
        token=data['access_token']
        print(token)

    def test_admin_003(self):
        """接口"""
        r = self.obj.post_01(row=2)
        print(r.text)
        print(token)





if __name__ == '__main__':
    unittest.main(verbosity=2)







