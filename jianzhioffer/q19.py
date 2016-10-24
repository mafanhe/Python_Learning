# coding=utf-8

from BinaryTreeNode import *


# 二叉树的镜像 递归
def binary_tree_node_mirror(bt):
    if not bt:
        return
    l = bt.left
    r = bt.right
    bt.left, bt.right = bt.right, bt.left
    binary_tree_node_mirror(l)
    binary_tree_node_mirror(r)


# 循环
def binary_tree_node_mirror2(bt):
    lis = []
    while bt or lis:
        if bt:
            lis.append(bt)
            bt.left, bt.right = bt.right, bt.left
            bt = bt.right
        else:
            bt = lis.pop()
            bt = bt.left


if __name__ == '__main__':
    t = BinaryTreeNode('-', BinaryTreeNode('*', BinaryTreeNode('a'), BinaryTreeNode('b')), BinaryTreeNode('/', BinaryTreeNode('d'), BinaryTreeNode('e')))
    first_traversal(t)
    binary_tree_node_mirror2(t)
    first_traversal(t)