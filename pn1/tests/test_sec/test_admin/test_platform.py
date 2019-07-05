

import unittest
from base.method import Method,IsContent
from page.admin import *
import json
from untils.operationExcel import OperationExcel

def test_admin_002(self):
    """供应商信息搜索接口,并将id写入到supplierid文件中"""
    r = self.obj.get(params=detail(page=1 ,pageSize=50 ,row=2 ) ,row=2)
    print(r.text)
    supplierid =''
    for i in range(0 ,50):
        supplierid =  str(r.json()['data']['records'][i]['id'] ) +', ' +supplierid
    writesupplierID(supplierid)
    self.assertTrue(self.p.isContent(str2=r.text, row=2))
    self.isContent(r=r, row=2)
    self.excel.writeResult(row=2 ,content='pass')



def test_admin_004(self):
        '''删除供应商接口'''
        # list=getSupplierid().split(",")
        # supplierid=list[2]
        r=self.obj.delete(url=geturl(row=4,id=soSupplierid()),row=4)
        print('supplierid:', soSupplierid())
        print(r.text)
        self.assertTrue(self.p.isContent(row=4,str2=r.text))
        self.excel.writeResult(row=4, content='pass')

