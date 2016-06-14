def check_fermat(a,b,c,n):
    if a**n+b**n == c**n and n>2:
        print "Holy smokers,Fermat was wrong!"
    else:
        print "NO,that dosen't work"

def func():
    a=int(input("please input int number as 'a'\n"))
    b=int(input("please input int number as 'b'\n"))
    c=int(input("please input int number as 'c'\n"))
    n=int(input("please input int number as 'n'\n"))
    check_fermat(a,b,c,n)

func()