def re_order_odd_even(data,func):
	l = 0
	r = len(data)-1
	while l < r:
		while l < r and func(data[l]):
			l += 1
		while l < r and not func(data[r]):
			r -= 1
		data[l], data[r] = data[r], data[l]
		# l+=1
		# r-=1
	print data

def is_even(i):
	if i&1==1:
		return True
	else:
		return False
re_order_odd_even([1,3,2,4,5,6,7,8,9],is_even)


