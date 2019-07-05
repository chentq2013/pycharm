import json
import requests
from untils.operationExcel import OperationExcel
from untils.operationJson import OperationJson
from untils.excel_data import *
from page.admin import *




class Method:
    def __init__(self):
        self.operationJson = OperationJson()
        self.excel = OperationExcel()

    def post(self,data,url=None,row=None):
        '''post请求'''
        if data and url !=None:
            r = requests.post(url=url,
                              data=data,
                              headers=getHeadersToken(row=row),
                              timeout=6
                              )
            return r

        elif data==None:
            r = requests.post(url=url,
                              headers=getHeadersToken(row=row),
                              timeout=6
                              )
            return r

        elif data!=None:
            r=requests.post(url=self.excel.getUrl(row=row),
                              data=data,
                              headers=getHeadersToken(row=row),
                              timeout=6
                              )
            return r




    def get(self,params=None,url=None,row=None):
        if params==None and url==None:
            '''直接调用excel中的url'''
            r = requests.get(url=self.excel.getUrl(row=row),
                             headers=getHeadersToken(row=row),
                             timeout=6)

            return r
        elif params!=None:
            '''接口带json文件的参数'''
            r = requests.get(url=self.excel.getUrl(row=row),
                             params=params,
                             headers=getHeadersToken(row=row),
                             timeout=6)
            return r
        elif params==None:
            '''接口后面跟id,调用自定义的方法'''
            r = requests.get(url=url,
                             headers=getHeadersToken(row=row),
                             timeout=6)
            return r





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
    def put(self,data=None,url=None,row=None):
        '''put请求'''
        if data == None:
            r = requests.put(url=url,
                             headers=getHeadersToken(row=row),
                             timeout=6
                             )
            return r
        else:
            r = requests.put(url=self.excel.getUrl(row=row),
                             data=data,
                             headers=getHeadersToken(row=row),
                             timeout=6
                             )
            return r



    def patch(self,data=None,url=None,row=None):
        # if data and url != None:
        #     r = requests.post(url=url,
        #                       data=data,
        #                       headers=getHeadersToken(row=row),
        #                       timeout=6
        #                       )
        #     return r

        if data==None:
            r = requests.patch(url=url,
                               headers=getHeadersToken(row=row),
                               timeout=6)
            return r
        else:
            r = requests.patch(url=self.excel.getUrl(row=row),
                               data=data,
                               headers=getHeadersToken(row=row),
                               timeout=6)
            return r




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



