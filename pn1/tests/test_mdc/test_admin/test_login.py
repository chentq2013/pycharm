import unittest
from base.method import Method,IsContent
from page.admin import *
import json
from untils.operationExcel import OperationExcel

# header = {"Authorization": "token","Content-Type": "application/json;charset=UTF-8"}

class login(unittest.TestCase):
    def setUp(self):
        self.obj = Method()
        self.p = IsContent()
        self.excel = OperationExcel()

    def test_admin_01(self):
        """后台登录接口-01,商城密码登录-02，
           后台grant_type=password，前台grant_type=mall,
           前台登录名要以 PWD@ 开头"""
        r = self.obj.post(data=Login('coco', 111111,grant_type='password',row=1), row=1)
        data = r.json()
        header = {"Authorization": "Bearer "+data["access_token"],
                  "Content-Type": "application/json;charset=UTF-8"}
        tokenfile=writesupplierID(content=header,data='data',filename='token.json')
        print(r.text)







