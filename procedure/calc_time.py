# coding=utf-8

'''
计算函数运行时间的装饰函数
'''

import time
import functools

def calc_time(fn):
    def _wrapper(*args, **kwargs):
        start = time.time()
        fn(*args, **kwargs)
        print "%s cost %s second" % (fn.__name__,str(time.time()-start))
    return _wrapper

# def time_me(info="used"):
#     def _time_me(fn):
#         @functools.wraps(fn)
#         def _wrapper(*args,**kwargs):
#             start = time.clock()
#             fn(*args,**kwargs)
#             print "%s %s %f"%(fn.__name__,info,time.clock()-start),"second"
#         return _wrapper
#     return _time_me
def time_me(fn):
    @functools.wraps(fn)
    def _wrapper(*args,**kwargs):
        start = time.time()
        fn(*args,**kwargs)
        print "%s %f"%(fn.__name__,time.time()-start),"second"
    return _wrapper

@calc_time
def test(x):
    time.sleep(3)

@time_me
def test2(x):
    time.sleep(0.1)

# test(1)
# print test.__name__
# test2(1)
# print test2.__name__


# n1=time.time()
# time.sleep(2)
# n2=time.time()
# print (n2-n1)