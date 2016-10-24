class BinaryTreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def first_traversal(t):
    l = []
    while t or l:
        # print l
        if(t):
            print t.data,
            l.append(t)
            t = t.left
        else:
            t = l.pop()
            t = t.right


def firsttraverse2(t):
    if t:
        print t.data,
        firsttraverse2(t.left)
        firsttraverse2(t.right)