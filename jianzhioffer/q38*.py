# coding:utf-8
# 面试题38：数字在排序数组中出现的次数


# 获取数组中的第一个k
def get_first_k(data, k, start, end):
	if start > end:
		return -1
	mid = (start + end) / 2
	mid_data = data[mid]
	if mid_data == k:
		if mid > 0 and data[mid-1] != k or mid == 0:
			return mid
		else:
			end = mid - 1

	if mid_data < k:
		start = mid + 1
	else:
		end = mid - 1
	return get_first_k(data, k, start, end)


# 获取数组中的第二个k
def get_last_k(data, k, start, end):
	if start > end:
		return -1
	mid = (start + end) / 2
	mid_data = data[mid]
	if mid_data == k:
		if mid < len(data)-1 and data[mid+1] != k or mid == len(data)-1:
			return mid
		else:
			start = mid +1

	elif mid_data < k:
		start = mid + 1
	else:
		end = mid - 1
	return get_last_k(data, k, start, end)


# 计算k在数组中出现的次数
def get_number_of_k(data, k):
	number = 0
	if data and len(data) > 0:
		first = get_first_k(data, k, 0, len(data)-1)
		last = get_last_k(data, k, 0, len(data)-1)
		if first>-1 and last>-1:
			number = last - first + 1
	return number

if __name__ == "__main__":
	s = [1, 2, 3, 3, 3, 3, 3, 4, 5, 6, 7]
	print get_number_of_k(s, 3)

