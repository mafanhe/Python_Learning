# coding=utf-8


# 面试题28：字符串的排列
def permutation(input):
	permut('', list(input))


def permut(result, string):
	if len(string) == 0:
		print result
	for i in range(len(string)):
		string[i], string[0] = string[0], string[i]
		permut(result+string[0], string[1:])


def permut2(string, begin):

	if begin == 2:
		print string
		return
	for i in range(begin, len(string)):
		string[i], string[begin] = string[begin], string[i]
		permut2(string, begin+1)
		string[i], string[begin] = string[begin], string[i]


# 字符串的组合
def combination(com, left):
	print com
	if not left:
		return
	for i in range(len(left)):
		if left[i] in com:
			combination(com, left[i+1:])
		else:
			combination(com+left[i], left[i+1:])


# permutation('abc')
# permut2(list('abc'), 0)
combination('','abcd')