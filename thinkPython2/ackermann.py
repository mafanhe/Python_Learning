__author__ = 'mafanhe'

known = dict()
cache = dict()


def ack(m, n):
    if (m, n) in known:
        return known[(m, n)]

    if m == 0:
        return n+1
    elif m > 0 and n == 0:
        return ack(m-1, 1)
    else:
        known[(m, n)] = ack(m-1, ack(m, n-1))
        return ack(m-1, ack(m, n-1))


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

if __name__ == "__main__":
    print(ack(3, 4))
    print(known)

    print(ackermann(3, 4))
    print(cache)
