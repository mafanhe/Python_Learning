import math

def move(x,y,step,angle=0):
	nx = x+ step * math.cos(angle)
	ny = y - step * math.sin( angle)
	return nx,ny
def hmove(n, a, b, c):
	if  n==1:
		print(a, "-->", c)
		return
	else:
		hmove(n-1, a, c, b)
		hmove(n-1, a, b, c)
		hmove(n-1, b, a, c)
