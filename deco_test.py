#!/usr/bin/python
# -*- coding:utf-8 -*-

import time

def deco(func):
    def wrapper():  #避免计时功能对my_func函数调用代码的影响
        starttime = int(time.time())
        func()
        endtime = int(time.time())
        mesecs = (endtime - starttime)*1000
        print "->elapsed time: %f ms"%mesecs
    return wrapper

@deco
def my_func():
    print 'my_func start'
    time.sleep(0.6)
    print 'my_func end'

if __name__ == '__main__':
    print "my_func is: ", my_func.__name__
    print ''
    my_func()
