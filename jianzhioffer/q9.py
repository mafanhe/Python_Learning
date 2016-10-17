# coding=utf-8

# 斐波那挈数列
def fibonacci(n):
    if n==1:
        return 1
    if n==2:
        return 1
    return fibonacci(n-1)+fibonacci(n-2)


def fibonacci(n):
    f = [1]*n
    for i in range(2,n):
        f[i] = f[i-1]+f[i-2]
    print f
    return f[n-1]

print fibonacci(9)

