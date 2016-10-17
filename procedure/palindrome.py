__author__ = 'mafanhe'


def first(word):
    return word[0]


def last(word):
    return word[-1]


def middle(word):
    return word[1:-1]


def is_palindrome(word):
    if len(word) == 0:
        print "yes"
        return True
    if first(word) != last(word):
        print "no"
        return False

    is_palindrome(middle(word))


def is_palindrome2(word):
    return word == word[::-1]

if __name__ == "__main__":
    print is_palindrome2('redivider')

