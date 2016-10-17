# coding=utf-8

# 插入排序递归实现
def ins_sort_rec(seq,i):
	if i == 0:
		return
	ins_sort_rec(seq, i-1)
	j = i
	while j > 0 and seq[j-1] > seq[j]:
		seq[j-1], seq[j] = seq[j], seq[j-1]
		j -= 1

# 插入排序循环实现
def ins_sort(seq):
	for i in range(1, len(seq)):
		j = i
		while j > 0 and seq[j-1] > seq[j]:
			seq[j - 1], seq[j] = seq[j], seq[j - 1]
			j -= 1



l = [6,3,5,4,1,2]
l2 = l[:]
ins_sort(l2)
print l2