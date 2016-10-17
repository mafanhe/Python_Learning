# sogou
def getPrime(maxNum):
    aList = [x for x in range(0,maxNum)]
    prime = []
    for i in range(2,len(aList)):
        if aList[i] != 0:
            prime.append(aList[i])
            clear(aList[i],aList,maxNum)
    return prime

def clear(aPrime,aList,maxNum):
    for i in range(2,int((maxNum/aPrime)+1)):
        if not aPrime*i>maxNum-1:
            aList[i*aPrime]=0

n = int(raw_input())
l = []
for i in range(n):
    l.append(int(raw_input()))


primes = getPrime(max(l)) if n!=0 else []
res = [0]*len(l)
for i in primes:
    for j in range(len(l)):
        if i<l[j]:
            res[j]+=1
sum=0
for i in range(len(res)):
    for j in range(i+1,len(res)):
        sum+=abs(res[i]-res[j])
print sum