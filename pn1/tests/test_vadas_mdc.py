import unittest
from base.method import Method,IsContent
from page.admin import *
import json
from untils.operationExcel import OperationExcel



class Admin(unittest.TestCase):
    def setUp(self):
        self.obj=Method()
        self.p=IsContent()
        self.excel=OperationExcel()


    def statusCode(self,r):
        """断言协议状态码和JSON 文件的关键字"""
        self.assertEqual(r.status_code,200)
        self.assertEqual(r.json()['code'],1)

    def isContent(self,r,row):
        '''断言业务状态码和参数预期结果是否一致'''
        self.statusCode(r=r)
        self.assertTrue(self.p.isContent(row=row, str2=r.text))

    def test_admin_001(self):
        """登录接口"""
        r = self.obj.post(data=Login('PWD@15618824739',111111,grant_type='mall',row=2),row=2)
        data=r.json()
        with open("../data/token.json", "w") as f:
            header = {'Authorization': 'Bearer ' + data['access_token'],
                      'Content-Type': 'application/json;charset=UTF-8'}
            json.dump(header,f)
        print(r.text)


    def test_admin_002(self):
        """供应商信息搜索接口,并将id写入到supplierid文件中"""
        r = self.obj.get(params=detail(1,50,row=3),row=3)
        print(r.text)
        supplierid=''
        for i in range(0,50):
            supplierid =  str(r.json()['data']['records'][i]['id'])+','+supplierid
        writesupplierID(supplierid)
        self.assertTrue(self.p.isContent(str2=r.text, row=2))
        self.isContent(r=r, row=2)
        self.excel.writeResult(row=2,content='pass')

    # @unittest.skip('pass')
    def test_admin_003(self):
        """新增日志"""
        r = self.obj.post(data=json.dumps(Logs(content='自动化测试用例', logType='QR', overstockId=120,row=3)),row=3)
        print(r.text)
        self.isContent(r=r, row=3)
        self.excel.writeResult(row=3,content='pass')

    # @unittest.skip('pass')
    def test_admin_004(self):
        '''删除供应商接口'''
        # list=getSupplierid().split(",")
        # supplierid=list[2]
        r=self.obj.delete(url=geturl(row=4,id=soSupplierid()),row=4)
        print('supplierid:', soSupplierid())
        print(r.text)
        self.assertTrue(self.p.isContent(row=4,str2=r.text))
        self.excel.writeResult(row=4, content='pass')

    # @unittest.skip('pass')
    def test_admin_005(self):
        '''添加供应商信息'''
        r=self.obj.post(data=add_supplier(phone=15616624736,id=None,row=5),row=5)
        print(r.text)


    def test_admin_006(self):
        '''修改供应商信息'''
        r = self.obj.put(add_supplier(phone=15614597456,id=47,row=6),row=6)
        print(r.text)

    def test_admin_007(self):
        '''修改供应商临时周期'''
        r=self.obj.put(updateTime(id=soSupplierid(),cycleType='MONTH',updateCycle=10,row=7),row=7)
        print(r.text)

    # @unittest.skip('pass')
    def test_admin_008(self):
        '''分配'''
        r=self.obj.post(distributeSu(operatingId=14,list=[40,41,43,45],row=8),row=8)
        print(r.text)

    # @unittest.skip('pass')
    def test_admin_009(self):
        '''更新供应商的呆料'''
        r=self.obj.put(url=geturl(id=62,row=9),row=9)
        print(r.text)

    # @unittest.skip('pass')
    def test_admin_10(self):
        '''类目列表'''
        r=self.obj.get(row=10)
        print(r.text)

    # @unittest.skip('pass')
    def test_admin_11(self):
        '''类目保存'''
        r=self.obj.post(category(name='test-005',parentId=5,sort=1,row=11),row=11)
        print(r.text)

    # @unittest.skip('pass')
    def test_admin_12(self):
        '''类目修改'''
        r = self.obj.put(category(name='test-3', parentId=0, sort=1, id=2, status='Y', row=11), row=11)
        print(r.text)

    # @unittest.skip('pass')
    def test_admin_13(self):
        '''估价单列表'''
        r=self.obj.get(params=detail(page=1,pageSize=10,row=13),row=13)
        print(r.text)
        evaluationid = ''
        for i in range(0,20):
            evaluationid = str(r.json()['data']['records'][i]['id']) + ',' + evaluationid
        writesupplierID(evaluationid)

    @unittest.skip('pass')
    def test_admin_14(self): pass
        # '''新增估价单'''


    #@unittest.skip('pass')
    def test_admin_15(self):
        '''估价单详情'''
        r=self.obj.get(url=geturl(id=20,row=15),row=15)
        print(r.text)

    # @unittest.skip('pass')
    def test_admin_16(self):
        '''删除估价单'''
        r=self.obj.delete(geturl(id=40,row=16),row=16)
        print(r.text)

    # @unittest.skip('pass')
    def test_admin_17(self):
        '''确认估价'''
        r=self.obj.patch(url=geturl(id=57,row=17),row=17)
        print(r.text)

    # @unittest.skip('pass')
    def test_admin_18(self):
        '''重新爬取'''
        r=self.obj.get(url=geturl(id=55,row=18),row=18)
        print(r.text)

    # @unittest.skip('pass')
    def test_admin_19(self):
        '''下载估价单'''
        r=self.obj.get(url=geturl(id=55,row=19),row=19)
        print(r.text)

    @unittest.skip('pass')
    def test_admin_20(self):
        '''上传指导价'''
        pass

    # @unittest.skip('pass')
    def test_admin_21(self):
        '''生成呆料单'''
        r=self.obj.post(data=evaOverstock(address='南京',delivery="CN",evaluateId=54,factoryId=31,invType='TL',name='测试',premium='2.3',isRfq='Y',row=21),row=21)
        print(r.text)

    def test_admin_22(self):
        '''修正估价价格'''
        r = self.obj.patch(data=overStockpart(partsId=1370,updatePrice=1.3,row=22),row=22)
        print(r.text)

    def test_admin_23(self):
        '''删除选中物料'''
        r = self.obj.delete(url=partList(id=39,partsIds =[1318,1319,1321,1320],row=23),row=23)
        print(r.text)

    def test_admin_24(self):
        '''一键删除冷门料'''
        r = self.obj.delete(url=geturl(id=55,row=24), row=24)
        print(r.text)
    @unittest.skip('pass')
    def test_admin_25(self):pass
        # '''上传出价'''
        # r = self.obj.delete(url=geturl(id=55, row=25), row=25)
        # print(r.text)
    def test_admin_26(self):
        '''报价预览'''
        r = self.obj.get(url=geturl(id=132, row=26), row=26)
        print(r.text)

    def test_admin_27(self):
        '''下载出价表格'''
        r = self.obj.get(url=geturl(id=132, row=27), row=27)
        print(r.text)


    def test_admin_28(self):
        '''标记删除|取消标记'''
        r = self.obj.patch(data=markId(id=11707,status='Y',row=28), row=28)
        print(r.text)

    def test_admin_29(self):
        '''预览生成订单----D'''
        r = self.obj.post(url=geturl(id=132,row=29),data=overOrder(customerId=85,entityId=[25524,22525,25526],row=29),row=29)
        print(r.text)

    def test_admin_30(self):
        '''修改原表----D'''
        r = self.obj.patch(url=geturl(id=205, row=30),
                          data=partprice(partId=11707, row=30), row=30)
        print(r.text)

    def test_admin_31(self):
        '''删除日志'''
        r = self.obj.delete(url=geturl(id=424, row=31), row=31)
        print(r.text)

    def test_admin_32(self):
        '''查看沟通日志'''
        r = self.obj.get(url=geturl(id=205, row=32), row=32)
        print(r.text)

    def test_admin_33(self):
        '''呆料单列表'''
        r = self.obj.get(params=detail(page=1,pageSize=100,row=33), row=33)
        print(r.text)

    def test_admin_34(self):
        '''新增呆料单----D'''
        r = self.obj.post(data=evaOverstock(address="",delivery ="HK",factoryId=15,invType="ZB",name ="这是自动化上传的单子",isRfq="N",row=34), row=34)
        print(r.text)

    def test_admin_35(self):
        '''呆料单编辑详情'''
        r = self.obj.get(url=geturl(id=205,row=35), row=35)
        print(r.text)

    def test_admin_36(self):
        '''编辑呆料单----D'''
        r = self.obj.post(url=geturl(id=205, row=36),data=evaOverstock(address="苏州",delivery="HK",factoryId=92,invType="TL",name="这是自动化上传的单子",id=205,isRfq='N',row=36),row=36)
        print(r.text)
    def test_admin_37(self):
        '''删除呆料单'''
        r = self.obj.delete(url=geturl(id=205, row=37), row=37)
        print(r.text)

    def test_admin_38(self):
        '''下载呆料单原表'''
        r = self.obj.get(url=geturl(id=215, row=38), row=38)
        print(r.text)

    def test_admin_39(self):
        '''工厂(供应商)下拉框'''
        r = self.obj.get(params=factorySO(keyword="上海", row=39), row=39)
        print(r.text)

    def test_admin_40(self):
        '''呆料单列表-更多'''
        r = self.obj.get(params=detail(page=1,pageSize=100, row=40), row=40)
        print(r.text)

    def test_admin_41(self):
        '''更新状态(上架、下架)'''
        r = self.obj.patch(data=overStatus(id=215, status="N", row=41), row=41)
        print(r.text)

    def test_admin_42(self):
        '''下载呆料模板'''
        r = self.obj.get(params=None,url=None,row=42)
        print(r.text)

    def test_admin_43(self):
        '''置顶、取消置顶'''
        r = self.obj.patch(overStatus(id=214,status='Y',row=43),row=43)
        print(r.text)

    def test_admin_44(self):
        '''品牌列表,有分页'''
        r = self.obj.get(detail(page=1,pageSize=100,key='HPV',row=44),row=44)
        print(r.text)

    def test_admin_45(self):
        '''保存'''
        r = self.obj.post(brand(linkIds=4063, shortName=100, name='HPV', row=45), row=45)
        print(r.text)

    def test_admin_46(self):
        '''修改'''
        r = self.obj.post(brand(linkIds=4063, shortName=100, name='CVB',id=4063,row=46), row=46)
        print(r.text)

    def test_admin_47(self):
        '''删除'''
        r = self.obj.delete(geturl(id=4810,row=47), row=47)
        print(r.text)

    def test_admin_48(self):
        '''品牌列表无分页'''
        r = self.obj.get(row=48)
        print(r.text)

    def test_admin_49(self):
        '''客户信息搜索'''
        r = self.obj.get(params=detail(page=1,pageSize=100,key="上海",row=49),row=49)
        print(r.text)

    def test_admin_50(self):
        '''添加客户信息'''
        r = self.obj.post(data=customerAdd(company="sisi-0023",name="mumu-0023",phone=15623145698,row=50),row=50)
        print(r.text)


    def test_admin_51(self):
        '''修改客户信息'''
        r = self.obj.put(data=customerAdd(company="sisi-0023",name="tes-001",phone=15618822221,row=51,id=83),row=51)
        print(r.text)

    def test_admin_52(self):
        '''客户详情'''
        r = self.obj.get(url=geturl(id=83,row=52),row=52)
        print(r.text)

    def test_admin_53(self):
        '''删除'''
        r = self.obj.delete(url=geturl(id=83,row=53), row=53)
        print(r.text)

    def test_admin_54(self):
        '''客户为新的标识取消'''
        r = self.obj.delete(url=partList(id=128,partsIds=4,row=54), row=54)
        print(r.text)

    def test_admin_55(self):
        '''分配'''
        r = self.obj.post(data=distributeSu(operatingId=128, list=[128,117,114,113], row=55), row=55)
        print(r.text)

    def test_admin_56(self):
        '''客户信息下拉框'''
        r = self.obj.get(params=detail(page=1, pageSize=10,key='上海',row=56), row=56)
        print(r.text)

    def test_admin_57(self):
        '''客户信息下拉框'''
        r = self.obj.get(row=57)
        print(r.text)




    def test_admin_58(self):
        '''数据中心id号(58-71)'''
        r = self.obj.get(
            orderover(cycleType='weeks', endTime='2019-06-23 23:59:59', startTime='2019-06-17 23:59:59',type='customer', row=58), row=70)
        print(r.text)

    def test_admin_59(self):
        '''数据字典列表有分页'''
        r = self.obj.get(detail(page=1, pageSize=100, row=72), row=72)
        print(r.text)



    def test_admin_60(self):
        '''添加字典'''
        r = self.obj.post(data=dict(flagName="客户类型", flagType="CUSTOMERTYPE",kvList={"LDS":"料单商","MUX":"目录型"},row=73), row=73)
        print(r.text)

    def test_admin_61(self):
        '''修改字典的键值'''
        r = self.obj.put(data=dictValue(id=101, dictValue="cszy",row=74), row=74)
        print(r.text)

    def test_admin_62(self):
        '''删除'''
        r = self.obj.delete(url=geturl(id=101,row=75),row=75)
        print(r.text)

    def test_admin_63(self):
        '''数据字典列表无分页'''
        r = self.obj.get(row=76)
        print(r.text)

    def test_admin_64(self):
        '''数据字典类型列表'''
        r = self.obj.get(row=77)
        print(r.text)

    # def test_admin_65(self):
    #     '''素材列表'''
    #     r = self.obj.get(params=detail(page=1,pageSize=100,row=72),row=78)
    #     print(r.text)

    def test_admin_66(self):
        '''活动、供应商、合作伙伴'''
        r = self.obj.get(params=detail(page=1,pageSize=2,row=72),row=82)
        print(r.text)

    def test_admin_67(self):
        '''添加banner、活动、供应商、合作伙伴---D'''
        r = self.obj.post(data=friend(link="javascript:;",materialFile="",row=83),row=83)
        print(r.text)

    def test_admin_68(self):
        '''删除banner、活动、供应商、合作伙伴'''
        r = self.obj.delete(url=geturl(id=66,row=84),row=84)
        print(r.text)

    # def test_admin_69(self):
    #     '''vadas动态'''
    #     r = self.obj.get(params=detail(pageSize=100,page=1,row=72), row=84)
    #     print(r.text)
    # #
    # def test_admin_70(self):
    #     ''''''
    #     r = self.obj.post(data=News(content='这是自动化测试',source='',row=86,title='这是自动化测试'), row=86)
    #     print(r.text)

    def test_admin_89(self):
        '''编辑banner、活动、供应商、合作伙伴'''
        r = self.obj.post(data=friend(id=25, link='/pool',name='测试',type="BA", row=89), row=89)
        print(r.text)

    def test_admin_90(self):
        '''用户反馈列表'''
        r = self.obj.get(params=detail(page=1, pageSize=100,row=72), row=90)
        print(r.text)

    def test_admin_91(self):
        '''咨询反馈红点'''
        r = self.obj.get(row=91)
        print(r.text)
    def test_admin_92(self):
        '''取消咨询反馈红点'''
        r = self.obj.post(data=feedbackType(type='SQGYS',row=92),row=92)
        print(r.text)

    def test_admin_93(self):
        '''用户呆料列表'''
        r = self.obj.get(params=detail(page=1, pageSize=100, row=72), row=93)
        print(r.text)

    def test_admin_94(self):
        '''更新状态'''
        r = self.obj.post(url=geturl(id=1,row=72),row=94)
        print(r.text)
    def test_admin_95(self):
        '''申请供应商列表'''
        r = self.obj.get(params=detail(page=1, pageSize=100, row=72), row=95)
        print(r.text)

    def test_admin_96(self):
        '''更新状态'''
        r = self.obj.post(url=geturl(id=53,row=96),data=None,row=96)
        print(r.text)

    def mcc(self):
        '''MCC物料列表'''
        r = self.obj.get(params=detail(page=1, pageSize=100, row=72), row=110)
        print(r.text)


if __name__ == '__main__':
    unittest.main(verbosity=2)







