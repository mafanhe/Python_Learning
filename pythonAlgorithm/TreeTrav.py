class Tree:
	# def __init__(self):
	# 	pass
	def __init__(self, data=None, left=None, right=None):
        	self.data = data
        	self.left = left
        	self.right = right

def firsttraverse(t):
	l = []
	while t or l:
		# print l
		if(t):
			print t.data,
			l.append(t)
			t = t.left
		else:
			t = l.pop()
			t = t.right

def firsttraverse2(t):
	if t:
		print t.data,
		firsttraverse2(t.left)
		firsttraverse2(t.right)

def midtraverse(t):
	l = []
	while t or l:
		# print l
		if(t):
			l.append(t)
			t = t.left
		else:
			t = l.pop()
			print t.data,
			t = t.right

def midtraverse2(t):
	if t:
		midtraverse2(t.left)
		print t.data,
		midtraverse2(t.right)

def lasttraverse(t):
	l = []
	mark = None
	while t or l:
		# print l
		while t:
			l.append(t)
			t = t.left
		t= l.pop()
		if not t.right or t.right == mark:
			print t.data,
			mark = t
			t = None
		else:
			l.append(t)
			t = t.right

def lasttraverse2(t):
	if t:
		lasttraverse2(t.left)
		lasttraverse2(t.right)
		print t.data,


t = Tree('-',Tree('*',Tree('a'),Tree('b')),Tree('/',Tree('d'),Tree('e')))
# t= Tree()

firsttraverse(t)
print
firsttraverse2(t)

print

midtraverse(t)
print
midtraverse2(t)

print

lasttraverse(t)
print
lasttraverse2(t)