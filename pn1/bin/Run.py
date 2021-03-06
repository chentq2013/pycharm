from untils.operationExcel import OperationExcel
from email.mime.text import MIMEText
import smtplib
from tests.runHtml import *
class Runner():
    def __init__(self):
        self.excel=OperationExcel()
    @staticmethod
    def getSuite():
        '''获取要执行的测试套件'''
        suite=unittest.TestLoader().discover(
            start_dir=os.path.join(os.path.dirname(os.path.dirname(__file__)),'tests'),
            pattern='test_*.py',
            top_level_dir=None
        )
        return suite




    def send_email(self,to_user,sub,content):
        '''
        发送邮件内容
        :param to_user:发送邮件的人
        :param sub:主题
        :param content:邮件内容
        '''
        global send_mail
        global send_user

        send_mail='smtp.qq.com'
        send_user='2213627107@qq.com'
        print(content)
        message=MIMEText(content, 'html', 'utf-8')
        message['Subject']=sub
        message['FROM']=send_user
        message['To']=to_user
        server=smtplib.SMTP()
        server.connect(send_mail)
        server.login('2213627107@qq.com','jymofnlvlsabebha')
        server.sendmail(send_user,to_user,message.as_string())
        server.close()



    def main_run(self):
        '''批量执行测试用例'''
        unittest.TextTestRunner().run(self.getSuite())
        fp = os.path.join(os.path.dirname(__file__))
        parent= os.path.abspath(os.path.dirname(fp) + os.path.sep + ".")
        parent=os.path.join(parent,"tests","report","1111.html")
        parent=parent.replace("\\","/")
        htmlf = open(parent, 'r', encoding="utf-8")
        count='通过数:{0}  失败数:{1}  通过率:{2}'.format(
            self.excel.run_sucess_result(),
            self.excel.run_fail_result(),
            self.excel.run_pass_rate())
        content =count+ htmlf.read()
        print('please wait while the statistics test results are sent in the mail')
        self.send_email('2484779229@qq.com','接口自动化测试报告',content)

if __name__ == '__main__':
    Runner().main_run()
