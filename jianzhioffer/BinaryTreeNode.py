class BinaryTreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def first_traversal(t):
    s = []
    while t or s:
        # print s
        if(t):
            print t.data,
            s.append(t)
            t = t.left
        else:
            t = s.pop()
            t = t.right


def firsttraverse2(t):
    if t:
        print t.data,
        firsttraverse2(t.left)
        firsttraverse2(t.right)