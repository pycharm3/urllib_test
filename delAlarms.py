# -*- coding: utf-8 -*-
# @Time    : 2018/9/19 15:00
# @Author  : xuyun
from checkbox import boxtest,Select,Keys
import time
from checkbox import boxtest
A = boxtest()
A.setUp()
A.test_search_in_python_org()

A.drviet.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/ul/li[2]/a').click()
A.drviet.find_element_by_xpath('//*[@id="treeMenu"]/li[4]/a').click()
cookies = A.drviet.get_cookies()
print(cookies)
time.sleep(1)
while True:
    A.drviet.find_element_by_xpath('//*[@id="datatable"]/thead/tr/th[1]/label/input').click()
    time.sleep(1)
    A.drviet.find_element_by_xpath('//*[@id="content"]/div/div[2]/div[3]/div/button').click()
    time.sleep(1)
    A.drviet.switch_to_alert().accept()
    time.sleep(2)

