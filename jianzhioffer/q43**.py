# coding:utf-8
# 面试题43：n个


def print_probability(number):
	global g_maxValue
	max_sum = number * g_maxValue
	pProbabilities = [0] * (max_sum - number + 1)
	probability(number, pProbabilities)
	pass


def probability(number, pProbabilites):
	for i in range(g_maxValue):
		probability2(number, number, i, pProbabilites)


def probability2(original, current, _sum, pProbabilites):
	if current == 1:
		pProbabilites[_sum-original] += 1
	else:
		for i in range(g_maxValue):
			probability2(original, current-1, i+_sum, pProbabilites)

if __name__ == "__main__":
	g_maxValue = 6
	print_probability(2)
