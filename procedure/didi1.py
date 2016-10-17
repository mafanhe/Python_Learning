# 阶乘末尾0的个数
def zeros(n):
    x = n // 5
    return x + zeros(x) if x else 0
a = int(raw_input())
print zeros(a)