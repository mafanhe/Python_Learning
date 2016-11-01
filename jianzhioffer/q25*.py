# coding=utf-8

from BinaryTreeNode import *


def find_path(pTreeRoot, eSum, cSum, stack):
	stack.append(pTreeRoot.data)
	cSum += int(pTreeRoot.data)
	if cSum == eSum:
			print eSum,cSum,stack
	if pTreeRoot.left:
		find_path(pTreeRoot.left, eSum, cSum, stack)
	if pTreeRoot.right:
		find_path(pTreeRoot.right, eSum, cSum, stack)
	# if cSum is index then
	# cSum -= pTreeRoot.data
	stack.pop()

if __name__ == "__main__":
	t = BinaryTreeNode('10', BinaryTreeNode('5', BinaryTreeNode('4'), BinaryTreeNode('7')),\
					   BinaryTreeNode('12'))
	find_path(t, 22,0,[])