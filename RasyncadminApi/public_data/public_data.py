import requests
import json
import xlrd,xlwt
import datetime,logging
from xlutils.copy import copy
import time



def read_excel(sheet,row,col):
    '''读取excel表公共方法'''
    a = xlrd.open_workbook('G:/RasyncadminApi/datas/apiTestCase.xls')
    b = a.sheet_by_name(sheet)
    c = b.cell_value(row,col)
    return c


def write_excel(list,row,col,data):
    '''写入excel表公共方法'''
    file = r"G:/RasyncadminApi/datas/apiTestCase.xls"
    rb = xlrd.open_workbook(file, formatting_info=True)
    wb = copy(rb)
    ws = wb.get_sheet(list)
    ws.write(row, col, data)
    wb.save(file)
    print('写入数据成功')
    #list 第几章表0开始，row几行, col几列, data写入的数据

def Headers(token,data):
    '''将公共部分与请求参数拼接起来'''
    headers = {
        "id":str(time.time()),
        "device":"",
        "module":"WEBADMIN",
        "token":token,
        "version": "3.0.3.2"
    }
    data=json.loads(data)
    data.update(headers)
    return json.dumps(data)



def setlogging():
    '''打印日志公共方法'''
    t = str(datetime.datetime.now()).split(' ')[0]    # 创建一个logger

    logger = logging.getLogger()
    logger.setLevel(level=logging.DEBUG)
    handler = logging.FileHandler('G:/RasyncadminApi/logs/' + t + ".log") # log_path = os.path.dirname(os.getcwd()) + '/Logs/'  # 项目根目录下/Logs 保存日志
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')  # 定义handler的输出格式
    handler.setFormatter(formatter)

    console = logging.StreamHandler()
    console.setLevel(logging.DEBUG)

    logger.addHandler(handler)  # 给logger添加handler
    logger.addHandler(console)

    return logger


#日志的公共方法
logger = setlogging()

