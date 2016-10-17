n,m = [int(i) for i in raw_input().strip().split()]
l = [int(i) for i in raw_input().strip().split()]
res = 0
length = len(l)
for i in range(length):
    for j in range(i,length):
        if l[i]^l[j]>m:
            res+=1
print res


