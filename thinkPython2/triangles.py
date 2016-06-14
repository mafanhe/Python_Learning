def triangles():
	l1=[1]
	yield l1
	while True:
		n=0
		l2=[]
		for x in l1:
			y=x+n
			n=x
			l2.append(y)		
		l2.append(1)
		yield l2
		l1=l2