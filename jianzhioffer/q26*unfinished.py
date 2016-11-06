# coding=utf-8

from ListNode import *


# 面试题26：复杂链表的复制
def clone_nodes(pHead):
	p = pHead
	cHead = p
	ph = pHead
	while ph:
		cNext = ph.next
		p.next = cNext
		p = p.next
		ph = ph.next
	printNode(cHead)
	p = pHead
	ph = pHead
	# while ph:
	# 	if ph.pSibling




	pass


if __name__ == "__main__":
	A = ComplexListNode('A',None,None)
	B = ComplexListNode('B')
	C = ComplexListNode('C')
	D = ComplexListNode('D')
	E = ComplexListNode('E')
	A.next = B
	B.next = C
	C.next = D
	D.next = E
	A.sibling = C
	B.sibling = E
	D.sibling = B

	clone_nodes(A)
	# printNode(l)