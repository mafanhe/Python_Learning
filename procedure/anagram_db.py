import shelve
from anagram_sets import all_anagrams,signature


def store_anagrams(filename, anagram_map):
    shelf = shelve.open(filename, 'c')
    for word, word_list in anagram_map.items():
        shelf[word] = word_list
    shelf.close()


def read_anagrams(filename, word):
    shelf = shelve.open(filename)
    sig = signature(word)
    try:
        return shelf[sig]
    except KeyError:
        return []



def main():
    anagram_map = all_anagrams("book/words.txt")
    # store_anagrams("book/anagram_db", anagram_map)
    # print (read_anagrams("book/anagram_db", "stop"))
    for word,wordList in anagram_map.items():
        if len(wordList)>1:
            print(word,wordList)


if __name__ == "__main__":
    main()

