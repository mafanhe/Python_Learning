# coding=utf8

from collections import defaultdict


def counting_sort(A, key=lambda x: x):
	B, C = [], defaultdict(list)
	for x in A:
		C[key(x)].append(x)
	for k in range(min(C), max(C)):
		B.extend(C[k])
	return B

if __name__ == "__main__":
	# A = [1,4,2,5,3]
	# print counting_sort(A)
	print 'start'
	sorted([1,23,4,5,6,8])


