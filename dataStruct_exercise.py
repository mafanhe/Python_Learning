import string
from list_exercises import read2list


def deal_text(t):
    t.strip(string.whitespace+string.punctuation)
    return t


def read2dict(file):
    t = dict()
    with open(file) as words:
        for index, word in enumerate(words):
            for w in word.split(' '):
                d_word = deal_text(w)
                if d_word != "":
                    t[d_word] = t.get(d_word, 0)+1
    return t


def num_word(t):
    return len(t)


def max20(t):
    t2 = sorted(t.items(), key=lambda d: d[1], reverse=True)
    for i in range(20):
        print(t2[i][0])
    print("-" * 20)


def word_not_in_dictionary(t):
    dictionary = read2list()
    word = set(t)-dictionary
    return word


