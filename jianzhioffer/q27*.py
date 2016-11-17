# coding=utf-8

from BinaryTreeNode import *


# 面试题27：二叉搜索树与双向链表
def convert_binary_search_tree(pHead):
	pLastNodeList = None
	convert_node(pHead, pLastNodeList)
	# pLastNodeList 指向双向链表的尾结点
	# 我们需要返回头结点
	while pHead and pHead.left is not None:
		pHead = pHead.left
	return pHead


def convert_node(pNode, pLastNodeList):
	if pNode is None:
		return
	pCurrent = pNode
	if pCurrent.left is not None:
		pLastNodeList=convert_node(pCurrent.left, pLastNodeList)
	pCurrent.left = pLastNodeList
	if pLastNodeList is not None:
		pLastNodeList.right = pCurrent
	pLastNodeList = pCurrent
	if pCurrent.right is not None:
		pLastNodeList=convert_node(pCurrent.right, pLastNodeList)
	return pLastNodeList


def print_node(pNode):
	while pNode:
		print pNode.data
		pNode = pNode.right

if __name__ == "__main__":
	t = BinaryTreeNode('10', BinaryTreeNode('6', BinaryTreeNode('4'), BinaryTreeNode('8')), BinaryTreeNode('14',
						BinaryTreeNode('12'), BinaryTreeNode('16')))
	p = convert_binary_search_tree(t)
	print_node(p)
