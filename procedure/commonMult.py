l=[1,2,3,4,5,6,8]
def commult(l):
    x=max(l)
    while(True):
        for i in range(len(l)):
            if (x%l[i]!=0):
                x+=1
                break
            if i ==len(l)-1:
                print x
                return 
commult(l)