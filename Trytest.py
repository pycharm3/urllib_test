# -*- coding: utf-8 -*-
# @Time    : 2018/9/21 17:29
# @Author  : xuyun
from selenium import webdriver
driver = webdriver.Chrome()
driver.get('http://10.0.0.9/login')
try:
    driver.find_element_by_id('username').send_keys('Xadmin')
    driver.find_element_by_id('password').send_keys('123456')
    driver.find_element_by_id('loginBtn').click()
except:
    driver.get_screenshot_as_file('D:/Try.png')
username = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/ul/li[7]/a').text
if username == u'Xadmin' :
    print('登录成功')
else:
    raise NameError('username Error!')
inputs = driver.find_element_by_tag_name('input')
a = 0
for i in inputs:
    if i.get_attribute('type') == 'checkbox':
        a +=1
print('当前列表文件为%d' %a)
driver.quit()