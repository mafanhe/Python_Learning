import math

n = int(raw_input())
l = [int(i) for i in raw_input().strip().split()]
l.sort()
length = len(l)
m = math.ceil(length/3.0)
print int(m*3-length)

