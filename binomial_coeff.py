from collections import defaultdict

binomial = defaultdict(list)


def binomial_coeff(n, k):
    """Compute the binomial coefficient "n choose k"

    :param n: number of trials
    :param k: number of successes

    :return: int
    """
    if k == 0:
        return 1
    if n == 0:
        return 0

    global binomial
    b = binomial[(n, k)]
    if len(b) == 0:
        res = binomial_coeff(n-1, k) + binomial_coeff(n-1, k-1)
        b.append(res)
        return res
    else:
        return b[0]

a = binomial_coeff(4, 2)
print(a)
print(binomial)
