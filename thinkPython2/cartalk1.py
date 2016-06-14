__author__ = 'mafanhe'


def car_talk1(word):
    if len(word) < 6:
        return False
    for i in xrange(len(word)-5):
        if word[i] == word[i+1] and word[i+2] == word[i+3] and word[i+4] == word[i+5]:
            return True
    return False


def is_palindrome(word):
    return is_reverse(word,word)


def is_reverse(word1,word2):
    return 1 if word1 == word2[::-1] else 0


def car_talk2():
    for i in range(100000, 999999):
        last_four = str(i)[2:]
        last_five = str(i+1)[1:]
        middle_four = str(i+2)[1:5]
        six = str(i+3)[:]
        if reduce(lambda x, y: x*y, map(lambda x: is_palindrome(x), [last_four, last_five, middle_four, six])):
            print i


def car_talk3():
    for age in xrange(1, 100):
        son_age = 0
        mather_age = age
        count = 0
        for i in xrange(100):
            son_age += 1
            mather_age += 1
            # print(son_age, mather_age)
            if is_reverse(str(son_age), str(mather_age)):
                count += 1
                # print "*"*7
        # print age, count
        if count == 8:
            my_age = 0
            my_mather = age
            six_count = 0
            for i in xrange(100):
                my_age += 1
                my_mather += 1
                if six_count == 6:
                    print my_age, my_mather
                    return mather_age, my_mather
                if is_reverse(str(my_age), str(my_mather)):
                    six_count += 1



car_talk3()
# fin = open("word.txt")
# for line in fin:
#     word = line.strip()
#     if car_talk1(word):
#         print word
# fin.close()
