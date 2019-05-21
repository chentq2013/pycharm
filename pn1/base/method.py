import json
import requests
from untils.operationExcel import OperationExcel
from untils.operationJson import OperationJson
from untils.excel_data import *

token=None

class Method:
    def __init__(self):
        self.operationJson = OperationJson()
        self.excel = OperationExcel()

    def post_01(self,row):
        """其他接口专用"""
        try:
            r=requests.post(url=self.excel.getUrl(row=row),
                            data=self.operationJson.getRequestsData(row=row),
                            headers={
                                 "Content-Type":"application/json;charset=UTF-8",
                                 "Authorization": "Bearer " + token
                            },
                            timeout=6)
            return r
        except Exception as e:
            print(e)
            raise RuntimeError('接口发生未知错误')


    def post(self,data,row):
        """登录接口专用"""
        try:
            r = requests.post(url=self.excel.getUrl(row=row),
                              data=data,
                              headers=getHeadersValue(),
                              timeout=6
                              )

            data = json.loads(r.text)
            global token
            token = data['access_token']
            return r

        except Exception as e:
            print(e)
            raise RuntimeError('接口发生未知错误')



class IsContent():
    def __init__(self):
        self.excel=OperationExcel()
    def isContent(self,row,str2):
        flag = None
        if self.excel.getExpect(row=row) in str2:
            flag = True
        else:
            flag = False
        return flag


