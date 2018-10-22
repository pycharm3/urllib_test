# -*- coding: utf-8 -*-
# @Time    : 2018/9/18 15:08
# @Author  : xuyun
import time,random
from checkbox import boxtest,Select,Keys
from Method import generate_random_str,generate_random_NS,randomMAC
A = boxtest()
A.setUp()
A.test_search_in_python_org()
A.drviet.implicitly_wait('30')
# while True:

A.drviet.find_element_by_xpath('//*[@id="content"]/div/div[2]/div[1]/div[1]/a').click()  # 添加设备
time.sleep(1)
A.drviet.find_element_by_xpath('//*[@id="addDevice"]/div[1]/div').click()  # 点击设备类型选框
time.sleep(1)
# 百度了半个小时发现要把display=none设置为display=block设置为可见
js = 'document.querySelectorAll("select")[0].style.display="block";'
A.drviet.execute_script(js)
sel = A.drviet.find_element_by_tag_name('select')
# 选择value = 1也就是ap选项
Select(sel).select_by_value('1')
time.sleep(1)
#  选择设备型号
A.drviet.find_element_by_xpath('//*[@id="model_auto_chosen"]/a/span').click()
time.sleep(1)
# 导入js方法把display设置为可见
js = 'document.querySelectorAll("select")[0].style.display="block";'
A.drviet.execute_script(js)
model_xpath = '//*[@id="model_auto_chosen"]/div/ul/li[' + str(random.randint(2, 20)) + ']'
time.sleep(2)
# 点击选择设备型号
A.drviet.find_element_by_xpath(model_xpath).click()
time.sleep(2)
# 点击设备mac填写选项
A.drviet.find_element_by_xpath('//*[@id="mac"]').click()
# 填写设备mac
A.drviet.find_element_by_xpath('//*[@id="mac"]').send_keys(randomMAC())
time.sleep(1)
# 点击序列号填写框
A.drviet.find_element_by_xpath('//*[@id="serialNum"]').click()
time.sleep(1)
A.drviet.find_element_by_xpath('//*[@id="serialNum"]').send_keys(generate_random_NS())
# 点击位置信息输入框
A.drviet.find_element_by_xpath('//*[@id="positionDescription"]').click()
A.drviet.find_element_by_xpath('//*[@id="positionDescription"]').send_keys(generate_random_str())
time.sleep(2)
# 点击提交添加设备信息
A.drviet.find_element_by_xpath('//*[@id="addDevice"]/div[7]/div/input').send_keys(Keys.ENTER)
time.sleep(2)