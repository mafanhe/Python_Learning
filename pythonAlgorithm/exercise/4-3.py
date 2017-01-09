# coding=utf-8


def func(A, k):
	Q = []
	for i in A:
		if len(A[i])<k:
			Q.append(i)
	while Q:
		q = Q.pop()
		for i in A[q]:
			A[i].remove(q)
			if len(A[i]) < k:
				Q.append(i)
		A.pop(q)
	print A

if __name__ == "__main__":
	A = {'a':{'b','c','d','e'},'b':{'a','c','e','f'},'f':{'b'},'c':{'a','b','e'},'d':{'a'},'e':{'a','b','c'}}
	func(A, 3)
