from base.method import Method,IsContent

from untils.operationExcel import OperationExcel




class Init():
    def setUp(self):
        self.obj = Method()
        self.p = IsContent()
        self.excel = OperationExcel()

    def statusCode(self, r):
        """断言协议状态码和JSON 文件的关键字"""
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], 1)

    def isContent(self, r, row):
        '''断言业务状态码和参数预期结果是否一致'''
        self.statusCode(r=r)
        self.assertTrue(self.p.isContent(row=row, str2=r.text))

