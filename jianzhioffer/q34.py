# coding=utf-8

# 面试题34：丑数


# 解法一
def is_ugly(number):
    while not number % 2:
        number /= 2
    while not number% 5:
        number /= 5
    while not number % 3:
        number /= 3
    return True if number == 1 else False


def get_ugly_number(n):
    number = 0
    uglys = 0
    while uglys<n:
        number+=1
        if is_ugly(number):
            uglys+=1
    return number
    # res = filter(is_ugly, range(2,n))
    # return res


def get_ugly_number2(n):
    ugly_number = [float('inf')]*n
    ugly_number[0] = 1
    nextUgly = 1
    num2 = 0
    num3 = 0
    num5 = 0
    while nextUgly < n:
        ugly_number[nextUgly] = (min(ugly_number[num2]*2, ugly_number[num3]*3, ugly_number[num5]*5))
        while num2 * 2 < ugly_number[nextUgly]:
            num2 += 1
        while num3 * 3 < ugly_number[nextUgly]:
            num3 += 1
        while num5 * 5 < ugly_number[nextUgly]:
            num5 += 1
        nextUgly += 1

    print ugly_number
    return ugly_number[-1]

if __name__ == "__main__":
    print get_ugly_number(10)
    print get_ugly_number2(10)