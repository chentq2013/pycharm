
from urllib import parse
import hashlib

def dataSign(secure="nana",*args,**kwargs):
    dict1=dict(sorted(kwargs.items(),key=lambda item:item[0]))
    str2=parse.urlencode(dict1)+secure
    m2=hashlib.md5()
    m2.update(str2.encode('utf-8'))
    return m2.hexdigest()

    print(str2)

dict2={"a":"a","c":"c","b":"b","name":"coco","age":13}
print(dataSign(**dict2))
