# -*- coding: utf-8 -*-
# @Time    : 2018/9/6 16:53
# @Author  : xuyun

import re,string,random,time,unittest,sys,Method
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

        driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div[1]/div[1]/a').click()   # 添加设备
        time.sleep(1)

        driver.find_element_by_xpath('//*[@id="addDevice"]/div[1]/div').click()     # 点击设备类型选框
        time.sleep(1)

        # 百度了半个小时发现要把display=none设置为display=block设置为可见
        js = 'document.querySelectorAll("select")[0].style.display="block";'
        driver.execute_script(js)
        sel = driver.find_element_by_tag_name('select')
        # 选择value = 1也就是ap选项
        Select(sel).select_by_value('1')
        time.sleep(1)

        #  选择设备型号
        driver.find_element_by_xpath('//*[@id="model_auto_chosen"]/a/span').click()
        time.sleep(1)

        # 导入js方法把display设置为可见
        js = 'document.querySelectorAll("select")[0].style.display="block";'
        driver.execute_script(js)
        model_xpath = '//*[@id="model_auto_chosen"]/div/ul/li[' + str(random.randint(1,9)) + ']'
        time.sleep(2)
        # 点击选择设备型号
        driver.find_element_by_xpath(model_xpath).click()
        time.sleep(2)
        # 点击设备mac填写选项
        driver.find_element_by_xpath('//*[@id="mac"]').click()
        # 定义一个随机生成mac函数
        def randomMAC():
            mac = [0x52, 0x54, 0x00,
                   random.randint(0x00, 0x7f),
                   random.randint(0x00, 0xff),
                   random.randint(0x00, 0xff)]
            return ':'.join(map(lambda x: "%02x" % x, mac))
        print(randomMAC())
        # 填写设备mac
        driver.find_element_by_xpath('//*[@id="mac"]').send_keys(randomMAC())
        time.sleep(1)

        # 点击序列号填写框
        driver.find_element_by_xpath('//*[@id="serialNum"]').click()
        time.sleep(1)
        # 生成20长度的数字+字母组合随机字符串
        def generate_random_str(randomlength=20):
            string.digits = '0123456789'
            string.ascii_letters = 'DFGC'
            str_list = [random.choice(string.digits + string.ascii_letters) for i in range(randomlength)]
            random_str = ''.join(str_list)
            return random_str
        # 输入随机字符串
        driver.find_element_by_xpath('//*[@id="serialNum"]').send_keys(generate_random_str())
        time.sleep(2)

        # 点击位置信息输入框
        driver.find_element_by_xpath('//*[@id="positionDescription"]').click()
        def generate_random_str(randomlength=20):
            string.digits = '窗前明月光，疑是地上霜。举头望明月，低头思故乡'
            string.ascii_letters = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM!@#$%^&*()_+?><.//*\|'
            str_list = [random.choice(string.digits + string.ascii_letters ) for i in range(randomlength)]
            random_str = ''.join(str_list)
            return random_str
        driver.find_element_by_xpath('//*[@id="positionDescription"]').send_keys(generate_random_str())
        time.sleep(2)

        # 点击提交添加设备信息
        driver.find_element_by_xpath('//*[@id="addDevice"]/div[7]/div/input').send_keys(Keys.ENTER)
        time.sleep(2)

        # 查询并勾选全部设备
        driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/form/div[16]/button[3]').click()
        time.sleep(1)
        # 点击修改位置
        driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div[1]/div[1]/button[3]').click()
        time.sleep(1)
        # 生成随机字符串
        def generate_random_str(randomlength=20):
            string.digits = '西风烈，长空雁叫霜晨月，霜晨月，马蹄声碎，喇叭声咽。雄关漫道真如铁，而今迈步从头越，从头越，苍山如海，残阳如血'
            string.ascii_letters = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM!@#$%^&*()_+?><.//*\|'
            str_list = [random.choice(string.digits + string.ascii_letters) for i in range(randomlength)]
            random_str = ''.join(str_list)
            return random_str
        # 输入随机位置信息字符串
        driver.find_element_by_xpath('//*[@id="position"]').send_keys(generate_random_str())
        time.sleep(2)
        # 点击提交
        driver.find_element_by_xpath('//*[@id="updatePosition"]/div/div/div[3]/input').click()
        time.sleep(2)
        # 接受函数方法（确定)
        driver.switch_to.alert.accept()
        time.sleep(2)

        # 查询并勾选全部设备
        driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/form/div[16]/button[3]').click()
        time.sleep(1)
        # 点击修改描述
        driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div[1]/div[1]/button[4]').click()
        time.sleep(1)
        # 生成随机字符串
        def generate_random_str(randomlength=20):
            string.digits = '北国风光，千里冰封，万里雪飘,望长城内外，惟馀莽莽；大河上下，顿失滔滔。山舞银蛇，原驰蜡象，欲与天公试比高。须晴日，看红妆素裹，分外妖娆'
            string.ascii_letters = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM!@#$%^&*()_+?><.//*\|'
            str_list = [random.choice(string.digits + string.ascii_letters) for i in range(randomlength)]
            random_str = ''.join(str_list)
            return random_str
        # 输入描述信息随机字符串
        driver.find_element_by_xpath('//*[@id="description"]').send_keys(generate_random_str())
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="updateDescription"]/div/div/div[3]/input').click()
        # 接受函数方法(确定)
        alert = driver.switch_to_alert()
        alert.accept()
        time.sleep(2)
        # 打开终端管理
        driver.find_element_by_xpath('//*[@id="treeMenu"]/li[2]/a/span').click()
        time.sleep(2)
        # 点击项目开局
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
        #点击项目地址下拉框
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
        driver.find_element_by_xpath('//*[@id="trade_chosen"]/div/ul/li[3]').click()
        time.sleep(2)
        # 点击输入项目标识
        driver.find_element_by_xpath('//*[@id="addUpdateProject"]/div[1]/div[6]/div/input').click()
        driver.find_element_by_xpath('//*[@id="addUpdateProject"]/div[1]/div[6]/div/input').send_keys(generate_random_str())
        time.sleep(2)
        # 点击输入项目描述
        driver.find_element_by_xpath('//*[@id="addUpdateProject"]/div[1]/div[7]/div/textarea').click()
        driver.find_element_by_xpath('//*[@id="addUpdateProject"]/div[1]/div[7]/div/textarea').send_keys(generate_random_str())
        time.sleep(2)
        # 点击输入客户密码
        driver.find_element_by_xpath('//*[@id="addUpdateProject"]/div[1]/div[9]/div/input').click()
        driver.find_element_by_xpath('//*[@id="addUpdateProject"]/div[1]/div[9]/div/input').send_keys(Method.generate_random_int())
        time.sleep(2)
        # 点击输入客户名称
        driver.find_element_by_xpath('//*[@id="addUpdateProject"]/div[1]/div[10]/div/input').click()
        driver.find_element_by_xpath('//*[@id="addUpdateProject"]/div[1]/div[10]/div/input').send_keys(Method.generate_random_numbers())
        time.sleep(2)
        # 点击输入联系人
        driver.find_element_by_xpath('//*[@id="addUpdateProject"]/div[1]/div[11]/div/input').click()
        driver.find_element_by_xpath('//*[@id="addUpdateProject"]/div[1]/div[11]/div/input').send_keys(generate_random_str())
        time.sleep(2)
        # 点击输入客户电话
        driver.find_element_by_xpath('//*[@id="addUpdateProject"]/div[1]/div[12]/div/input').click()
        driver.find_element_by_xpath('//*[@id="addUpdateProject"]/div[1]/div[12]/div/input').send_keys(generate_random_str())
        time.sleep(2)
        # 点击输入客户邮箱
        driver.find_element_by_xpath('//*[@id="addUpdateProject"]/div[1]/div[13]/div/input').click()
        driver.find_element_by_xpath('//*[@id="addUpdateProject"]/div[1]/div[13]/div/input').send_keys('1@1.com')
        # 选择客户地址
        # pro = Select(driver.find_element_by_id('province'))
        # pro.select_by_value('北京市')
        # pro = driver.find_element_by_tag_name('select')
        # ret = Select(pro).options
        # time.sleep(2)
        # ret = Select(pro).options
        # srant = random.Random().choice(ret[0:])
        # Select(pro).deselect_by_value(srant)
        # 选择客户地址
        time.sleep(2)
        pro = Select(driver.find_element_by_class_name('form-control'))
        ret = Select(pro).options
        srant = random.Random().choice(ret[0:])
        Select(pro).deselect_by_value(srant)
        driver.find_element_by_xpath('//*[@id="addUpdateProject"]/div[1]/div[15]/div/input').click()
        driver.switch_to_alert()
        time.sleep(2)




        driver.find_element_by_xpath('//*[@id="treeMenu"]/li[4]/a').click()
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="treeMenu"]/li[5]/a/span').click()
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="treeMenu"]/li[6]/a/span').click()
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="treeMenu"]/li[7]/a/span').click()
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="treeMenu"]/li[8]/a/span').click()
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="treeMenu"]/li[9]/a/span').click()
        time.sleep(3)
        # self.assertIn('DC',driver.title)
        # elem = driver.find_element_by_class_name('username')
        # elem.send_keys('Xadmin')
        # elem.send_keys(Keys.RETURN)
        # assert 'no results found.'not in driver.page_source
    def tearDown(self):
        self.drviet.quit()
if __name__ == '__main__':
    unittest.main()




