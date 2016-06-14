import math

__author__ = 'mafanhe'


def estimate_pi():
    one_pi = 0
    k = 0
    while 1:
        k4 = k*4
        num = math.factorial(k4)*(1103+26390*k)*2*math.sqrt(2)/(pow(math.factorial(k),4)*pow(396,k4)*9801)
        if num < 10**-15:
            break
        one_pi += num
        k += 1
    return 1.0/one_pi

print estimate_pi(),math.pi