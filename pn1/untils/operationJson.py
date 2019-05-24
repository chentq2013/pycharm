from untils.public import *
import json
from untils.operationExcel import OperationExcel

class OperationJson:
    def __init__(self):
        self.excel=OperationExcel()
    def getReadJson(self):
        '''读取json内容'''
        with open(data_dir(data='data',fileName='requestData.json'),'rb') as fp:
            data=json.load(fp)
            return data
    def getRequestsData(self,row):
        '''读取请求参数'''
        return self.getReadJson()[self.excel.get_request_data(row=row)]

opera=OperationJson()
a=opera.getRequestsData(5)

