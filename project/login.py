# -*- coding: utf-8 -*-
# @Time    : 2018/9/25 11:22
# @Author  : xuyun
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import unittest,time,os
from project import deflogin

# # 打开username.txt并用source.read读取username.txt
# source = open(r'D:\username.txt','r')
# un = source.read()
# source.close()
# # 打开password.txt并用source.read读取username.txt
# source2 = open(r'D:\password.txt','r')
# pw = source2.read()
# source2.close()

# 通过定义一个def文件进行调用函数username和password
un,pw = deflogin.fun()
print(un,pw)
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('http://10.0.0.9/login')
driver.find_element_by_id('username').clear()
driver.find_element_by_id('username').send_keys(un)
driver.find_element_by_id('password').clear()
driver.find_element_by_id('password').send_keys(pw)
driver.find_element_by_xpath('//*[@id="loginBtn"]').click()
time.sleep(2)
# 截图方法
driver.get_screenshot_as_file('D:\login.png')
driver.quit()

if __name__ == '__main__':
    unittest.main()

