# coding=utf-8
from random import randint,random,randrange


# 一维的情况
def partition(seq,left,right):
	m = (min(seq[left:right+1])+max(seq[left:right+1]))/2
	while left<right:
		while left<right and seq[left]<=m:
			left += 1
		while left<right and seq[right]>m:
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


# 二维情况
def funciton():
	pass


if __name__ == "__main__":
	seq2 = [randrange(0,1000,1) for i in range(10)]
	print seq2
	seq = [5,50,9,70,15,0,30,20]
	# i = partition(seq,0,9)
	# print i,seq
	print c_pair(seq2,0,9)