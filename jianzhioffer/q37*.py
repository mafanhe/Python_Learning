# coding:utf-8
# 面试题36：两个链表的第一个公共结点,（类似题目：面试题50）

from ListNode import ListNode


# 用栈来解决
def find_first_common_node(phead1, phead2):
	stack1, stack2 = [], []
	while phead1:
		stack1.append(phead1)
		phead1 = phead1.next
	while phead2:
		stack2.append(phead2)
		phead2 = phead2.next
	top1 = stack1.pop()
	top2 = stack2.pop()
	common_node = None
	while top1 == top2:
		common_node = top1
		top1 = stack1.pop()
		top2 = stack2.pop()
	return common_node

if __name__ == "__main__":
	common_node = ListNode(6, ListNode(7))
	l1 = ListNode(1, ListNode(2, ListNode(3, common_node)))
	l2 = ListNode(4, ListNode(5, common_node))

	print find_first_common_node(l1, l2).value

