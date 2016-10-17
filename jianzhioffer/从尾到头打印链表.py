class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def printListFromTailToHead(listNode):
    # write code here
    if listNode is None:
        return []
    p = listNode
    c = listNode.next
    p.next = None
    while c.next:
        n = c.next
        c.next = p
        p = c
        c = n
    n.next = p
    return n

def printf(listNode):
    while listNode:
        print listNode.val,
        listNode = listNode.next

l = ListNode(0)
p = l
for i in range(1,4):
    p.next = ListNode(i)
    p = p.next
l=printListFromTailToHead(l)
printf(l)