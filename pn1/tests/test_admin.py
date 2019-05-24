import unittest
from base.method import Method,IsContent
from page.admin import *
import json
from untils.operationExcel import OperationExcel


class Admin(unittest.TestCase):
    def setUp(self):
        self.obj=Method()
        self.p=IsContent()
        self.excel=OperationExcel()


    def statusCode(self,r):
        """断言协议状态码和JSON 文件的关键字"""
        self.assertEqual(r.status_code,200)
        self.assertEqual(r.json()['code'],1)

    def isContent(self,r,row):
        '''断言业务状态码和参数预期结果是否一致'''
        self.statusCode(r=r)
        self.assertTrue(self.p.isContent(row=row, str2=r.text))


    def test_admin_001(self):
        """登录接口"""
        r = self.obj.post(data=Login('admin',123456),row=1)
        data=r.json()
        with open("../data/token.json", "w") as f:
            header = {'Authorization': 'Bearer ' + data['access_token'],
                      "Content-Type": "application/json;charset=UTF-8"}
            json.dump(header,f)
        # print(r.text)


    def test_admin_002(self):
        """供应商信息搜索接口,并将id写入到supplierid文件中"""
        r = self.obj.get(row=2)
        # print(r.text)
        self.assertTrue(self.p.isContent(str2=r.text, row=3))
        for i in range(0, 1):
            supplierid = r.json()['data']['records'][i]['id']
            writesupplierID(supplierid)
        self.isContent(r=r, row=2)
        self.excel.writeResult(row=2,content='pass')


    def test_admin_003(self):
        """新增日志"""
        r = self.obj.post(data=json.dumps(Logs(content='自动化测试用例', logType='QR', overstockId=128,row=3)),row=3)
        # print(r.text)
        self.isContent(r=r, row=3)
        self.excel.writeResult(row=3,content='pass')

    @unittest.skip('pass')
    def test_admin_004(self):
        '''删除供应商接口'''
        r=self.obj.delete(url=geturl(supplierid=getSupplierid()),row=4)
        # print(r.text)
        self.assertTrue(self.p.isContent(row=4,str2=r.text))
        self.excel.writeResult(row=4, content='pass')

    def test_admin_005(self):
        '''添加供应商信息'''
        r=self.obj.post(data=add_supplier(phone=15618824736,row=5),row=5)
        return r
        # print(r.text)






if __name__ == '__main__':
    unittest.main(verbosity=2)







