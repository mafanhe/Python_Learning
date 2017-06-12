# coding=utf-8
from procedure.calc_time import time_me
from random import randint

@time_me(10000)
def partition(left=0, right=9):
	seq = [randint(0,100) for _ in range(20)]
	pi = seq[left]
	left, right = left+1, right
	while left < right:
		while seq[left] <= pi and left < right:
			left += 1
		while seq[right] > pi and left <right:
			right -= 1
		seq[left], seq[right] = seq[right], seq[left]
	seq[left-1],seq[0] = seq[0],seq[left-1]
	return seq, left-1


@time_me(10000)
def partition2():
	seq = [randint(0,100) for _ in range(20)]
	pi, seq = seq[0], seq[1:]
	lo = [x for x in seq if x <= pi]
	hi = [x for x in seq if x > pi]
	return lo, pi, hi


if __name__ == "__main__":

	print partition()
	print partition2()