# -*-coding:utf-8 -*-
import random


class Card:
    """代表一张卡牌"""
    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7',
                  '8', '9', '10', 'Jack', 'Queen', 'King']

    def __init__(self, suit=0, rank=2,):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return "%s of %s" % (Card.rank_names[self.rank],
                             Card.suit_names[self.suit])

    def __lt__(self, other):
        # if self.suit < other.suit:
        #     return True
        # if self.suit > other.suit:
        #     return False
        # # 花色相同。。。判断等级
        # return self.rank < other.rank
        t1 = self.suit, self.rank
        t2 = other.suit, other.rank
        return t1 < t2

    def __eq__(self, other):
        return self.suit == other.suit and self.rank == other.rank


class Deck:
    """ 一副牌 """
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)

    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return "\n".join(res)

    def pop_card(self):
        return self.cards.pop()

    def add_card(self, card):
        self.cards.append(card)

    def remove_card(self, card):
        self.cards.remove(card)

    def shuffle(self):
        return random.shuffle(self.cards)

    def sort(self):
        self.cards.sort()

    def move_cards(self, hand, num):
        for i in range(num):
            hand.add_card(self.pop_card())

    # def deal_hands(self, hand_num, card_num):
    #     hands = []
    #     for i in range(hand_num):
    #         hand = Hand()
    #         self.move_cards(hand, card_num)
    #         hands.append(hand)
    #     return hands


class Hand(Deck):
    """ 代表手牌 """
    def __init__(self, label=''):
        self.cards = []
        self.label = label


def find_defining_class(obj, method_name):
    """Finds and returns the class object that will provide
    the definition of method_name (as a string) if it is
    invoked on obj.

    obj: any python object
    method_name: string method name
    """
    for ty in type(obj).mro():
        if method_name in ty.__dict__:
            return ty
    return None

