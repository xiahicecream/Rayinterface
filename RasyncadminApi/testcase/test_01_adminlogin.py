from unittest import TestCase
# import sys
# sys.path.apend('..')
from public_data.public_data import *
import unittest
import requests
import json

class AdminLogin(TestCase):
    '''管理员登录模块'''
    logger.info('=' * 30 + '[开始执行管理员登录模块接口用例]' + '=' * 30)
    def setUp(self):
        self.urlsite=(read_excel('publicData',1,1))  #公共url
        self.all_sheet=1     #写入的数据是第几张表
        self.sheetNAME='Adminmanager'   #读取的表的名字是哪一张

    def tearDown(self):
        logger.info(self.apiname)
        logger.info(self.parameter)
        logger.info(self.dd)

        '''将断言写数据弄成一个方法'''
    def requestHandler(self, reqdata, row):
        self.result = requests.post(self.urlsite, data=reqdata,verify=False)  # 发送post请求,将 verify 设置为 False，Requests 也能忽略对 SSL 证书的验证。

        self.dd = json.loads(self.result.text)  # 将json格式转换为python字典格式方便取出键值
        # 进行断言，将result实际值与表格中预期结果进行比对
        self.assertEqual(int(self.dd['result']), int(read_excel(self.sheetNAME, row, 6)))
        # # 写入result值，0为正常
        write_excel(self.all_sheet, row, 8, 'result:' + str(self.dd['result']))


    def test_login1(self,row=2):
        '''用户登录，密码正确'''
        self.apiname=read_excel(self.sheetNAME,row,2)   #用例名称
        self.parameter=read_excel(self.sheetNAME,row,5)#请求参数
        self.requestHandler(reqdata=self.parameter, row=row)
        # self.result=requests.post(self.urlsite,data=self.parameter,verify=False) #发送post请求,将 verify 设置为 False，Requests 也能忽略对 SSL 证书的验证。
        # self.dd= json.loads(self.result.text) #将json格式转换为python字典格式方便取出键值
        # #进行断言，将result实际值与表格中预期结果进行比对
        # self.assertEqual(int(self.dd['result']),int(read_excel(self.sheetNAME,row,6)))
        # # 写入result值，0为正常
        # write_excel(self.all_sheet, row, 8, 'result:'+str(self.dd['result']))
        token=self.dd["token"]     #登录获取token
        write_excel(0,3,1,token)        #讲token写到公共表publicData


    def test_login2(self,row=1):
        '''用户登录，密码错误'''
        self.apiname=read_excel(self.sheetNAME,row,2)   #用例名称
        self.parameter=Headers(read_excel('publicData',3,1),read_excel('Adminmanager',row,5))#请求参数
        self.requestHandler(reqdata=self.parameter,row=row)


    def test_login3(self,row=4):
        '''获取当前管理员信息'''
        self.apiname=read_excel(self.sheetNAME,row,2)
        self.parameter=Headers(read_excel('publicData',3,1),read_excel('Adminmanager',row,5))
        self.requestHandler(reqdata=self.parameter,row=row)

    def test_login4(self,row=5):
        '''更新当前管理员信息'''
        self.apiname=read_excel(self.sheetNAME,row,2)
        self.parameter=Headers(read_excel('publicData',3,1),read_excel('Adminmanager',row,5))
        self.requestHandler(reqdata=self.parameter, row=row)

    def test_login5(self,row=6):
        '''重登管理员信息'''
        self.apiname=read_excel(self.sheetNAME,row,2)
        self.parameter = read_excel(self.sheetNAME, row, 5)  # 请求参数
        self.requestHandler(reqdata=self.parameter, row=row)
        newtoken=self.dd["token"]     #登录获取token
        write_excel(0,4,1,newtoken)        #将token写到公共表publicData









if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(AdminLogin('test_login1'))
    suite.addTest(AdminLogin('test_login2'))
    runner = unittest.TextTestRunner()
    runner.run(suite)


