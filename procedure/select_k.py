# coding=utf8

def partition(l, lo, hi):
    i = lo+1
    j = hi
    v = l[lo]
    while True:
        while l[i]<v:
            if i==hi:
                break
            i+=1
        while l[j]>v:
            if j==lo:
                break
            j-=1
        if i>=j:
            break
        l[i],l[j] = l[j],l[i]
    l[lo],l[j] = l[j],l[lo]
    return j

def select(l,k):
    lo = 0
    hi = len(l)-1
    while lo<=hi:
        j = partition(l,lo,hi)
        if j==k:return l[j]
        elif j>k:
            hi -= 1
        else:
            lo += 1
    return l[k]

l = [1,4,2,6,3,9,8,6,7,5]
print select(l,2)

