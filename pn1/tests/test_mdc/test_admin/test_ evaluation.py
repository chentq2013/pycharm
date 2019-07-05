import unittest
from tests.test_mdc.test_admin.init import Init
from page.admin import *
import json

'''估价相关的接口'''
ids= soSupplierid(fileName='suppierId', data='data')
id=ids[0]

class OverStock(Init,unittest.TestCase):


    def test_admin_13(self):
        '''估价单列表'''
        r = self.obj.get(params=detail(page=1, pageSize=40, row=72), row=13)
        print(r.text)
        evaluationid = ''
        for i in range(0,30):
            evaluationid = str(r.json()['data']['records'][i]['id']) + ',' + evaluationid
        writesupplierID(content=evaluationid,data='data',filename='overstockId')


    def test_admin_14(self): pass

        # '''新增估价单'''

    def test_admin_15(self):
        '''估价单详情'''
        print(id)
        r = self.obj.get(url=geturl(id=6, row=15), row=15)
        print(r.text)


    # def test_admin_16(self):
    #     '''删除估价单'''
    #     r = self.obj.delete(geturl(id=id, row=16), row=16)
    #     print(r.text)


    def test_admin_17(self):
        '''确认估价'''
        r = self.obj.patch(url=geturl(id=30, row=17), row=17)
        print(r.text)

    # @unittest.skip('pass')
    def test_admin_18(self):
        '''重新爬取'''
        r = self.obj.get(url=geturl(id=id, row=18), row=18)
        print(r.text)

    # @unittest.skip('pass')
    def test_admin_19(self):
        '''下载估价单'''
        r = self.obj.get(url=geturl(id=id, row=19), row=19)
        print(r.text)


    def test_admin_20(self):
        '''上传指导价'''
        pass


    def test_admin_21(self):
        '''生成呆料单'''
        r = self.obj.post(
            data=evaOverstock(address='南京', delivery="CN", evaluateId=54, factoryId=31, invType='TL', name='测试',
                              premium='2.3', isRfq='Y', row=21), row=21)
        print(r.text)

    def test_admin_22(self):
        '''修正估价价格'''
        r = self.obj.patch(data=overStockpart(partsId=id, updatePrice=1.3, row=22), row=22)
        print(r.text)

    def test_admin_23(self):
        '''删除选中物料'''
        r = self.obj.delete(url=partList(id=39, partsIds=ids[0:8], row=23), row=23)
        print(r.text)

    def test_admin_24(self):
        '''一键删除冷门料'''
        r = self.obj.delete(url=geturl(id=id, row=24), row=24)
        print(r.text)




    def test_admin_16(self):
        '''删除估价单'''
        r = self.obj.delete(geturl(id=id, row=16), row=16)
        print(r.text)







if __name__ == '__main__':
    unittest.main(verbosity=2)