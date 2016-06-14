def fib(max):
	n,a,b=0,0,1
	while n<max:
		yield b	#generator
		a,b=b,a+b
		n+=1
	return 'done'