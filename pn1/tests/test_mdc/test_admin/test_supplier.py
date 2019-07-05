import unittest
from page.admin import *
from tests.test_mdc.test_admin.init import Init

'''供应商相关的接口'''

ids= soSupplierid(fileName='suppierId', data='data')
id=ids[0]
class SuppLier(Init,unittest.TestCase):

    def test_admin_03(self):
        """供应商信息搜索接口,并将id写入到supplierid文件中"""
        r = self.obj.get(params=detail(page=1, pageSize=50, row=3), row=3)
        supplierid = ''
        for i in range(0, 50):
            supplierid = str(r.json()['data']['records'][i]['id']) + ', ' + supplierid
        writesupplierID(content=supplierid,data='data',filename='suppierId')
        print(r.text)
        # self.assertTrue(self.p.isContent(str2=r.text, row=3))
        # self.isContent(r=r, row=2)
        # self.excel.writeResult(row=2, content='pass')

    def test_admin_04(self):
        '''删除供应商接口'''
        # supplierid=soSupplierid(fileName='suppierId',data='data')
        r = self.obj.delete(url=geturl(row=4, id=id), row=4)
        print('supplierid:', id)
        print(r.text)
        self.assertTrue(self.p.isContent(row=4, str2=r.text))
        self.excel.writeResult(row=4, content='pass')

    def test_admin_05(self):
        '''添加供应商信息'''
        r = self.obj.post(data=add_supplier(phone=15616624461, row=5), row=5)
        print(r.text)


    def test_admin_06(self):
        '''修改供应商信息'''
        # id = soSupplierid(fileName='suppierId', data='data')
        r = self.obj.put(add_supplier(id=id, phone=18199999989,row=6), row=6)
        print(r.text)


    def test_admin_07(self):
        '''修改供应商临时周期'''
        r = self.obj.put(updateTime(id=id, cycleType='MONTH', updateCycle=10, row=7), row=7)
        print(r.text)


    def test_admin_08(self):
        '''分配'''

        r = self.obj.post(distributeSu(operatingId=14, list=ids[0:8], row=8), row=8)
        print(r.text)


    def test_admin_09(self):
        '''更新供应商的呆料'''
        r = self.obj.put(url=geturl(id=id, row=9), row=9)
        print(r.text)


if __name__ == '__main__':
    unittest.main(verbosity=2)