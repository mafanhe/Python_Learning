# coding=utf-8

# 题目8：旋转数组最小值
def mini(l):
    index1 = 0
    index2 = len(l)-1
    while index2-index1!=1:
        mid = (index1 + index2) / 2
        if l[mid]>l[index1]:
            index1 = mid
        else:
            index2 = mid
    print l[index2]

l = [3,4,5,6,1,2,2,3]
mini(l)