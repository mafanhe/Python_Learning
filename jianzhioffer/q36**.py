# coding:utf-8
# 面试题36：数组中的逆序对


def inverse_pairs(data):
	length = len(data)
	if not data and length < 0:
		return 0
	copy = data[:]
	count = inserve_pairs_core(data, copy, 0, length-1)
	return count


def inserve_pairs_core(data, copy, start, end):
	if start == end:
		copy[start] = data[start]
		return 0

	length = (start + end) / 2
	left = inserve_pairs_core(copy, data, start, start+length)
	right = inserve_pairs_core(copy, data, start+length+1, end)

	# i初始化为前半端最后一个数字的下标
	i = start + length
	# j 初始化为后半段最后一个数字的下标
	j = end
	indexCopy = end
	count = 0
	while i >= start and j >= start+length+1:
		if data[i] > data[j]:
			copy[indexCopy] = data[i]
			i -= 1
		else:
			copy[indexCopy] = data[j]
			j -= 1
		indexCopy -= 1
	for x in range(i, start-1, -1):
		copy[indexCopy] = data[x]
		indexCopy -= 1

	for y in range(j, start+length+1, -1):
		copy[indexCopy] = data[y]
		indexCopy -= 1
	return left + right + count
