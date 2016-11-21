# coding=utf-8


# 面试题31：连续子数组的最大和

# 解法一：举例分析数组的规律
def find_greatest_sum_of_sub_array(data):
	max_sum = -float('inf')
	sum = 0
	for i in data:
		sum += i
		if sum < 0:
			sum = 0
		if max_sum < sum:
			max_sum = sum
	return max_sum


# 解法二：运用动态规划算法
def find_greatest_sum_of_sub_array2(data):
	length = len(data)
	pdata = [0]*length
	for i in range(length):
		if i == 0 or pdata[i-1] <= 0:
			pdata[i] = data[i]
		elif i != 0 and pdata[i-1] > 0:
			pdata[i] = pdata[i-1]+data[i]
	return max(pdata)

if __name__ == "__main__":
	print find_greatest_sum_of_sub_array([1, -2, 3, 10, -4, 7, 2, -5])
	print find_greatest_sum_of_sub_array2([1, -2, 3, 10, -4, 7, 2, -5])
