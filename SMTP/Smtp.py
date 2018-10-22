# -*- coding: utf-8 -*-
# @Time    : 2018/9/28 9:13
# @Author  : xuyun
import smtplib,os,HTMLTestRunner,unittest,time,datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

def sendmain(file) :

    # 发送邮箱
    sender = '819077607@qq.com'
    # 接受邮箱
    # receiver = '1035612906@qq.com'
    receiver = '2565701045@qq.com'

    # 发送邮箱主题
    subget = 'python email test'
    # 发送邮箱服务器
    smtpserver = 'smtp.qq.com'
    # 发送邮箱用户名/密码
    username = '819077607@qq.com'
    password = 'rqlyswejgsqkbcbj'

    # msg = MIMEText('HELLO 这个一封测试信息','text','utf-8')
    # msg = MIMEText('<html><h1>this is python smtp test</h1></html>','html','utf-8')
    msg = MIMEText('<html><h1>琪琪呀呀呀哎呀呀哎呀呀呀this is python SMTP test</h1></html>','html','utf-8')

    msg['Subject'] = Header(subget, 'utf-8')


    smtp = smtplib.SMTP()
    smtp.connect('smtp.qq.com')
    smtp.login(username,password)
    smtp.sendmail(sender,receiver, msg.as_string())
    smtp.quit()
    print('email sent')

def sendreport() :
    result_dir = 'D://'
    lists = os.listdir(result_dir)
    lists.sort(key=lambda fn:   os.path.getatime(result_dir+'//'+fn)
                                         if not os.path.isabs(result_dir + '//' + fn) else 0)
    print(u'最新的测试报告为: ' + lists[-1])
    file = os.path.join(result_dir, lists[-1])
    print(file)
    sendmain(file)
