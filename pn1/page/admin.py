from untils.operationJson import OperationJson
from  untils.operationExcel import OperationExcel
from untils.public import *
import json

operationJson=OperationJson()
operationExcel=OperationExcel()

def Login(username=None,password=None):
    '''对用户名重新赋值'''
    dici1=operationJson.getRequestsData(row=1)
    dici1['username']=username
    dici1['password'] = password
    return dici1


def writesupplierID(content):
    '''把供应商ID写入文件中'''
    with open(data_dir(data='data',fileName='supplierID'),"w") as f:
        f.write(str(content))




def getSupplierid():
    '''读取供应商ID'''
    with open(data_dir(data='data', fileName='supplierID'), 'r') as f:
        return f.read()



def Logs(content=None,logType=None,overstockId=None,row=None):
    '''新增日志---动态参数传值'''
    dici1 = operationJson.getRequestsData(row=row)
    dici1['content']=content
    dici1['logType'] = logType
    dici1['overstockId'] = overstockId
    return dici1


def add_supplier(phone=None,row=None):
    dici1 = operationJson.getRequestsData(row=row)
    dici1['phone'] = phone
    a=json.dumps(dici1)
    return a



def geturl(supplierid):
    '''获取url'''
    # urlInfo=operationExcel.getUrl(row=4)
    userInfo="http://192.168.1.251:9999/mdc/admin/supplier/"+str(supplierid)
    return userInfo


