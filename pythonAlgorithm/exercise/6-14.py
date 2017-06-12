# coding=utf-8
import random

def partition(l, left, right, key):
	i, j = left, right
	k = seq[i]
	while i < j:
		while i < j and key(l[j]) >= key(k):
			j -= 1
		l[i] = l[j]
		while i < j and key(l[i]) <= key(k):
			i += 1
		l[j] = l[i]
	l[i] = k
	return i


def quick_sort(seq, left, right, key):
	if left < right:
		q = partition(seq,left,right,key)
		# print left, right, q
		quick_sort(seq, left,q-1,key)
		quick_sort(seq, q+1, right, key)
	return seq


def sort(seq,key=None):
	if key is None:
		key = lambda x:x
	quick_sort(seq,0,len(seq)-1,key)


if __name__ == "__main__":
	# seq = [random.randint(0,100) for i in range(10)]
	seq = [[random.randint(0,100),random.randint(0,100)] for i in range(10)]
	l=[60, 27, 58, 20, 31, 16, 90, 41, 57, 20]
	# q = l[:]
	# print seq
	# quick_sort(l,0,9)
	print seq
	sort(seq,key=lambda x:x[-1])

	print seq
	# print q