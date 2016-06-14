from collections import Counter


def is_anagram(str1, str2):
    if len(str1) != len(str2):
        return False
    l2=list(str2)
    for i in str1:
        for j in str2:
            if j == i:
                l2.remove(j)
                break

    return True if len(l2) == 0 else False


def is_anagram2(str1, str2):
    str1, str2 = sorted(str1), sorted(str2)
    return True if str1 == str2 else False


def is_anagram3(str1, str2):
    c1, c2 = Counter(str1), Counter(str2)
    return True if c1 == c2 else False


print(is_anagram("123","321"),is_anagram("123","121"),is_anagram("123","1231"))
print(is_anagram2("123","321"),is_anagram("123","121"),is_anagram("123","1231"))
print(is_anagram3("123","321"),is_anagram("123","121"),is_anagram("123","1231"))