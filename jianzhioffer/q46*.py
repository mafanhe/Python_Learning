# coding:utf-8
# 面试题46：求1+2+...+n


# 解法一：利用构造函数求解
class Temp:
	n = 0
	sum = 0
	def __init__(self):
		Temp.n += 1
		Temp.sum += Temp.n


# 解法二：利用虚函数求解


# 解法三：利用函数作为参数求解
def solution3_teminator(n):
	return 0


def sum_solution3(n):
	fun = [solution3_teminator, sum_solution3]
	return n+fun[not not n](n-1)

# 解法四：利用模板类型求解

if __name__ == "__main__":
	# Temp()
	# [Temp()]*5
	# print Temp.sum

	print sum_solution3(3)




