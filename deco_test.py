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

def deco_with_arg(arg = True):
    if arg:
        def _deco(func):
            def wrapper(*args, **kwargs):
                starttime = int(time.time())
                func(*args, **kwargs)
                endtime = int(time.time())
                mesecs = (endtime - starttime)*1000
                print "->elapsed time: %f ms"%mesecs
            return wrapper
    else:
        def _deco(func):
            return func
    return _deco

@deco_with_arg(True)
def add_func(a, b):
    print 'start add'
    time.sleep(0.6)
    print 'result is %d'%(a+b)
    print 'end add'

if __name__ == '__main__':
    print "my_func is: ", my_func.__name__
    print ''
    my_func()

    add_func(4, 7)
