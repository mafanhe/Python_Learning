# coding:utf-8
# 面试题36：数组中的逆序对


# 类似归并排序的计算
def inverse_pairs(data):
	length = len(data)
	if not data and length < 0:
		return 0
	copy = data[:]
	count = inverve_pairs_core(data, copy, 0, length-1)
	print data, copy
	return count


def inverve_pairs_core(data, copy, start, end):
	if start == end:
		copy[start] = data[start]
		return 0

	length = (end - start) / 2
	# left = inverve_pairs_core(data, copy, start, start+length)
	left = inverve_pairs_core(copy, data, start, start+length)
	# right = inverve_pairs_core(data, copy, start+length+1, end)
	right = inverve_pairs_core(copy, data, start+length+1, end)

	# i初始化为前半端最后一个数字的下标
	i = start + length
	# j 初始化为后半段最后一个数字的下标
	j = end
	indexCopy = end
	count = 0
	while i >= start and j >= start+length+1:
		if data[i] > data[j]:
			copy[indexCopy] = data[i]
			count += j - start - length
			i -= 1
		else:
			copy[indexCopy] = data[j]
			j -= 1
		indexCopy -= 1
	while i >= start:
		copy[indexCopy] = data[i]
		indexCopy -= 1
		i -= 1

	while j >= start+length+1:
		copy[indexCopy] = data[j]
		indexCopy -= 1
		j -= 1
	return left + right + count


if __name__ == "__main__":
	print inverse_pairs([7, 5, 6, 4])
