# -*- coding: utf-8 -*-
# @Time    : 2018/9/18 9:37
# @Author  : xuyun

import time
from selenium import webdriver
from checkbox import boxtest,Select,Keys
c = boxtest()
c.setUp()
c.test_search_in_python_org()
# while True:
# driver = webdriver.Chrome
js = 'document.querySelectorAll("select")[0].style.display="block";'
c.drviet.execute_script(js)
c.drviet.find_element_by_xpath('//*[@id="status_chosen"]/a').click()
c.drviet.find_element_by_xpath('//*[@id="status_chosen"]/div/ul/li[3]').click()
time.sleep(2)
c.drviet.find_element_by_xpath('//*[@id="content"]/div/div[2]/form/div[16]/button[3]').click()
time.sleep(2)
c.drviet.find_element_by_xpath('//*[@id="content"]/div/div[2]/div[1]/div[1]/button[1]').is_displayed()
c.drviet.find_element_by_xpath('//*[@id="content"]/div/div[2]/div[1]/div[1]/button[1]').click()
c.drviet.switch_to_alert().accept()
time.sleep(2)
