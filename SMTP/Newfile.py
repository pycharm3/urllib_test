# -*- coding: utf-8 -*-
# @Time    : 2018/9/28 16:33
# @Author  : xuyun
import os,datetime,time
result_dir = 'D://'
lists = os.listdir(result_dir)
lists.sort(key=lambda fn:   os.path.getatime(result_dir+'//'+fn)
                                             if not os.path.isabs(result_dir + '//' + fn) else 0)
print('最新的测试报告为: ' + lists[-1])
file = os.path.join(result_dir, lists[-1])
print(file)