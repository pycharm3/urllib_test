# -*- coding: utf-8 -*-
# @Time    : 2018/9/27 10:35
# @Author  : xuyun
import unittest, ADDproject, DelectAP, HTMLTestRunner
from project import login
from time import strftime, localtime, time


class OperationCase(unittest.TestCase):
    def test_login(self):
        u"""敦崇云平台登录测试"""
        return login

    def test_ADDdevice(self):
        u"""敦崇云平台添加设备测试"""
        return ADDproject

    def test_DelectAP(self):
        u"""敦崇云平台删除设备测试"""
        return DelectAP


# PyCharm会默认使用自带的unittest框架来执行单元测试，不会执行main函数中的代码，所以不生成测试报告
# if __name__ == '__main__' :
testunit = unittest.TestSuite()
testunit.addTest(OperationCase('test_login'))
testunit.addTest(OperationCase('test_ADDdevice'))
testunit.addTest(OperationCase('test_DelectAP'))
now = strftime("%Y-%m-%M-%H_%M_%S", localtime(time()))  # 获取当前时间
filename = now + 'D://result.html'
fp = open('D:/TestingReport/TestReport.html', 'wb')
runner = HTMLTestRunner.HTMLTestRunner(
    stream=fp,
    title=u'敦崇云AC测试报告: ',
    description=u'测试报告详情页: '
)
# runner.run(testunit)
