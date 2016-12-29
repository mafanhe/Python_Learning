# coding=utf-8

# 递归直接求出
def fun_recursion(m,k):
    """
    f[1]=0;
    f[i]=(f[i-1]+k)%i = (f[i-1] +m%i) % i = (f[i-1] + m) % i ;  (i>1)
    :param m: 长度
    :param k: 第k数出环
    :return:
    """
    if m == 1:
        return 0
    else:
        return (fun_recursion(m-1, k) +k) % m

# 递归求出出圈队列
def fun(m, k, i):
    """
    当i=1时，f(m,k,i) = (m+k-1)%m
    当i!=1时，f(m,k,i)= ( f(m-1,k,i-1)+k )%m
    :param m: 长度
    :param k: 第k数出环
    :param i:
    :return:
    """
    if(i==1):
        return (m+k-1)%m
    else:
        return (fun(m-1, k, i-1)+k)%m
# for i in range(1,11):
#     print("第%d次出环：%d" % (i,fun(10,3,i)))

# 遍历求出结果
def func2(m, k):
    """
    :param m:
    :param k:
    :return:
    """
    s = 0
    for i in range(2, m+1):
        s = (s + k) % i
    print "the winner is %d" % s

