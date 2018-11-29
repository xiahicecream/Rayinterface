#coding=utf-8
from HTMLTestRunner import HTMLTestRunner
# from HTMLTestReportCN import HTMLTestRunner
from public_data.EmailSend import emailsend
from  public_data import *
import os,sys,time
import unittest
sys.path.append("../public")


if __name__ == '__main__':

    start = time.clock()
    test_dir = 'G:/RasyncadminApi/testcase'
    report_dir = 'G:/RasyncadminApi/report/'
    discover = unittest.defaultTestLoader.discover(test_dir,pattern='test_*.py')
    #now = time.strftime(u'%Y-%m-%d.%H.%M.%S')
    now = time.strftime('%Y-%m-%d')
    filename = report_dir + '%s_result.html'%now  #这个filename是生成的自动化测试报告的文件名
    fp = open(filename,'wb')
    runner = HTMLTestRunner(stream=fp,title='测试报告',description='用例的执行情况')
    runner.run(discover)
    fp.close()
    end = time.clock()
    all_time = end-start
    print('\n','总共用时%.0f秒' % all_time)
    emailsend()

