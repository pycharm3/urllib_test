# -*- coding: utf-8 -*-
# @Time    : 2018/9/3 17:41
# @Author  : xuyun

import requests
import json
import cookiejar
import random
# url = 'http://10.0.0.9:8080/om/monitor/device/info/a4:fb:8d:04:14:19?deviceType=1'
# r = requests.get(url)   # 返回值放r里边
# print(r.status_code)    # status_code 输出状态码
# print(r.content)        # content 输出值

# content = {'username':'Xadmin','password':'123456'}
# str_con = json.dumps(content)   # 把content转换为json str格式
# print(str_con)
# print(type(str_con))
# r = requests.post('http://10.0.0.9:8080/login',data=content)
# print(r.status_code)
# print(r.content)
#
# content = json.loads(str_con)    # 把str_con转换为dict 格式
# print(str_con)
# print(type(content))

url = 'http://10.0.0.9:8080/login'
da = {'username':'Xadmin','password':'123456'}
re = requests.post(url)
c = re.cookies                          # 为转为str类型前获取请求的cookie，类型转变后就无法获取了
print(c)                                # 打印请求的cookie
req = requests.post(url,data=da)        # 转变类型
print(req.status_code)                  # 打印请求状态
print(req.url,'\n')                     # 打印请求后的url

url = 'http://10.0.0.9:8080/om/device/add'
a = {'1':'s'}
da = {'deviceType':'1',
       'model':'WA722M-E',
       'protocol':'capwap',
       'mac':'A4:FB:8D:03:09:4d',
       'serialNum':'D0268010022F150601522',
       'positionDescription':''}
for key,value in da.items() :       # 把参数遍历出来以备后用
    print(key+ ':' +value,'\n')
    if key == 'mac' :
        value = random.shuffle(value)   # 把value变为无序状态
        print(da)



    # if value == () :
    #
    #     print('测试')

print('\n')
headers = {
        'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding' : 'gzip, deflate',
        'Accept-Language' : 'zh-CN,zh;q=0.9',
        'Cache-Control' : 'max-age=0',
        'Cookie': 'JSESSIONID=4EAA39F7CE707957C5665F8FAA502BD3',
        'Host' : '10.0.0.9:8080',
        'Proxy-Connection': 'keep-alive',
        'Referer' : 'http://10.0.0.9:8080/om/inventory/device/list',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
}

re = requests.post(url)
c = re.cookies
print(c,'\n')           # 打印一下为装换字符类型前的cookie可惜不晓得为啥打印为空

req = requests.post(url,json=url,headers=headers, data=da)
print(req.status_code)
print(req.url)

