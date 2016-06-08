__author__ = 'mafanhe'


def avoids(word, char):
    return True if char not in word else False


def func(char):
    count = 0
    fin = open('word.txt')
    for line in fin:
        word = line.strip()
        if avoids(word, 'a'):
            count += 1
    fin.close()
    return count


def uses_only(word, letters):
    return 1 if set(letters).issuperset(set(word)) else 0


def uses_all(word, letters):
    return uses_only(letters, word)


def has_no_e(word):
    for letter in word:
        if letter == 'e':
            return False
    return True


def avoids(word, forbidden):
    for letter in word:
        if letter in forbidden:
            return False
    return True


def is_abecedarian(word):
    previous = word[0]
    for c in word:
        if c < previous:
            return False
        previous = c
    return True


fin = open('word.txt')
for line in fin:
    word = line.strip()
    if uses_all(word, 'aeiouy'):
        print word

fin.close()


