# coding=utf-8

from BinaryTreeNode import *


# 面试题23：从上往下打印二叉树
def print_from_top_to_bottom(pTreeRoot):
	queen = [pTreeRoot]
	while queen:
		bt = queen.pop(0)
		print bt.data
		if bt.left:
			queen.append(bt.left)
		if bt.right:
			queen.append(bt.right)

if __name__ == "__main__":
	t = BinaryTreeNode('-', BinaryTreeNode('*', BinaryTreeNode('a'), BinaryTreeNode('b')),
					   BinaryTreeNode('/', BinaryTreeNode('d'), BinaryTreeNode('e')))
	print_from_top_to_bottom(t)