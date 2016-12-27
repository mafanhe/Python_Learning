# coding:utf-8
# 面试题44：扑克牌的顺子


def is_continues(numbers):
	numbers.sort()
	zeros = 0
	gaps = 0
	for i in numbers:
		if i == 0:
			zeros += 1
	for j in range(zeros,len(numbers)-1):
		gap = numbers[j+1] - numbers[j]
		if gap == 0:
			return False
		else:
			gaps += gap-1
	return True if gaps <= zeros else False


if __name__ == "__main__":
	data=[1,2,3,4,5]
	data=[1,2,3,4,6]
	data=[5,4,3,2,0]
	data=[5,6,2,3,0]
	print is_continues(data)