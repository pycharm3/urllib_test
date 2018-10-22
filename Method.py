# -*- coding: utf-8 -*-
# @Time    : 2018/9/17 16:43
# @Author  : xuyun

import re,string,random,time,unittest,sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

def generate_random_str(randomlength=20):
    string.digits = '西风烈，长空雁叫霜晨月，霜晨月，马蹄声碎，喇叭声咽。雄关漫道真如铁，而今迈步从头越，从头越，苍山如海，残阳如血'
    string.ascii_letters = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM!@#$%^&*()_+?><.//*\|'
    str_list = [random.choice(string.digits + string.ascii_letters) for i in range(randomlength)]
    random_str = ''.join(str_list)
    return random_str

def generate_random_int(randomlength=6):
    string.digits = '西风烈，长空雁叫霜晨月，霜晨月，马蹄声碎，喇叭声咽。雄关漫道真如铁，而今迈步从头越，从头越，苍山如海，残阳如血'
    string.ascii_letters = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM123456789'
    str_list = [random.choice(string.ascii_letters) for i in range(randomlength)]
    random_str = ''.join(str_list)
    return random_str

def generate_random_numbers(randomlength=10):
    string.digits = '西风烈，长空雁叫霜晨月，霜晨月，马蹄声碎，喇叭声咽。雄关漫道真如铁，而今迈步从头越，从头越，苍山如海，残阳如血'
    string.ascii_letters = '123456789'
    str_list = [random.choice(string.ascii_letters) for i in range(randomlength)]
    random_str = ''.join(str_list)
    return random_str

def generate_random_NS(randomlength=20):
    string.ascii_letters = '123456789DQWERASG'
    str_list = [random.choice(string.ascii_letters) for i in range(randomlength)]
    random_str = ''.join(str_list)
    return random_str


def randomMAC():
    mac = [0x52, 0x54, 0x00,
           random.randint(0x00, 0x7f),
           random.randint(0x00, 0xff),
           random.randint(0x00, 0xff)]
    return '-'.join(map(lambda x: "%02x" % x, mac))
print(randomMAC())