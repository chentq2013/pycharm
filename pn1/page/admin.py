from untils.operationJson import OperationJson
from  untils.operationExcel import OperationExcel
from untils.public import *
import json
import random
operationJson=OperationJson()
operationExcel=OperationExcel()

def Login(username=None,password=None,grant_type=None,scope=None,row=None):
    '''对用户名重新赋值'''
    dici1=operationJson.getRequestsData(row=row)
    dici1['username']=username
    dici1['password'] = password
    dici1['grant_type'] = grant_type
    dici1['scope'] = scope
    return dici1



def writesupplierID(content,data,filename):
    '''把供应商ID写入文件中'''
    with open(data_dir(data=data,fileName=filename),"w") as f:
        f.write(json.dumps(content))



def getSupplierid(data,fileName):
    '''读取供应商ID'''
    with open(data_dir(data=data, fileName=fileName), 'r') as f:
         return f.read()



def soSupplierid(data,fileName):
    '''对读取的供应商id进行处理'''
    list1= getSupplierid(data=data, fileName=fileName).split(',')
    a=str(list1)
    f=a.replace('\"','').replace("\'",'').replace(' ','').replace('[','').replace(']','')
    list=f.split(",")
    return list


def updateTime(id=None,cycleType=None,updateCycle=None,row=None):
    '''修改供应商临时周期'''
    dici1 = operationJson.getRequestsData(row=row)
    dici1['cycleType']=cycleType
    dici1['id'] = id
    dici1['updateCycle'] =updateCycle
    a = json.dumps(dici1)
    return a

def distributeSu(operatingId=None,list=None,row=None):
    '''分配供应商'''
    dici1 = operationJson.getRequestsData(row=row)
    dici1['operatingId'] = operatingId
    dici1['list']=list
    a=json.dumps(dici1)
    return a



def Logs(content=None,logType=None,overstockId=None,row=None):
    '''新增日志---动态参数传值'''
    dici1 = operationJson.getRequestsData(row=row)
    dici1['content']=content
    dici1['logType'] = logType
    dici1['overstockId'] = overstockId
    return dici1


def add_supplier(phone=None,id=None,row=None):
    '''添加供应商必填参数'''
    dici1 = operationJson.getRequestsData(row=row)
    dici1['phone'] = phone
    dici1['id']=id
    # dici1['name'] = name
    a=json.dumps(dici1)
    return a



def geturl(id=None,row=None):
    '''获取带id的 url'''
    urlInfo=operationExcel.getUrl(row=row)
    userInfo=urlInfo + str(id)
    return userInfo


def partList(id =None,partsIds=None,row=None):
    '''删除选中物料'''
    M=geturl(id=id,row=row)+'/'+ str(partsIds).replace('[','').replace(']','').replace(' ','')
    return M
p=partList(id=30,partsIds=[10,20,30],row=17)
print(p)



def category(name=None,parentId=None,sort=None,id=None,status=None,row=None):
    '''分类接口'''
    dicil=operationJson.getRequestsData(row=row)
    dicil['name']=name
    dicil['parentId']=parentId
    dicil['sort'] = sort
    dicil['id'] = id
    dicil['status'] = status
    a=json.dumps(dicil)
    return a


def detail(page=None,pageSize=None,isRfq=None,key=None,row=None):
    '''列表方法定义'''
    dicil=operationJson.getRequestsData(row=row)
    dicil['page']=page
    dicil['pageSize '] = pageSize
    dicil['isRfq '] = isRfq
    dicil['key '] = key
    return dicil


def upfile(evaluationFile=None,name=None):
    pass

def evaOverstock(address=None,delivery=None,
                 premium=None,evaluateId=None,
                 factoryId=None,invType=None,
                 name=None,row=None,
                 isRfq=None,id=None):
    """上传和生成呆料单新增呆料单"""

    dicil = operationJson.getRequestsData(row=row)
    dicil['address'] = address
    dicil['delivery'] = delivery
    dicil['evaluateId'] = evaluateId
    dicil['factoryId'] = factoryId
    dicil['invType'] = invType
    dicil['name'] = name
    dicil['premium'] = premium
    dicil['isRfq']=isRfq
    dicil['id'] = id
    a=json.dumps(dicil)

    return a



def overStockpart(partsId=None,updatePrice=None,row=None):
    dicil = operationJson.getRequestsData(row=row)
    dicil['partsId']=partsId
    dicil['updatePrice']=updatePrice
    a=json.dumps(dicil)
    return a

def markId(id=None,status=None,row=None):
    dicil = operationJson.getRequestsData(row=row)
    dicil['id']=id
    dicil['status']=status
    a=json.dumps(dicil)
    print(type(a))
    return a

def overOrder(customerId=None,entityId=None,row=None):
    '''预览生成订单'''
    dicil = operationJson.getRequestsData(row=row)
    dicil[0]['customerId'] = customerId
    dicil[0]['entityId'] = entityId
    a=json.dumps(dicil)
    return a


def partprice(partId=None,row=None):
    '''修改原表'''
    dicil = operationJson.getRequestsData(row=row)
    dicil[0]['partId']= partId
    return dicil

def factorySO(keyword=None,row=None):
    dicil = operationJson.getRequestsData(row=row)
    dicil['keyword']=keyword
    return dicil


def overStatus(id=None,status=None,row=None):
    dicil = operationJson.getRequestsData(row=row)
    dicil['id'] = id
    dicil['status'] = status
    a=json.dumps(dicil)
    return a

def brand(linkIds=None,name=None,shortName=None,id=None,row=None):
    '''品牌列表'''
    dicil = operationJson.getRequestsData(row=row)
    dicil['linkIds'] = linkIds
    dicil['name'] = name
    dicil['shortName'] = shortName
    dicil['id'] = id
    a=json.dumps(dicil)
    return a

def customerAdd(company=None,name=None,phone=None,id=None,row=None):
    '''客户信息'''
    dicil = operationJson.getRequestsData(row=row)
    dicil['company'] = company
    dicil['name'] = name
    dicil['phone'] = phone
    dicil['id'] = id
    a=json.dumps(dicil)
    return a




def orderover(cycleType=None,endTime=None,startTime=None,type =None,row=None):
    '''数据中心'''
    dicil = operationJson.getRequestsData(row=row)
    dicil['cycleType'] = cycleType
    dicil['endTime'] = endTime
    dicil['startTime'] = startTime
    dicil['type'] = type
    return dicil

def dict(kvList=None,flagType=None,flagName=None,row=None):
    '''数据字典接口'''
    dicil = operationJson.getRequestsData(row=row)
    dicil['flagName'] = flagName
    dicil['flagType'] = flagType
    dicil['kvList'] = kvList

    return dicil


def dictValue(dictValue=None,id=None,row=None):
    '''数据字典接口'''
    dicil = operationJson.getRequestsData(row=row)
    dicil['dictValue'] = dictValue
    dicil['id'] = id
    a=json.dumps(dicil)
    return a


def friend(link=None,materialFile=None,name=None,sort=None,attachmentId=None,id=None,type=None,row=None):
    '''合作伙伴'''
    dicil = operationJson.getRequestsData(row=row)
    dicil['link'] = link
    dicil['materialFile'] = materialFile
    dicil['name'] = name
    dicil['sort'] = sort
    dicil['attachmentId'] = attachmentId
    dicil['id'] = id
    dicil['type'] = type
    a = json.dumps(dicil)
    return a

def News(content='',id=None,source=None,title=None,row=None):
    '''添加新闻'''
    dicil = operationJson.getRequestsData(row=row)
    dicil['id'] = id
    dicil['source'] = source
    dicil['content'] = content
    dicil['title'] = title
    a = json.dumps(dicil)
    return a


def feedbackType(type=None,row=None):
    '''添加新闻'''
    dicil = operationJson.getRequestsData(row=row)
    dicil['type'] = type
    a = json.dumps(dicil)
    return a

def offer(inquiryId=None,message=None,offer=None,phone=None,row=None):
    '''添加新闻'''
    dicil = operationJson.getRequestsData(row=row)
    dicil['inquiryId'] = inquiryId
    dicil['message'] = message
    dicil['offer'] = offer
    dicil['phone'] = phone
    a = json.dumps(dicil)
    return a


