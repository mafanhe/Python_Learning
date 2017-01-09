# coding:utf-8
# 面试题39：二叉树的深度

from BinaryTreeNode import BinaryTreeNode


# 遍历一次
def tree_depth(tree):
	if not tree:
		return 0
	left = tree_depth(tree.left)
	right = tree_depth(tree.right)
	return max(left+1, right+1)


# 遍历多次
def is_avl_tree(tree):
	if not tree:
		return True
	left = tree_depth(tree.left)
	right = tree_depth(tree.right)
	if abs(left-right) > 1:
		return False
	return is_avl_tree(tree.left) and is_avl_tree(tree.right)


# 遍历一次
def is_avl_tree2(tree, depth=0):
	if not tree:
		depth = 0
		return True
	left, right = 0, 0
	if is_avl_tree2(tree.left, left) and is_avl_tree2(tree.right, right):
		if abs(left-right)>1:
			return max(left+1, right+1)
	return False


if __name__ == "__main__":
	t = BinaryTreeNode('-', BinaryTreeNode('*', BinaryTreeNode('a'), BinaryTreeNode('b')), BinaryTreeNode('/', BinaryTreeNode('d'), BinaryTreeNode('e')))
	t2 = BinaryTreeNode('-', BinaryTreeNode('*',BinaryTreeNode('a')))
	# print tree_depth(t)
	# print tree_depth(t2)
	print is_avl_tree2(t)
	print is_avl_tree2(t2)