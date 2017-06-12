
# Listing 6-1 a general implementation of the Divide and conquer Scheme
def divide_and_conquer(S, divide, combine):
	if len(S) == 1: return S
	L, R = divide(S)
	A = divide_and_conquer(L, divide, combine)
	B = divide_and_conquer(R, divide, combine)
	return combine(A, B)

# Listing 6-2 Insertion into and Search in a Binary Search Tree
class Node:
	lft = None
	rgt = None
	def __init__(self, key, val):
		self.key = key
		self.val = val


def insert(node, key, val):
	if node is None: return Node(key, val)
	if node.key == key: node.val = val
	elif key < node.key:
		node.lft = insert(node.lft, key, val)
	else:
		node.rgt = insert(node.rgt, key, val)
	return node


def search(node, key):
	if node is None: raise KeyError
	if node.key == key: return node.val
	elif key < node.key:
		return search(node.lft, key)
	else:
		return search(node.rgt, key)


class Tree:
	root = None

	def __setitem__(self, key, val):
		self.root = insert(self.root, key, val)

	def __getitem__(self, key):
		return search(self.root, key)

	def __contains__(self, key):
		try:
			search(self.root, key)
		except KeyError:
			return False
		return True


def find_kth(lst, k):
	if k > len(lst):
		raise KeyError
	val = lst[0]
	lft = []
	rgt = []
	for i in lst[1:]:
		if i <= val:
			lft.append(i)
		else:
			rgt.append(i)
	if len(lft) == k-1:
		return val
	elif len(lft) > k-1:
		return find_kth(lft, k)
	else:
		return find_kth(rgt, k-len(lft)-1)



if __name__ == "__main__":
	l = [1, 5, 3, 6, 9, 2, 4, 8, 7, 11, 10]
	print find_kth(l, 2)
