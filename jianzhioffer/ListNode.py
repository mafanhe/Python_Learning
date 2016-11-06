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


# doubly linked list
class DoubleListNode:
	def __init__(self, value, pre=None, next=None):
		self.value = value
		self.pre = pre
		self.next = next


class ComplexListNode:
	def __init__(self, value=None, next=None, sibling=None):
		self.value = value
		self.next = next
		self.sibling = sibling

if __name__ == '__main__':
	l = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7)))))))
	printNode(l)