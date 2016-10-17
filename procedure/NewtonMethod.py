__author__ = 'mafanhe'

import math

def newton_method(a):
    x = a
    epsilon = 0.0000001
    while True:
        y = (x+a*1.0/x)/2
        if abs(y-x) < epsilon:
            return x

        x = y


def test_squre_root():
    print 'a', ' '*2, 'mysqrt(a)', ' '*4, 'math.sqrt(a)', 'diff'
    for i in range(1, 10):
        new_sqrt = newton_method(i)
        math_sqrt = math.sqrt(i)
        diff = new_sqrt-math_sqrt
        print i, new_sqrt, math.sqrt(i), diff


test_squre_root()