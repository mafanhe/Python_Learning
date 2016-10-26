# coding:utf-8

from BinaryTreeNode import *


# 面试题18：树的子结构
def has_sub_tree(p, s):
	flag = False
	if p and s:
		if p.data == s.data:
			flag = does_tree1_have_tree2(p, s)
		if not flag:
			flag = has_sub_tree(p.left, s)
		if not flag:
			flag = has_sub_tree(p.right, s)
	return flag


def has_sub_tree2(p, s):
	l = []
	while l or p:
		if p:
			l.append(p)
			if p.data == s.data and does_tree1_have_tree22(p, s) is None:
				return True
			p = p.left
		else:
			p = l.pop()
			p = p.right
	return False


def does_tree1_have_tree2(b1, b2):
	if not b2:
		return True
	if not b1:
		return False
	if b1.data != b2.data:
		return False
	return does_tree1_have_tree2(b1.left, b2.left) and does_tree1_have_tree2(b1.right, b2.right)


def does_tree1_have_tree22(b1, b2):
	l1 = []
	l2 = []
	while l2 or b2:
		if b2:
			if b2.data != b1.data:
				return False
			l1.append(b1)
			l2.append(b2)
			b2 = b2.left
			b1 = b1.left
		else:
			b2 = l2.pop()
			b2 = b2.right
			b1 = l1.pop()
			b1 = b1.right
	return True


if __name__ == '__main__':
	t = BinaryTreeNode('-', BinaryTreeNode('*', BinaryTreeNode('a'), BinaryTreeNode('b')), BinaryTreeNode('/', BinaryTreeNode('d'), BinaryTreeNode('e')))
	t2 = BinaryTreeNode('-', BinaryTreeNode('*', BinaryTreeNode('a'), BinaryTreeNode('b')), BinaryTreeNode('/', BinaryTreeNode('d'), BinaryTreeNode('e')))
	t3 = BinaryTreeNode('-', BinaryTreeNode('*', BinaryTreeNode('a')))
	t4 = BinaryTreeNode('*', BinaryTreeNode('a'), BinaryTreeNode('b'))
	t5 = BinaryTreeNode('/', BinaryTreeNode('d'), BinaryTreeNode('e'))
	t6 = BinaryTreeNode('/', BinaryTreeNode('a'), BinaryTreeNode('e'))


	# print does_tree1_have_tree2(t6, t5)
	# print does_tree1_have_tree22(t6, t5)
	print has_sub_tree(t,t2), has_sub_tree(t,t2)
	print has_sub_tree(t,t3), has_sub_tree(t,t3)
	print has_sub_tree(t,t4), has_sub_tree(t,t4)
	print has_sub_tree(t,t5), has_sub_tree(t,t5)
	print has_sub_tree(t,t6), has_sub_tree(t,t6)
