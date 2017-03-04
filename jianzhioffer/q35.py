# coding:utf-8

# 面试题35：第一个只出现一次的字符(创建简单哈希表)


# 嵌套循环 O(n^2)
def first_not_repeating_char(s):
	for i in range(len(s)):
		char = s[i]
		is_repeat = False
		for j in range(i+1, len(s)):
			if char == s[j]:
				is_repeat = True
				break
		if not is_repeat:
			return char


# 简单hash数组，遍历两边 O(n)
def first_not_repeating_char2(s):
	hashs = [0]*256
	for i in s:
		hashs[ord(i)] += 1
	print hashs
	for i in s:
		if hashs[ord(i)] == 1:
			return i

# print first_not_repeating_char('abaccdeff')


# 相关题目 1,2,3......
# 从第一个字符串中删除在第二个字符串中出现过的所有字符
def del_elements_in_sec_str(s1, s2):
	hh = [0]*256
	for i in s2:
		hh[ord(i)]=1
	for j in s1:
		if hh[ord(j)]:
			# del j
			pass
	return s1