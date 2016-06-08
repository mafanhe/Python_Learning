import math
import string
import matplotlib.pyplot as plt
from analyze_book1 import skip_gutenberg_header


def file2dict(filename):
    d = dict()
    with open(filename) as fp:
        skip_gutenberg_header(fp)
        for line in fp:
            process_line(line, d)
    return d


def process_line(line, d):
    line = line.replace('-', ' ')
    strippables = string.punctuation + string.whitespace
    for word in line.rstrip().split():
        word = word.strip(strippables)
        word = word.lower()
        d[word] = d.setdefault(word, 0) + 1



def main():
    d = file2dict("book/emma.txt")
    d2 = sorted(d.items(), key=lambda t: t[1], reverse=True)
    word_sum = sum(d.values())
    i=1

    for (key, value) in d2:
        print("{0:10s} {1:10f} {2:10f}".format(key, math.log10(int(value)/word_sum), math.log10(i)))
        i += 1



if __name__ == "__main__":
    main()
