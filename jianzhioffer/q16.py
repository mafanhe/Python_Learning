# coding=utf-8

from ListNode import *


# 面试题16：反转链表
def reverse_list(pListHead):
	p = None
	c = pListHead
	reverse_head = None

	while c:
		n = c.next
		# if c is tail
		if n is None:
			reverse_head = c
		c.next = p
		p = c
		c = n
	return reverse_head


# 递归实现反转
def reverse_list2(p):
	if p is None or p.next is None:
		return p
	else:
		n = reverse_list2(p.next)
		p.next.next = p
		p.next = None
		return n


if __name__ == "__main__":
	l = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7)))))))
	# l = None
	# l = ListNode(1)
	printNode(l)
	reverse_list2(l)
	printNode(l)



