# -*- comding:utf-8   -*-


import smtplib
from bs4 import BeautifulSoup
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

import time
from email.mime.base import MIMEBase
from email.utils import parseaddr, formataddr


# aXbAWHc2C5KCWx2R

def emailsend():
    '''发送自动化报告到指定邮箱'''
    sender = 'iicecream@qq.com'  # 发件人邮箱
    receivers = ['iicecream@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱


    # 创建一个带附件带图片的实例
    message = MIMEMultipart()
    message['From'] = Header("雪糕", 'utf-8')  # 发件人
    message['To'] = Header('雪糕', 'utf-8')  # 收件人姓名
    subject = '镭速管理员后台接口自动化测试报告'  # 邮件标题
    message['Subject'] = Header(subject, 'utf-8').encode()

    msgAlternative = MIMEMultipart('alternative')
    message.attach(msgAlternative)

    mail_msg = """
    <h1><font size="5" coor="black">如果要查看具体详情请下载附件</font></h1>
    """
    now = time.strftime('%Y-%m-%d')
    path = 'G:/RasyncadminApi/report/' + '%s_result.html' % now
    f = open(path, 'rb')
    mail_body = f.read()
    f.close()

    msgAlternative.attach(MIMEText(mail_msg, 'html', 'utf-8'))
    msgAlternative.attach(MIMEText(mail_body, 'html', 'utf-8'))


    now = time.strftime('%Y-%m-%d')        #定义时间变量
    # 构造附件1，传送当前目录下的 test.txt 文件
    fujian1 = MIMEText(open('G:/RasyncadminApi/logs/' + '%s.log' % now, 'rb').read(), 'base64', 'utf-8')
    fujian1["Content-Type"] = 'application/octet-stream'
    fujian1["Content-Disposition"] = 'attachment; filename="%s.txt"'% now # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
    message.attach(fujian1)


    # 构造附件2，传送当前目录下的 result.html 文件
    fujian2 = MIMEText(open('G:/RasyncadminApi/report/' + '%s_result.html' % now, 'rb').read(), 'html', 'utf-8')
    fujian2["Content-Type"] = 'application/octet-stream'
    fujian2["Content-Disposition"] = 'attachment; filename="%s_result.html"' % now
    message.attach(fujian2)

    try:
        smtpObj = smtplib.SMTP_SSL('smtp.qq.com', 465)
        smtpObj.login('iicecream@qq.com', 'kfkqxveyatcvbhff')
        smtpObj.sendmail(sender, receivers, message.as_string())
        print("邮件发送成功")
    except smtplib.SMTPException:
        print("Error: 无法发送邮件")



