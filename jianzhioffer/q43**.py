# coding:utf-8
# 面试题43：n个


# 方法一：基于递归求骰子点数
def print_probability(number):
	global g_maxValue
	max_sum = number * g_maxValue
	pProbabilities = [0] * (max_sum - number + 1)
	probability(number, pProbabilities)
	total = pow(g_maxValue, number)
	for i in range(number, max_sum+1):
		ratio = pProbabilities[i-number]*1.0/total
		print "%d: %.2f\n" % (i, ratio)


def probability(number, pProbabilites):
	for i in range(g_maxValue):
		probability2(number, number, i, pProbabilites)


def probability2(original, current, _sum, pProbabilites):
	if current == 1:
		pProbabilites[_sum-original] += 1
	else:
		for i in range(g_maxValue):
			probability2(original, current-1, i+_sum, pProbabilites)


# 方法二：基于循环求骰子点数
def print_probability(number):
	global g_maxValue
	if number < 1:
		return
	pProbability = [[0]*(g_maxValue*number+1), [0]*(g_maxValue*number+1)]
	flag = 0
	for i in range(1, g_maxValue+1):
		pProbability[i] = 1
	for k in range(2, number+1):
		for i in range(k):
			pProbability[1-flag][i] = 0
		for i in range(k, g_maxValue*k+1):
			pProbability[1-flag][i] = 0
			j = 1
			while j <= i and j <= g_maxValue:
				pProbability[1-flag][i] += pProbability[flag][i-j]
				j += 1
		flag = 1 - flag
	total = pow(g_maxValue, number)
	for i in range(number, g_maxValue*number+2):
		ratio = pProbability[flag][i]*1.0 / total
		print "%d: %e\n" % (i, ratio)


if __name__ == "__main__":
	g_maxValue = 6
	print_probability(2)
