import unittest
from base.method import Method,IsContent
from page.admin import *
import json
from untils.operationExcel import OperationExcel


def test_admin_003(self):
    """新增日志"""
    r = self.obj.post(data=json.dumps(Logs(content='自动化测试用例', logType='QR', overstockId=120 ,row=3)) ,row=3)
    print(r.text)
    self.isContent(r=r, row=3)
    self.excel.writeResult(row=3 ,content='pass')