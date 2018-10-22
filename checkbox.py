# -*- coding: utf-8 -*-
# @Time    : 2018/9/14 15:23
# @Author  : xuyun
import unittest,time,os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.select import Select

class boxtest(unittest.TestCase) :
    def setUp(self):
        self.drviet = webdriver.Chrome()

    def test_search_in_python_org(self):    # 登录
        driver = self.drviet
        # 设置隐性等待时长
        driver.implicitly_wait(10)
        driver.get('http://10.0.0.9/login')
        driver.implicitly_wait(30)
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="username"]').send_keys('Xadmin')
        driver.find_element_by_xpath('//*[@id="username"]').send_keys(Keys.TAB)
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="password"]').send_keys('123456')
        driver.find_element_by_xpath('//*[@id="password"]').send_keys(Keys.TAB)
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="loginBtn"]').click()
        time.sleep(1)
        driver.get_screenshot_as_file('D:/error_png.png')
#




