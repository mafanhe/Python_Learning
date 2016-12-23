# coding:utf-8
# 面试题42：翻转单词顺序VS左旋转字符串


# 题目一：翻转一个英文句子，翻转句子中单词的顺序，但单词内字符的顺序不变。
def reverse(data, begin, end):
	while begin < end:
		data[begin], data[end] = data[end], data[begin]
		begin += 1
		end -= 1


def reverse_sentence(data):
	data = list(data)
	reverse(data, 0, len(data)-1)
	begin = 0
	end = 0
	for i in data:
		if i == ' ':
			if end-begin > 1:
				reverse(data, begin, end-1)
			end += 1
			begin = end
		else:
			end += 1
	return "".join(data)


# 字符串的左旋转操作是把字符串前面的若干个字符转移到字符串的尾部
def left_rotate_string(pstr, n):
	if pstr and len(pstr) > 0 and 0 < n < len(pstr):
		pstr = list(pstr)
		reverse(pstr, 0, n - 1)
		reverse(pstr, n, len(pstr) - 1)
		reverse(pstr, 0, len(pstr) - 1)
	return "".join(pstr)

if __name__ == "__main__":
	# a = 'i am a student.'
	# print reverse_sentence(a)
	b = 'abcdefg'
	print left_rotate_string(b, 2)