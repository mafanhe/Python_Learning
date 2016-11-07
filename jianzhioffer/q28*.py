# coding=utf-8


# 面试题28：字符串的排列
def permutation(input):
	permuta('', list(input))


def permuta(result, string):
	if len(string) == 0:
		print result
	for i in range(len(string)):
		string[i], string[0] = string[0], string[i]
		permuta(result+string[0], string[1:])


def permuta2(string, begin):
	# if begin==2:
	# 	print string
	if begin == 2:
		print string
		# return
	for i in range(begin, len(string)):
		string[i], string[begin] = string[begin], string[i]
		permuta2(string, begin+1)
		string[i], string[begin] = string[begin], string[i]


# permutation('abc')
permuta2(list('abc'), 0)