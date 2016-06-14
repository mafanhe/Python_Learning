__author__ = 'mafanhe'


def rotate_letter(letter, num):
    if letter.isupper():
        start = ord('A')
    elif letter.islower():
        start = ord('a')
    else:
        return letter
    return chr((ord(letter)-start+num) % 26+start)


def rotate_word(strs, num):
    new_str = ""
    for s in strs:
        new_str += rotate_letter(s, num)
    return new_str

print rotate_word("love", 1)