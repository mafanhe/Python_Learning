# coding=utf-8
from ListNode import *


# 面试题15:链表中倒数第k个结点
def find_kth_to_tail(pListHead, k):
	if pListHead is None or k <= 0:
		print "args is not valid"
		return
	first = pListHead
	second = pListHead
	i = 0
	while i < k and first is not None:
		first = first.next
		i += 1
	if first is None:
		print 'k is not valid'
		return
	while first is not None:
		first = first.next
		second = second.next
	print second.value


# 相关题目：求链表的中间节点
def find_mid(pListHead):
	first = pListHead
	second = pListHead
	if pListHead is None:
		return None
	if pListHead.next is None:
		return pListHead
	while second is not None and second.next is not None and second.next.next is not None:
		first = first.next
		second = second.next.next
	print first.value


# 相关题目：判断一个单项链表是否形成了环形结构
def is_circle(pListHead):
	first = pListHead
	second = pListHead
	while second is not None and second.next is not None and second.next.next is not None and first.next is not None:
		if second == first:
			return True
		second = second.next.next
		first = first.next
	return False

if __name__ == '__main__':
	l = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7)))))))
	p = l
	while p.next:
		p = p.next
	p.next = l
	print is_circle(l)