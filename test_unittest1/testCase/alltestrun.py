import unittest
import os
import HTMLTestRunner
import time
#执行模块下所有的测试用例
def alltestcase():
    suite=unittest.TestLoader().discover(
            start_dir=os.path.dirname(__file__),
            pattern='test_*.py',
            top_level_dir=None)
    return suite

def getnowtime():
    return time.strftime('%Y-%m-%d %H_%M_%S',time.localtime(time.time()))

def run():
    fp = os.path.join(os.path.dirname(__file__), 'report',getnowtime()+ 'testreport.html')
    print(fp)

    HTMLTestRunner.HTMLTestRunner(stream=open(fp,'wb'),
                                  title='自动化测试报告',
                                  description='自动化测试报告详细信息',
                                  ).run(alltestcase())

if __name__ == '__main__':
    run()







