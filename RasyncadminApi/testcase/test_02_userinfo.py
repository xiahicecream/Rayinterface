from unittest import TestCase
from public_data.public_data import *
import unittest
import requests
import json

class UserInfo(TestCase):
    logger.info('=' * 30 + '[开始执行用户信息模块接口用例]' + '=' * 30)
    def setUp(self):
        self.urlsite = (read_excel('publicData', 1, 1))  # 公共url
        self.all_sheet = 2  # 写入的数据是第几张表
        self.sheetNAME = 'Userinfo'  # 读取的表的名字是哪一张

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

    def test_userinfo1(self,row=1):
        '''获取用户列表'''
        self.apiname=read_excel(self.sheetNAME,row,2)
        self.parameter=Headers(read_excel('publicData',4,1),read_excel('Userinfo',row,5))
        self.requestHandler(reqdata=self.parameter,row=row)

    def test_userinfo2(self,row=3):
        '''新建用户'''
        self.apiname=read_excel(self.sheetNAME,row,2)
        self.parameter=Headers(read_excel('publicData',4,1),read_excel('Userinfo',row,5))
        self.requestHandler(reqdata=self.parameter,row=row)

    # def test_userinfo3(self,row=4):
    #     '''更新用户'''
    #     self.apiname=read_excel(self.sheetNAME,row,2)
    #     self.parameter=Headers(read_excel('publicData',4,1),read_excel('Userinfo',row,5))
    #     print(self.parameter)
    #     self.requestHandler(reqdata=self.parameter,row=row)

    def test_userinfo4(self,row=5):
        '''更新密码'''
        self.apiname=read_excel(self.sheetNAME,row,2)
        self.parameter=Headers(read_excel('publicData',4,1),read_excel('Userinfo',row,5))
        self.requestHandler(reqdata=self.parameter,row=row)

    def test_userinfo5(self, row=6):
        '''用户锁定'''
        self.apiname = read_excel(self.sheetNAME, row, 2)
        self.parameter = Headers(read_excel('publicData', 4, 1), read_excel('Userinfo', row, 5))
        self.requestHandler(reqdata=self.parameter, row=row)

    def test_userinfo6(self, row=7):
        '''用户解锁'''
        self.apiname = read_excel(self.sheetNAME, row, 2)
        self.parameter = Headers(read_excel('publicData', 4, 1), read_excel('Userinfo', row, 5))
        self.requestHandler(reqdata=self.parameter, row=row)

    def test_userinfo7(self, row=2):
        '''用户删除'''
        self.apiname = read_excel(self.sheetNAME, row, 2)
        self.parameter = Headers(read_excel('publicData', 4, 1), read_excel('Userinfo', row, 5))
        print(self.parameter)
        self.requestHandler(reqdata=self.parameter, row=row)

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(UserInfo('test_userinfo1'))
    runner = unittest.TextTestRunner()
    runner.run(suite)
