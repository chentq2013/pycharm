import xlrd
from untils.public import *
from untils.excel_data import *
from xlutils.copy import copy
class OperationExcel:
    def getExcel(self):
        db=xlrd.open_workbook(data_dir('data','data.xlsx'))
        sheet=db.sheet_by_index(0)
        return sheet
    def get_rows(self):
        '''获取excel的行数'''
        return self.getExcel().nrows
    def get_row_cel(self,row,col):
        '''获取单元格的内容'''
        return self.getExcel().cell_value(row,col)
    def getUrl(self,row):
        '''获取请求地址'''
        return self.get_row_cel(row,getUrl())
    def get_request_data(self,row):
        '''获取请求参数'''
        return self.get_row_cel(row,get_request_data())
    def getExpect(self,row):
        '''获取预期结果'''
        return self.get_row_cel(row,getExpect())
    def getResult(self,row):
        '''获取实际的结果'''
        return self.get_row_cel(row,getResult())
    def getCaseID(self,row):
        '''获取测试id'''
        return self.get_row_cel(row,getCaseID())

    def writeResult(self,row,content):
        '''测试结果写到文件中'''
        col=getResult()
        work=xlrd.open_workbook(data_dir('data','data.xlsx'))
        old_content=copy(work)
        ws=old_content.get_sheet(0)
        ws.write(row,col,content)
        old_content.save(data_dir('data','data.xls'))

    def run_sucess_result(self):
        '''获取成功的测试用例'''
        pass_count=[]
        fail_count=None
        for i in range(1,self.get_rows()):
            if self.getResult(i)=='pass':
                pass_count.append(i)
        return int(len(pass_count))
    def run_fail_result(self):
        '''获取失败的测试用例'''
        return int((self.get_rows()-1)-self.run_sucess_result())

    def run_pass_rate(self):
        '''计算结果通过率'''
        rate=''
        if self.run_fail_result()==0:
            rate='100%'
        elif self.run_fail_result() !=0:
            rate=str(int(self.run_sucess_result()/(self.get_rows()-1)*100))+"%"
        return rate

# opera=OperationExcel()
# print(opera.getUrl(110))