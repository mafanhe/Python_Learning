import sys
import math
def count(a):
    res = []
    r = int(math.sqrt(a))
    for i in range(0,r+1):
        b = math.sqrt(a-i**2)
        if b==int(b):
            res.append([i,b])

    sum = 0
    for r in res:
        if r[0]!=0 and r[1]!=0:
           sum+=4
        else:
            sum+=2
    print sum
a = int(raw_input())
count(a)

