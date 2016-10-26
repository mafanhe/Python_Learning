# coding=utf-8
from ListNode import *


# 面试题17：合并两个排序的链表
def merge_two_sorted_list(ln1, ln2):
	p1 = ln1
	p2 = ln2
	head = ListNode(-1)
	p = head
	while p1 and p2:
		if p1.value < p2.value:
			p.next = p1
			p1 = p1.next
		else:
			p.next = p2
			p2 = p2.next
		p = p.next

	if p1:
		p.next = p1

	if p2:
		p.next = p2
	return head


if __name__ == "__main__":
	ln1 = ListNode(1, ListNode(3, ListNode(5, ListNode(7, ListNode(9)))))
	ln2 = ListNode(2, ListNode(4, ListNode(6)))
	printNode(ln1)
	printNode(ln2)
	p = merge_two_sorted_list(ln1, ln2)
	p = merge_two_sorted_list(None, None)
	printNode(p.next)

