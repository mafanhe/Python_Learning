# coding=utf-8

# 面试题32：从1到n整数中1出现的次数


# 解法一：不考虑时间效率的解法
def number_of_between_and_n(n):
	number = 0
	for i in range(1, n+1):
		number += number_of_1(i)
	return number


def number_of_1(i):
	number = 0
	while i:
		if i%10 == 1:
			number += 1
		i /= 10
	return number


# 解法二：数字规律题***
def number_of_between_and_n2(n):
	"""
	1:1
	2:19
	3:
	"""
	if n < 0:
		return 0
	return number_of_1(str(n))


# see page 176
def number_of_1_2(n):
	pass


if __name__ == "__main__":
	print number_of_between_and_n(12)
