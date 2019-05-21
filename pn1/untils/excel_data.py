import token
class ExcelVariable:
    caseID=0
    url=2
    request_data=3
    expect=4
    result=5
def getCaseID():
    return ExcelVariable.caseID
def getUrl():
    return ExcelVariable.url
def get_request_data():
    return ExcelVariable.request_data
def getExpect():
    return ExcelVariable.expect
def getResult():
    return ExcelVariable.result
def getHeadersValue():
    '''获取请求头'''
    headers={"Authorization":"Basic dmJ1eS1tYWxsOnZidXktbWFsbA=="
             }
    return headers


def getHeadersValue1(token):
    '''获取请求头'''
    headers = {"Content-Type":"application/json;charset=UTF-8",
               "Authorization": "Bearer " + token
               }
    return headers

