# coding=utf-8

def task(m,l):
	minx = 10000
	n = len(l)
	for i in range(1,n+1):
		al = split2(l,i)
		print al
		a = max(al)*i
		if a<minx:
			minx = a 
	print minx

def split2(l,n):
	l2 = l[:]
	al = [0]*n
	while(l2):
		a = max(l2)
		l2.remove(a)
		# print a
		al[al.index(min(al))]+=a
	return al
