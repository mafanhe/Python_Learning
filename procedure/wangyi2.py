import time
def primes(x):
    # prepair data space
    plist = [0, 0] + range(2,x)
    for i in xrange(2, x):
        if plist[i]:
            plist[i+i::i] = [0] * len(plist[i+i::i])
    return plist
def fact(res):
    for i in range(3,len(res)):
        if res[i] != 0:
            continue
        for j in range(i+1,1,-1):
            if res[j] != 0 and i % j == 0:
                res[i] = res[j]
                break
    return res

n = int(raw_input())+1
start = time.time()
if n>3:
    res = primes(n)
    res[0] = 0
    res[1] = 1
    res[2] = 1
    res = fact(res)
    print (sum(res[:n + 1]))
elif n ==2:
    print 2
elif n ==1:
    print 1
else:
    print 0
end = time.time()
print end-start




