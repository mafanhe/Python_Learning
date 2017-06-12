class Node:
	lft = None
	rgt = None
	lvl = 1

	def __init__(self, key, val):
		self.key = key
		self.val = val


# Basically a right rotation
def skew(node):
	if None in [node, node.lft]: return node
	if node.lft.lvl != node.lvl: return node
	lft = node.lft			# The 3 steps of the rotation
	node.lft = lft.right
	lft.rgt = node
	return lft


# Left rotation & level increment
def split(node):
	if None in [node, node.rgt, node.rgt.rgt]: return node
	if node.rgt.rgt.lvl != node.lvl: return node
	rgt = node.rgt
	node.rgt = rgt.lft
	rgt.lft = node
	rgt.lvl += 1
	return rgt


def insert(node, key, val):
	if node is None: return Node(key, val)
	if node.key == key: node.val = val
	elif key < node.key:
		node.lft = insert(node.lft, key, val)
	else:
		node.rgt = insert(node.rgt, key, val)
	node = skew(node)
	node = split(node)
	return node
