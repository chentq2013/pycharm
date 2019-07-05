
import unittest
import os
import HTMLTestRunner



def getSuite():
    '''获取要执行的测试套件'''
    suite = unittest.TestLoader().discover(
        start_dir=os.path.join(os.path.dirname(__file__)),
        pattern='test_*.py',
        top_level_dir=None
    )
    return suite

# def getnowtime():
#     return '1111'
#

def run():
    '''批量执行测试用例'''
    fp = os.path.join(os.path.dirname(__file__), 'report','test.html')
    print(fp)

    HTMLTestRunner.HTMLTestRunner(stream=open(fp, 'wb'),
                                  title='接口自动化测试报告',
                                  description='自动化测试报告详细信息'
                                  ).run(getSuite())

if __name__ == '__main__':
    run()






