# coding=utf-8


# A:1,B:2,...,Z:26
# AA:27,AB:28,...,BA:53,...
# AAA:703
def calc_num(num):
    res = 0
    for i in range(len(num)-1,-1,-1):
        res = res+26**(len(num)-1-i)*(ord(num[i])-64)
        print res
    return res
# print calc_num("BA")


# 不可以对负数作操作，会出现死循环
def numberof1(n):
    count = 0
    while n:
        if n & 1:
            count += 1
        n >>= 1
    return count


# 循环次数为数字位数
def numberof1_2(n):
    count = 0
    flag = 1
    while flag <= abs(n):
        if n & flag:
            count += 1
        flag <<= 1
    return count


# 循环次数为数字1的个数
# 把一个整数减去1之后再和原来的整数做位与运算，
# 得到的结果相当于是把整数的二进制表示中的最右边一个1变成0
def numberof1_3(n):
    count = 0
    while n:
        count += 1
        n &= n-1
    return count

# print numberof1(int('1011001',2))
# print numberof1_2(int('1011001',2))
# print numberof1_3(int('1011111',2))


# 判断一个整数是不是2的整数次方
def xgtm(n):
    n &= n-1
    if n:
        return False
    return True

# print xgtm(8)


def xgtm2(m, n):
    s = m ^ n
    return numberof1_3(s)

# print xgtm2(10, 13)

