# -*-coding:utf-8 -*-


import random

import jieba

suffix_map = {}
prefix = ()

def markov(filename,order=2):
    i=1
    with open(filename) as fp:
        # skip_gutenberg_header(fp)

        for line in fp:
            i += 1
            for word in jieba.cut(line.rstrip().replace(" ",''), cut_all=False):
                process_word(str(word), order)
    print(i, "lines")


def process_word(word, order=2):
    global prefix
    global suffix_map
    if len(prefix) < order:
        prefix += (word,)
        return

    try:
        # print(prefix)
        suffix_map[prefix].append(word)
    except KeyError:
        # if there is not entry for this predix, make one
        suffix_map[prefix] = [word]
    prefix = shift(prefix, word)
    # print("prefix:", prefix[0], "word:", word)


def shift(t, word):
    return t[1:]+(word,)


def random_text(n=100):
    start = random.choice(list(suffix_map.keys()))
    for i in range(n):
        suffixes = suffix_map.get(start)
        if suffixes is None:
            random_text(n-i)
            return

        word = random.choice(suffixes)
        print(word, end='')
        start = shift(start, word)




# markov("book/zx.txt", 2)
# markov("book/doupo.txt", 2)
markov("book/jpm.txt", 2)
print(len(suffix_map.keys()))
random_text(500)