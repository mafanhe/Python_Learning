# coding:utf-8

import random
from collections import defaultdict


# 生成随机无重复序列
def generate_random_sequence(n):
	a = range(n)
	right = n-1
	for i in range(n-1):
		randindex = random.randint(0,right)
		a[randindex], a[right] = a[right], a[randindex]
		right -= 1
	return a


def generate_DAG(n=5):
	random_seq = generate_random_sequence(n)
	seq = [chr(97+_) for _ in random_seq]
	print seq
	res = defaultdict(set)
	for i in range(n-1):
		res[seq[i]].add(seq[i+1])
	res[seq[n-1]] = set()
	print res
	for i in range(n-1):
		for j in range(i+1, n):
			if random.randint(0,1):
				res[seq[i]].add(seq[j])

	print res
	return res

if __name__ == "__main__":
	G = generate_DAG(10)
	from pythonAlgorithm import topsort
	print topsort.topsort(G)
	print topsort.topsort2(G)
	# print generate_random_sequence(5)