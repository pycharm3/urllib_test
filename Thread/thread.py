# -*- coding: utf-8 -*-
# @Time    : 2018/10/9 16:19
# @Author  : xuyun
import _thread
from time import sleep,ctime
loopes = [4,2]
def loopr0(nloop, nsec, lock) :
    print('我是a: ',ctime())
    sleep(nsec)
    print('我是a1: ',ctime())
    lock
def loopr1() :
    print('我是b: ',ctime())
    sleep(2)
    print('我是b1: ',ctime())
def main() :
    print('我是c: ',ctime())
    _thread.start_new_thread(loopr0, ())
    _thread.start_new_thread(loopr1, ())
    sleep(6)
    print('我是d: ',ctime())
if __name__ == '__main__' :
    main()