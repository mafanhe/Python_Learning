# coding:utf-8
# 面试题47：不用加减乘除做加法


def add(m, n):
	while True:
		sum_ = m ^ n
		carry = (m & n) << 1
		m = sum_
		n = carry
		if n == 0:
			return m


# 递归版本
def add2(m, n):
	if n == 0:
		return m
	return add2(m ^ n, (m & n) << 1)


# 更短的代码版本
def add3(m, n):
	return m if not n else add3(m ^ n, (m & n) << 1)


# 相关问题：不使用新变量，交换两个变量的值。
# 方法一：基于加减法
a, b = 1, 2
a = a + b
b = a - b
a = a - b
# 方法二：基于亦或运算
a = a ^ b
b = a ^ b
a = a ^ b

if __name__ == "__main__":
	print add3(5, 7)

