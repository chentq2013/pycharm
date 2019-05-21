from untils.operationJson import OperationJson
import json
operationJson=OperationJson()
def Login(username=None,password=None):
    '''对用户名重新赋值'''
    dici1=operationJson.getRequestsData(1)
    dici1['username']=username
    dici1['password'] = password
    return dici1





