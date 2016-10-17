# 2-7 A Binary Class

class Tree:
    def __init__(self, left, right):
        self.left = left
        self.right = right

# t = Tree(Tree("a", "b"), Tree("c", "d"))
# t.right.left


# 2-8 A Multiway Tree Class

class Tree:
    def __init__(self, kids, next=None):
        self.kids = self.val = kids
        self.next = next

# t = Tree(Tree("a", Tree("b", Tree("c", Tree("d")))))
# t.kids.next.next.val


# Bunch Pattern
class Bunch(dict):
    def __init__(self, *args, **kwds):
        super(Bunch, self).__init__(*args, **kwds)
        self.__dict__ = self

# >>> T = Bunch
# >>> t = T(left=T(left="a", right="b"), right=T(left="c"))
# >>> t.left
# {'right': 'b', 'left': 'a'}
# >>> t.left.right
# 'b'
# >>> t['left']['right']
# 'b'
# >>> "left" in t.right
# True
# >>> "right" in t.right
# False
