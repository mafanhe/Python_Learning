__author__ = 'mafanhe'


def nested_sum(t):
    num = 0
    for i in t:
        num += sum(i)
    print (num)


def cumsum(t):
    t1 = []
    for i in range(len(t)):
        t1.append(sum(t[:i+1]))
    return t1