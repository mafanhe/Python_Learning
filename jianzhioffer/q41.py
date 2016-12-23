# coding:utf-8
# 面试题41：和为s的两个数字VS和为s的连续正数序列


def find_numbers_with_sum(data, sum):
	if not data or len(data) < 2:
		return None
	left = 0
	right = len(data)-1
	while left<right:
		_sum = data[left] + data[right]
		if _sum == sum:
			break
		elif _sum > sum:
			right -= 1
		else:
			left += 1
	return data[left], data[right]


def find_continuous_sequence(data, sum_):
	result = []
	res = []
	i = 0
	while i <= len(data):
		_sum = sum(res)
		if _sum == sum_:
			result.append(res[:])
			if i >= len(data):
				break
			res.pop(0)
			res.append(data[i])
			i+=1
		elif _sum > sum_:
			res.pop(0)
		elif i<len(data):
			res.append(data[i])
			i += 1
		else:
			break
	return result


# 书中例子
def find_continuous_sequence2(sum_):
	if sum < 3:
		return
	small, big, middle = 1, 2, (1+sum_)/2
	cur_sum = small+big
	while small < middle:
		if cur_sum == sum_:
			print range(small, big+1)
		while cur_sum > sum_ and small < middle:
			cur_sum -= small
			small += 1
			if cur_sum == sum_:
				print range(small, big+1)
		big += 1
		cur_sum += big


if __name__ == "__main__":
	data = [1, 2, 4, 7, 11, 15]
	data2 = [1, 2, 3, 4, 5, 6, 7, 8]
	# print find_numbers_with_sum(data,6)
	# print find_continuous_sequence(data2, 9)
	print find_continuous_sequence2(9)