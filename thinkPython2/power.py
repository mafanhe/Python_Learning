__author__ = 'mafanhe'


def is_power(a, b):
    if a*1.0/b != a//b:
        return False
    if a == b:
        return True
    return is_power(a*1.0/b, b)

if __name__ == "__main__":
    if is_power(8, 2):
        print "yes"