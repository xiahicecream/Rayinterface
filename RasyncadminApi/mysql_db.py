#coding:utf-8
import os
import configparser
import pymysql

base_dir = str(os.path.dirname(os.path.dirname(__file__))) #项目所在目录
base_dir = base_dir.replace('\\','/')
file_path = base_dir + '/db_config.ini'
print(file_path)

conf = configparser.ConfigParser()
conf.read(file_path)
host = conf.get('mysqlconf','host')
port = conf.get('mysqlconf','port')
user = conf.get('mysqlconf','user')
password = conf.get('mysqlconf','password')

print(host)


class DB:

    def __init__(self):
        try:
            #connect to the database
            self.connection = pymysql.Connect(host=host,
                                              port=port,
                                              user=user,
                                              password=password,
                                              db=DB)
        except:
            pass