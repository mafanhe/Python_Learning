n,q = [int(_) for _ in raw_input().split()]
A = [int(_) for _ in raw_input().split()]
B = [int(_) for _ in raw_input().split()]
Q = []
for i in range(q):
    Q.append([int(_)for _ in raw_input().split()])
for d in Q:
    x,y = d
    num = 0
    for i in range(n):
        if A[i]>=x and B[i]>=y:
            num+=1
    print num