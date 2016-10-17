# coding=utf-8


# 选择排序递归实现
def sel_sort_rec(seq, i):
	if i == 0: return
	max_j = i
	for j in range(i):
		if seq[j]>seq[max_j]:
			max_j = j
	seq[max_j], seq[i] = seq[i], seq[max_j]
	sel_sort_rec(seq, i-1)


# 选择排序循环实现
def sel_sort(seq):
	for i in range(len(seq)-1,0,-1):
		max_j = i
		for j in range(i):
			if seq[j]>seq[max_j]:
				max_j = j
		seq[max_j], seq[i] = seq[i], seq[max_j]

l = [6,2,4,5,1,3]
sel_sort(l)
print l