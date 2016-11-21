# coding=utf-8

# 面试题33：把数组排成最小的数


def mycmp(x, y):
		return cmp((x+y),(y+x))


def PrintMinNumber(numbers):
	return ''.join(sorted([str(n) for n in numbers], mycmp))



