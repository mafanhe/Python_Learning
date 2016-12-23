# coding:utf-8
# 面试题40：数组中只出现一次的数字


# 亦或
def find_nums_appear_once(data):
	result_or = reduce(lambda x, y: x ^ y, data)
	bin_res = bin(result_or)
	index = len(bin_res)-1-bin_res.index('1')
	a, b = [], []
	for i in data:
		bin_i = bin(i)
		if bin_i[len(bin_i)-1-index] == '1':
			a.append(i)
		else:
			b.append(i)
	num1 = reduce(lambda x, y: x ^ y, a)
	num2 = reduce(lambda x, y: x ^ y, b)
	return num1, num2

if __name__ == "__main__":
	data = [2, 4, 3, 6, 3, 2, 5, 5]
	print find_nums_appear_once(data)
