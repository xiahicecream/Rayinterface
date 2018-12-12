from unittest import TestCase
from public_data.public_data import *
import unittest
import requests
import json

class UserInfo(TestCase):
    logger.info('=' * 30 + '[开始执行高级设置模块接口用例]' + '=' * 30)
    def setUp(self):
        self.urlsite = (read_excel('publicData', 1, 1))  # 公共url
        self.all_sheet = 4  # 写入的数据是第几张表
        self.sheetNAME = 'Advance'  # 读取的表的名字是哪一张

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

    def test_advance1(self, row=1):
        '''获取邮箱信息'''
        self.apiname = read_excel(self.sheetNAME, row, 2)
        self.parameter = Headers(read_excel('publicData', 4, 1), read_excel('Advance', row, 5))
        self.requestHandler(reqdata=self.parameter, row=row)

    def test_advance2(self, row=2):
        '''设置邮箱信息'''
        self.apiname = read_excel(self.sheetNAME, row, 2)
        self.parameter = Headers(read_excel('publicData', 4, 1), read_excel('Advance', row, 5))
        self.requestHandler(reqdata=self.parameter, row=row)

    def test_advance3(self, row=3):
        '''设置高级配置'''
        self.apiname = read_excel(self.sheetNAME, row, 2)
        self.parameter = Headers(read_excel('publicData', 4, 1), read_excel('Advance', row, 5))
        self.requestHandler(reqdata=self.parameter, row=row)

    def test_advance4(self, row=4):
        '''获取高级配置'''
        self.apiname = read_excel(self.sheetNAME, row, 2)
        self.parameter = Headers(read_excel('publicData', 4, 1), read_excel('Advance', row, 5))
        self.requestHandler(reqdata=self.parameter, row=row)

    def test_advance5(self, row=5):
        '''获取实时传输列表'''
        self.apiname = read_excel(self.sheetNAME, row, 2)
        self.parameter = Headers(read_excel('publicData', 4, 1), read_excel('Advance', row, 5))
        self.result = requests.post(self.urlsite, data=self.parameter,verify=False)  # 发送post请求,将 verify 设置为 False，Requests 也能忽略对 SSL 证书的验证。
        self.dd = json.loads(self.result.text)  # 将json格式转换为python字典格式方便取出键值
        self.requestHandler(reqdata=self.parameter, row=row)

    def test_advance6(self,row=6):
        '''获取日志列表'''
        self.apiname=read_excel(self.sheetNAME,row,2)
        self.parameter=Headers(read_excel('publicData',4,1),read_excel('Advance',row,5))
        self.result=requests.post(self.urlsite,data=self.parameter,verify=False)
        self.dd=json.loads(self.result.text)
        self.requestHandler(reqdata=self.parameter,row=row)
        print(self.dd)

    def test_login7(self,row=3):
        '''用户退出'''
        self.apiname=read_excel('Adminmanager',row,2)
        self.parameter=Headers(read_excel('publicData',4,1),read_excel('Adminmanager',row,5))
        self.result = requests.post(self.urlsite, data=self.parameter,verify=False)  # 发送post请求,将 verify 设置为 False，Requests 也能忽略对 SSL 证书的验证。
        self.dd = json.loads(self.result.text)  # 将json格式转换为python字典格式方便取出键值
        # 进行断言，将result实际值与表格中预期结果进行比对
        self.assertEqual(int(self.dd['result']), int(read_excel('Adminmanager', row, 6)))
        # # 写入result值，0为正常
        write_excel(1, row, 8, 'result:' + str(self.dd['result']))


