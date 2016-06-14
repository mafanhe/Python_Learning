# -*- codiing:utf-8 -*-


def histogram(s):
    """
    直方图，是计数器（或是频率）集合的统计术语
    :param s: 可迭代对象
    :return: 字典
    """
    d = dict()
    for c in s:

        # for c in s:
        #     if c not in d:
        #         d[c] = 1
        #     else:
        #         d[c] += 1

        # ↓简化代码↓
        d[c] = d.get(c, 0)+1
    return d


def print_hist(h):
    """
    按序输出直方图
    :param h: 直方图字典
    :return: None
    """
    for c in sorted(h):
        print(c, h[c])


def reverse_lookup(d, v):
    """
    逆向查找字典的key
    :param d: 字典
    :param v: 值
    :return: 键
    """
    for k in d:
        if d[k] == v:
            return k
    raise LookupError


def invert_dict(d):
    """

    :param d:
    :return:
    """
    inverse = dict()
    for key, value in d.items():
        # inverse[value] = inverse.get(value, [])+[key]
        # ↓简化代码↓
        inverse.setdefault(value, []).append(key)
    return inverse

known = {0: 0, 1: 1}


def fibonacci(n):
    if n in known:
        return known[n]

    res = fibonacci(n-2)+fibonacci(n-1)
    known[n] = res
    return res

cache = dict()


def ackermann(m, n):
    """Computes the Ackermann function A(m, n)

    See http://en.wikipedia.org/wiki/Ackermann_function

    n, m: non-negative integers
    """
    if m == 0:
        return n+1
    if n == 0:
        return ackermann(m-1, 1)
    try:
        return cache[m, n]
    except KeyError:
        cache[m, n] = ackermann(m-1, ackermann(m, n-1))
        return cache[m, n]


def has_duplicates(t):
    """
    Returns True if any element appears more than once in a sequence.
    :param t: list
    :return: bool
    """
    s = dict()
    for i in t:
        if i in s:
            return True
        else:
            s[i] = True
    return False


def has_duplicates2(t):
    """
    Returns True if any element appears more than once in a sequence.
    :param t: list
    :return: bool
    """
    return len(set(t)) < len(t)


