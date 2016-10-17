# -*- encoding:utf-8 -*-
_author__ = 'mafanhe'


def gcd(a, b):

    ''' 根据 gcd(a,b) = gcd(b,a%b)
    :param a:
    :param b:
    :return: 最大公约数
    '''

    (a, b) = (a, b) if a > b else (b, a)
    if b == 0:
        return a
    return gcd(b, a % b)

if __name__ == "__main__":

    print gcd(20, 12)