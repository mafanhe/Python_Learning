"""This module contains a code example related to

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/
"""

from Card import Hand, Deck

class Hist(dict):
    def __init__(self, seq=[]):
        for x in seq:
            self.count(x)

    def count(self, x, f=1):
        self[x] = self.get(x,0) + f
        if self[x] == 0:
            del self[x]

class PokerHand(Hand):
    """Represents a poker hand."""

    all_labels = ['straightflush', 'fourkind', 'fullhouse', 'flush',
                  'straight', 'threekind', 'twopair', 'pair', 'highcard']

    def make_histogram(self):
        self.suits = Hist()
        self.ranks = Hist()

        for c in self.cards:
            self.suits.count(c.suit)
            self.ranks.count(c.rank)

        self.sets = list(self.ranks.values())
        self.sets.sort(reverse=True)

    def check_sets(self, *t):
        for need, hava in zip(t, self.sets):
            if need > hava:
                return False
        return True

    def in_a_row(self, ranks, n=5):
        count = 0
        for i in range(1, 15):
            if ranks.get(i, 0):
                count += 1
                if count == n:
                    return True
            else:
                count = 0
        return False

    def has_highcard(self):
        """Returns True if this hand has a high card."""
        return len(self.cards)

    def has_flush(self):
        """ 同花 """
        for val in self.suits.values():
            if val >= 5:
                return True
        return False

    def has_pair(self):
        return self.check_sets(2)

    def has_twopair(self):
        return self.check_sets(2, 2)

    def has_threekind(self):
        return self.check_sets(3)

    def has_fourkind(self):
        return self.check_sets(4)

    def has_fullhouse(self):
        return self.check_sets(3, 2)

    def has_straight(self):
        """ 顺子 """
        ranks = self.ranks
        ranks[14] = ranks.get(1, 0)
        return self.in_a_row(ranks, 5)

    def has_straightflush2(self):
        """ 同花顺 """
        # 创建一个(rank, suit)对的集合
        s = set()
        for c in self.cards:
            s.add((c.rank, c.suit))
            if c.rank == 1:
                s.add((14, c.suit))
        # 迭代花色和等级，判断是否时顺子
        for suit in range(4):
            count = 0
            for rank in range(1, 15):
                if (suit, rank) in s:
                    count += 1
                    if count == 5:
                        return True
                else:
                    count = 0
        return False

    def has_straightflush(self):
        # 已花色为key的字典
        d = {}
        for c in self.cards:
            d.setdefault(c.suit, PokerHand()).add_card(c)

        for hand in d.values():
            if len(hand.cards) < 5:
                continue
            hand.make_histogram()
            if hand.has_straight():
                return True
        return False

    def classify(self):
        self.make_histogram()
        self.labels=[]

        for label in PokerHand.all_labels:
            f = getattr(self, 'has_'+label)
            if f():
                self.labels.append(label)


class PokerDeck(Deck):
    """ a deck of cards """
    def deal_hands(self, hand_num=10, card_num=5):
        hands = []
        for i in range(hand_num):
            hand = PokerHand()
            self.move_cards(hand, card_num)
            hand.classify()
            hands.append(hand)
        return hands


def main():
    # the label histogram: map from label to number of occurances
    lhist = Hist()

    # loop n times, dealing 7 hands per iteration, 7 cards each
    n = 10000
    for i in range(n):
        if i % 1000 == 0:
            print(i)

        deck = PokerDeck()
        deck.shuffle()

        hands = deck.deal_hands(7, 7)
        for hand in hands:
            for label in hand.labels:
                lhist.count(label)

    # print the results
    total = 7.0 * n
    print(total, 'hands dealt:')

    for label in PokerHand.all_labels:
        freq = lhist.get(label, 0)
        if freq == 0:
            continue
        p = total / freq
        print('%s happens one time in %.2f' % (label, p))


if __name__ == '__main__':
    main()
