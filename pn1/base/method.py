import json
import requests
from untils.operationExcel import OperationExcel
from untils.operationJson import OperationJson
from untils.excel_data import *
from page.admin import *
operationExcel=OperationExcel()


class Method:
    def __init__(self):
        self.operationJson = OperationJson()
        self.excel = OperationExcel()

    def post(self,data,row):
        '''post请求'''
        try:
            r = requests.post(url=self.excel.getUrl(row=row),
                              data=data,
                              headers=getHeadersToken(row=row),
                              timeout=6
                              )
            return r

        except Exception as e:
            print(e)
            raise RuntimeError('接口发生未知错误')


    def get(self,row):
        """get接口专用"""
        try:
            r=requests.get(url=self.excel.getUrl(row=row),
                            params=self.operationJson.getRequestsData(row=row),
                            headers=getHeadersToken(row=row),
                            timeout=6)
            return r
        except Exception as e:
            print(e)
            raise RuntimeError('接口发生未知错误')

    def delete(self,url,row):
        """delete接口专用"""
        try:
            r = requests.delete(url=url,
                             headers=getHeadersToken(row=row),
                             timeout=6)
            return r
        except Exception as e:
            print(e)
            raise RuntimeError('接口发生未知错误')


class IsContent():
    def __init__(self):
        self.excel=OperationExcel()
    def isContent(self,row,str2):
        flag=None
        if self.excel.getExpect(row=row) in str2:
            flag = True
        else:
            flag = False
        return flag





