# -*- coding: utf-8 -*-
# @Time    : 2018/9/17 15:47
# @Author  : xuyun
import re,string,random,time,unittest,sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
print(sys.path)

class dunchongAC(unittest.TestCase) :
    def setUp(self):
        self.drviet = webdriver.Chrome()
    def test_search_in_python_org(self):    # 登录
        driver = self.drviet
        driver.save_screenshot('xuyun.png')
        driver.get('http://10.0.0.9/login')
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="username"]').send_keys('Xadmin')
        driver.find_element_by_xpath('//*[@id="username"]').send_keys(Keys.TAB)
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="password"]').send_keys('123456')
        driver.find_element_by_xpath('//*[@id="password"]').send_keys(Keys.TAB)
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="loginBtn"]').click()
        time.sleep(1)

        driver.find_element_by_xpath('//*[@id="treeMenu"]/li[3]/a/span').click()
        time.sleep(2)
        # 刷新当前页面
        driver.refresh()
        # 点击项目名称
        driver.find_element_by_xpath('//*[@id="addUpdateProject"]/div[1]/div[1]/div/input').click()
        time.sleep(2)

        # 生成随机字符串
        def generate_random_str(randomlength=20):
            string.digits = '独立寒秋，湘江北去，橘子洲头。看万山红遍，层林尽染；漫江碧透，百舸争流。鹰击长空，鱼翔浅底，万类霜天'
            string.ascii_letters = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM!@#$%^&*()_+?><.//*\|'
            str_list = [random.choice(string.digits + string.ascii_letters) for i in range(randomlength)]
            random_str = ''.join(str_list)
            return random_str

        time.sleep(2)
        # 输入随机字符串
        driver.find_element_by_xpath('//*[@id="addUpdateProject"]/div[1]/div[1]/div/input').send_keys(generate_random_str())
        time.sleep(2)
        # 点击项目地址下拉框
        driver.find_element_by_id('province').click()
        # pro = Select(driver.find_element_by_id('province'))
        # pro.select_by_value('北京市')
        # pro = driver.find_element_by_tag_name('select')
        # ret = Select(pro).options
        # time.sleep(2)
        # ret = Select(pro).options
        # srant = random.Random().choice(ret[0:])
        # Select(pro).deselect_by_value(srant)
        model_xpath = '//*[@id="province"]/option[8]'
        # 点击选择设备型号
        driver.find_element_by_xpath(model_xpath).click()
        time.sleep(2)

        # 点击详细地址输入框
        driver.find_element_by_xpath('//*[@id="street"]').click()

        def generate_random_str(randomlength=20):
            string.digits = '风雨送春归，飞雪迎春到。已是悬崖百丈冰，犹有花枝俏。俏也不争春，只把春来报。待到山花烂漫时，她在丛中'
            string.ascii_letters = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM!@#$%^&*()_+?><.//*\|'
            str_list = [random.choice(string.digits + string.ascii_letters) for i in range(randomlength)]
            random_str = ''.join(str_list)
            return random_str

        # 输入详细地址随机字符串
        driver.find_element_by_xpath('//*[@id="street"]').send_keys(generate_random_str())
        time.sleep(2)
        # 点击行业选框
        driver.find_element_by_xpath('//*[@id="trade_chosen"]/a/span').click()
        js = 'document.querySelectorAll("select")[0].style.display="block";'
        driver.execute_script(js)
        # Requtype = driver.find_element_by_xpath('//*[@id="trade"]')
        # Requtypeoptions = Requtype.find_element_by_id('trade')
        # Select(Requtypeoptions).select_by_value('5')

        driver.find_element_by_xpath('//*[@id="trade_chosen"]/div/ul/li[3]').click()
        time.sleep(2)
