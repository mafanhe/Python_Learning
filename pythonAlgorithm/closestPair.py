# coding=utf-8
from random import randint,random,randrange
from math import sqrt


# 一维的情况
def partition(seq,left,right,key=lambda x:x):
	m = (key(min(seq[left:right+1],key=key))+key(max(seq[left:right+1],key=key)))/2
	while left < right:
		while left < right and key(seq[left]) <= m:
			left += 1
		while left < right and key(seq[right]) > m:
			right -= 1
		seq[left], seq[right] = seq[right], seq[left]
	return left-1


def c_pair(seq,left,right):
	min_d = [9999,0,0]
	if right-left<1:
		return min_d
	i = partition(seq,left,right)
	d1, d2 = c_pair(seq,left,i), c_pair(seq,i+1,right)
	Max, Min = max(seq[left:i+1]), min(seq[i+1:right+1])
	d1d2 = [Min-Max,Max,Min]
	if d1[0]<d2[0]:
		if d1d2[0]<d1[0]:
			return d1d2
		else:
			return d1
	else:
		if d1d2[0]<d2[0]:
			return d1d2
		else:
			return d2

def distance(p1, p2):
	return sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)


# 二维情况
def c_pair2(seq, left, right):
	min_d = [9999,0,0,0,0]
	if right - left < 1:
		return min_d
	if right - left == 1:
		return [distance(seq[left],seq[right]),seq[left][0],seq[left][1],seq[right][0],seq[right][1]]
	i = partition(seq, left, right,key=lambda x:x[0])
	l = (left + right)/2
	d1, d2 = c_pair2(seq, left, i), c_pair2(seq, i+1, right)
	min_d = d1 if d1[0]<d2[0] else d2
	array1 = [s for s in seq[left:i+1] if l-s[0] < min_d[0]]
	array2 = [[x for x in seq[i+1:right+1] for y in array1 if (x[1]-y[1]) < min_d[0] < x[0]-l]]
	for a,bs in zip(array1,array2):
		for b in bs:
			dis_ab = distance(a, b)
			if dis_ab<min_d[0]:
				min_d=[dis_ab,a[0],a[1],b[0],b[1]]
	return min_d





if __name__ == "__main__":
	# 尝试画二维坐标！！！！！！
	# seq2 = [randrange(0,1000,1) for i in range(10)]
	seq3 = [[random(),random()] for i in range(10)]
	seq3 = [[randint(0,10),randint(0,10)]for i in range(10)]
	# print seq2
	print seq3
	# seq = [5,50,9,70,15,0,30,20]
	# i = partition(seq,0,9)
	# print i,seq
	# print c_pair(seq2,0,9)
	print c_pair2(seq3,0,9)