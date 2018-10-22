# -*- coding: utf-8 -*-
# @Time    : 2018/9/27 10:39
# @Author  : xuyun
import unittest,HTMLTestRunner,time,smtplib,os
from email.mime.text import MIMEText
from email.header import Header
from TestCase import TestCase_Operation,test_get
testunit = unittest.TestSuite()

testunit.addTest(unittest.makeSuite(TestCase_Operation.OperationCase))
testunit.addTest(unittest.makeSuite(test_get.OperationCase))

def sendmain(file) :
    # 发送邮箱
    sender = '819077607@qq.com'
    # 接受邮箱
    receiver = '2565701045@qq.com'
    # 定义正文
    f = open(file, 'rb')
    main_body = f.read()
    print(main_body)
    f.close()
    msg = MIMEText(main_body,_subtype='html',_charset='utf-8')
    # 定义标题
    msg['Subject'] = u'DC云AC测试报告'
    # 发送邮箱主题
    # subget = 'python email test'
    # 发送邮箱服务器
    msg['date'] = time.strftime('%a,%d%b%Y%H:%M:%S%z')
    smtp = smtplib.SMTP()
    smtp.connect('smtp.qq.com')
    smtp.login('819077607@qq.com','rqlyswejgsqkbcbj')
    # 发送邮箱用户名/密码
    # username = '819077607@qq.com'
    # password = 'rqlyswejgsqkbcbj'
    smtp.sendmail(sender,receiver, msg.as_string())
    smtp.quit()
    print('email sent')

def sendreport() :
    result_dir = 'D:\TestingReport'
    lists = os.listdir(result_dir)
    lists.sort(key=lambda fn:   os.path.getatime(result_dir+'\\'+fn)
                                         if not os.path.isabs(result_dir + '\\' + fn) else 0)
    print('最新的测试报告为: ' + lists[-2])
    file = os.path.join(result_dir, lists[-2])
    print(file)
    sendmain(file)


now=time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))
file = 'D:/TestingReport/' + now + 'TestReport.html'
fp = open(file,'wb')

runner = HTMLTestRunner.HTMLTestRunner(
    stream=fp,
    title = u'敦崇云AC测试报告: ',
    description = u'用例执行详情: '
)

if __name__ == '__main__' :
    runner.run(testunit)
    sendreport()