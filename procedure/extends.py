# coding=utf8
class A(object):
	x = 1

class B(A):
	pass

class C(object):
	x = 2

class D(C,A):
	pass
# B.x = 4
# A.x = 3
# print A.x,B.x,C.x,D.x

x = 1
def foo():
	# x+=1
	# 当你在某个作用域内为变量赋值时，该变量被python解释器自动视作该作用域的本地变量，
	# 并取代任何上一层作用域中相同名称的变量
	y =x+1
	print y

# foo()

def create_multipliers():
	return [lambda x : i * x for i in range(5)]


def create_multipliers2():
	return [lambda x, i=1: j * x for j in range(5)]


for multiplier in create_multipliers2():
	print multiplier(2)
