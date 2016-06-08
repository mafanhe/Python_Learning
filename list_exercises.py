__author__ = 'mafanhe'
import random


def nested_sum(t):
    num = 0
    for i in t:
        num += sum(i)
    print(num)


def cumsum(t):
    t1 = []
    for i in range(len(t)):
        t1.append(sum(t[:i+1]))
    return t1


def middle(t):
    t = t[1:-1]
    return t


def chop(t):
    del t[0]
    del t[-1]


def is_sorted(t):
    for i in range(len(t)-1):
        if t[i]> t[i+1]:
            return False
    return True


def is_anagram(str1, str2):
    if len(str1) != len(str2):
        return False
    word3 = list(str2)
    for i in str1:
        if i in word3:
            word3.remove(i)
    if len(word3) != 0:
        return False
    return True


# def has_duplicates(t):
#     l = []
#     for i in t:
#         if i in l:
#             return True
#         l.append(i)
#     return False


def has_duplicates(t):
    """Returns True if any element appears more than once in a sequence.

    t: list

    returns: bool
    """
    # make a copy of t to avoid modifying the parameter
    s = t[:]
    s.sort()

    # check for adjacent elements that are equal
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            return True
    return False


def random_bdays(n):
    """Returns a list of integers between 1 and 365, with length n.

    n: int

    returns: list of int
    """
    t = []
    for i in range(n):
        bday = random.randint(1, 365)
        t.append(bday)
    return t


def count_matches(num_students, num_simulations):
    """Generates a sample of birthdays and counts duplicates.

    num_students: how many students in the group
    num_samples: how many groups to simulate

    returns: int
    """
    count = 0
    for i in range(num_simulations):
        t = random_bdays(num_students)
        if has_duplicates(t):
            count += 1
    return count


def main():
    """Runs the birthday simulation and prints the number of matches."""
    num_students = 23
    num_simulations = 10000
    count = count_matches(num_students, num_simulations)

    print('After %d simulations' % num_simulations)
    print('with %d students' % num_students)
    print('there were %d simulations with at least one match' % count)


def read2list():
    t = []
    with open("word.txt") as words:
        for word in words:
            t.append(word.strip())
    return t


def in_bisect(t, a):
    left = 0
    right = len(t)-1

    while right >= left:
        mid = (left + right) // 2
        if t[mid] == a:
            return mid
        elif t[mid] > a:
            right = mid-1
        else:
            left = mid + 1
    return None


def reverse_pair(word_list, word):
    rev_word = word[::-1]
    return in_bisect(word_list, rev_word)


def diverse_word(word):
    return word[0::2], word[1::2]


def interlock(word_list):
    for word in word_list:
        word1, word2 = diverse_word(word)
        if in_bisect(word_list, word1) is not None and in_bisect(word_list, word2) is not None:
            print(word, diverse_word(word))


if __name__ == '__main__':
    word_list = ["shoe", "cold", "schooled"]
    word_list.sort()
    interlock(word_list)

