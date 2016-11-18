# coding=utf-8
# 面试题29： 数组中出现次数超过一半的数字

from procedure.Sort import partition

# 解法一：基于partition函数的O(n)算法
def more_than_half_num(numbers):
	if check_invalid_array(numbers):
		return 0
	length = len(numbers)
	middle = length>>1;
	start = 0
	end = length - 1
	index = partition(numbers, start, end)
	while index != middle:
		if index >middle:
			end = index - 1
			index = partition(numbers, start, end)
		else:
			start = index + 1
			index = partition(numbers, start, end)
	result = numbers[middle]
	if not check_more_than_half(numbers, result):
		result = 0
	return result


def check_invalid_array(numbers):
	if numbers is None and len(numbers) <= 0:
		return True


def check_more_than_half(numbers, number):
	times = 0
	for n in numbers:
		if n == number:
			times += 1
	return True if times*2<=len(numbers) else False


# 解法二: 根据数组特点找出O(n)的算法
def more_than_half_num2():
	pass
