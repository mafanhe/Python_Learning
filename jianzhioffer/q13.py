from ListNode import *


def delete_node(pListHead, pToBeDeleted):
	pre = pToBeDeleted
	cur = pre.next
	if pListHead == pToBeDeleted:
		# del pToBeDeleted
		# pToBeDeleted=NULL
		# pListHead = NULL
		pass
	if cur is None:
		# del pre
		pass
	else:
		n = pre.next.next
		pre.value = cur.value
		pre.next = n



l = ListNode(1, ListNode(2, ListNode(3)))
de = l.next.next
printNode(l)
delete_node(l, de)
printNode(l)

