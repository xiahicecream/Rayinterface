from unittest import TestCase
from public_data.public_data import *
import unittest
import requests
import json

class UserInfo(TestCase):
    logger.info('=' * 30 + '[开始执行服务器信息模块接口用例]' + '=' * 30)
    def setUp(self):
        self.urlsite = (read_excel('publicData', 1, 1))  # 公共url
        self.all_sheet = 3  # 写入的数据是第几张表
        self.sheetNAME = 'Serverinfo'  # 读取的表的名字是哪一张

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
    def test_serverinfo1(self, row=6):
        '''获取服务器实时监控信息'''
        self.apiname = read_excel(self.sheetNAME, row, 2)
        self.parameter = Headers(read_excel('publicData', 4, 1), read_excel('Serverinfo', row, 5))
        self.requestHandler(reqdata=self.parameter, row=row)

    def test_serverinfo2(self, row=7):
        '''获取服务器license激活信息'''
        self.apiname = read_excel(self.sheetNAME, row, 2)
        self.parameter = Headers(read_excel('publicData', 4, 1), read_excel('Serverinfo', row, 5))
        self.requestHandler(reqdata=self.parameter, row=row)
    def test_serverinfo3(self, row=1):
        '''获取服务器信息'''
        self.apiname = read_excel(self.sheetNAME, row, 2)
        self.parameter = Headers(read_excel('publicData', 4, 1), read_excel('Serverinfo', row, 5))
        self.requestHandler(reqdata=self.parameter, row=row)
        a=self.dd['server']  #因为版本号每次都会变，所以每次都要先获取版本号，在test2中更新服务器内使用
        a=json.dumps(a)
        write_excel(self.sheetNAME,2,5,a)
    def test_serverinfo4(self, row=2):
        '''更新服务器信息'''
        self.apiname = read_excel(self.sheetNAME, row, 2)
        self.a={"action": "UPDATE_SERVER"}
        self.a=json.dumps(self.a)
        self.parameter = Headers(read_excel('publicData', 4, 1),self.a)  #将公共部分与action合并
        self.parameter=json.loads(self.parameter)  #转换成python字典
        self.server=read_excel(self.sheetNAME,row,5)#取出excel的server值
        self.server=json.loads(self.server)#将server内信息转换为字典
        self.parameter['server']=self.server   #添加表中server新的键与键值

        self.parameter['server']['enableFTPS']=1   #更新服务器开启加密传输
        self.parameter['server']['license'] = '57d7ccc66356e'#更新服务器license信息
        self.parameter['server']['name'] = 'xuegao server'  #更新服务器名称
        self.parameter=json.dumps(self.parameter)  #转换成json格式进行http请求

        self.requestHandler(reqdata=self.parameter,row=row)


    def test_serverinfo5(self, row=5):
        '''关闭传输服务器'''
        self.apiname = read_excel(self.sheetNAME, row, 2)
        self.parameter = Headers(read_excel('publicData', 4, 1), read_excel('Serverinfo', row, 5))
        self.requestHandler(reqdata=self.parameter, row=row)

    def test_serverinfo6(self, row=3):
        '''启动传输服务器'''
        self.apiname = read_excel(self.sheetNAME, row, 2)
        self.parameter = Headers(read_excel('publicData', 4, 1), read_excel('Serverinfo', row, 5))
        self.requestHandler(reqdata=self.parameter, row=row)

    def test_serverinfo7(self, row=4):
        '''重启传输服务器'''
        self.apiname = read_excel(self.sheetNAME, row, 2)
        self.parameter = Headers(read_excel('publicData', 4, 1), read_excel('Serverinfo', row, 5))
        self.requestHandler(reqdata=self.parameter, row=row)






