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


def time_me(times=1):
    def _time_me(fn):
        @functools.wraps(fn)
        def _wrapper(*args,**kwargs):
            start = time.time()
            for i in xrange(times):
                fn(*args,**kwargs)
            print "%s cost %f"%(fn.__name__,time.time()-start),"second"
        return _wrapper
    return _time_me
# def time_me(fn,times=50):
#     @functools.wraps(fn)
#     def _wrapper(*args,**kwargs):
#         start = time.time()
#         for i in xrange(times):
#             fn(*args,**kwargs)
#         print "%s complete %d times, and cost %f"%(times,fn.__name__,time.time()-start),"second"
#     return _wrapper


@calc_time
def test(x):
    time.sleep(1)



@time_me(4)
def test2(x):
    time.sleep(1)

if __name__ == "__main__":
    test(1)
    # print test.__name__
    test2(1)
    # print test2.__name__


    # n1=time.time()
    # time.sleep(2)
    # n2=time.time()
    # print (n2-n1)