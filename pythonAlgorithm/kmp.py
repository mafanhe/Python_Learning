def index(pstr, subStr):
	i, j = 0, 0
	while i<len(pstr) and j<len(subStr):
		if pstr[i] == subStr[j]:
			i += 1
			j += 1
		else:
			i = i-j+1
			j = 0
	return i-len(subStr) if j==len(subStr) else -1
	# if j>=len(subStr):
	# 	print True
	# else:
	# 	print False


def kmp(pstr, subStr):
	i, j = 0, 0
	while i < len(pstr) and j < len(subStr):
		# print i,j
		if pstr[i] == subStr[j]:
			i += 1
			j += 1
		else:
			if j == 0:
				i += 1
			else:
				j = bulidNext(subStr)[j-1]+1

	return i - len(subStr) if j == len(subStr) else -1


def bulidNext(strs):
	next = [-2 for i in range(len(strs))]
	j = 0
	k = -1
	next[0] = -1
	while j < len(strs) - 1:
		if k == -1 or strs[j] == strs[k]:
			j += 1
			k += 1
			next[j] = k
		else:
			k = next[k]
	return next

	# if j >= len(subStr):
	# 	print True
	# else:
	# 	print False


a = "ababcabcacbab"
b = "abcac"
c = "abaabcac"
print c
print bulidNext(c)
# print kmp(a, b)
a="abc"
a.find()