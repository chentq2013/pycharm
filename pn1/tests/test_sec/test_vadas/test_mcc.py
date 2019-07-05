import unittest
from base.method import Method,IsContent
from page.admin import *
import json
from untils.operationExcel import OperationExcel

class McC(unittest.TestCase):
    def setUp(self):
        self.obj = Method()
        self.p = IsContent()
        self.excel = OperationExcel()

    def test_01(self):
        '''MCC物料列表'''
        print(self)
        r =self.obj.get(params=detail(page=1,pageSize=100,row=110),row=110)
        print(r.text)




if __name__ == '__main__':
    unittest.main(verbosity=2)