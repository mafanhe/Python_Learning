class Queen:
	def __init__(self,stack1=[],stack2=[]):
		self.stack1 = stack1
		self.stack2 = stack2
	def push(self,value):
		self.stack1.append(value)
	def pop(self):
		if self.stack2:
			return self.stack2.pop()
		while self.stack1:
			self.stack2.append(self.stack1.pop())
		return self.stack2.pop()


class ListNode:
	def __init__(self,value,nextNode=None):
		self.value = value
		self.nextNode = nextNode

def removeNode(pHead, value):
	if not pHead or not value:
		return
	p = pHead
	c = p.nextNode
	while c:
		n = c.nextNode
		if c.value==value:
			p.nextNode = n
			#delete c
		p = p.nextNode
		c = c.nextNode

def reverseList(pHead):
	p = pHead
	c = p.nextNode
	p.nextNode = None
	while c:
		n = c.nextNode
		c.nextNode = p
		p = c
		c = n
	return p


def reverseList2(pHead):
	p = pHead
	if p:
		if p.nextNode:
			reverseList2(p.nextNode)
		print p.value


def printListNode(list):
	while list:
		print list.value
		list = list.nextNode

# pHead = ListNode(None,ListNode(1,ListNode(2,ListNode(3))))
# printListNode(pHead)
# removeNode(pHead,4)
# printListNode(pHead)

# p=reverseList(pHead)
# printListNode(p)

# reverseList2(pHead)

