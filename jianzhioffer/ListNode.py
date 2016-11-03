class ListNode:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next


def printNode(l, j=20):
	i = 0
	while l and i < 20:
		print l.value, '->',
		l = l.next
		i += 1
	print 'None'


class ComplexListNode:
	def __int__(self, value, next, sibling):
		self.value = value
		self.next = next
		self.sibling = sibling

