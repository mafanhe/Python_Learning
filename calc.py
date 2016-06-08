#*args是可变参数，args接受的是一个tuple
def calc(*numbers):
	sum=0
	for n in numbers:
		sum+=n
	return sum
#**kw是关键字参数，kw接受的事件一个dict
def person(name, age, **kw):
	pass