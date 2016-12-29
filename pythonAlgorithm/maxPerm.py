# coding:utf-8
from collections import Counter


# Listing 4-5. A Naive Implementation of the Recursive Algorithm Idea for Finding a Maximum Permutation
# 时间复杂度 O(n^2) 递归版本
def naive_max_perm(M, A=None):
	if not A:
		A = set(range(len(M)))
	if len(A) == 1:
		return A
	B = set(M[i] for i in A)
	C = A - B
	if C:
		A.remove(C.pop())
		return naive_max_perm(M, A)
	return A


# Listing 4-6. Finding a Maximum Permutation
# 时间复杂度O(n),循环版本
def max_perm(M):
	n = len(M)
	A = set(range(n))
	# count = [0] * n		# 代表每个seat分别有多少人想坐
	# for i in M:
	# 	count[i] += 1
	count = Counter(M)		# 同上，代表每个seat分别有多少人想坐
	Q = [i for i in A if count[i] == 0]		# 无用的元素
	while Q:
		i = Q.pop()
		A.remove(i)
		j = M[i]
		count[j] -= 1
		if count[j] == 0:
			Q.append(j)
	return A


if __name__ == "__main__":
	M = [2, 2, 0, 5, 3, 5, 7, 4]
	print naive_max_perm(M)
	print max_perm(M)