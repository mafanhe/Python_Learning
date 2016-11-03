# coding=utf-8

from ListNode import *


# 面试题26：复杂链表的复制
def clone_nodes(pHead):

	cHead = pHead
	cNext = pHead.next
	cHead.next = cNext
	sibling = pHead.sibling
	cHead.sibling = sibling


	pass


if __name__ == "__main__":
	pass