import collections
from random import shuffle


class Card:
    def __init__(self, suit, rank):
        self._suit = suit
        self._rank = rank
        self._value = Poker.ranks.index(rank) * 10 + Poker.suits.index(suit)

    def __str__(self):
        return self._suit + self._rank

    def __lt__(self, other):
        return self.getValue() < other.getValue()

    def getSuit(self):
        return self._suit

    def getRank(self):
        return self._rank

    def getValue(self):
        return self._value

    def getSuitIndex(self):
        return self._value % 10 + 1

    def getRankIndex(self):
        return self._value // 10 + 1






class Poker:
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    suits = ['♦', '♥', '♣', '♠']

    def __init__(self):
        self._cards = [Card(suit, rank) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

    def shuffle(self):
        shuffle(self._cards)

    def cut(self):
        print('Poker has been cut.')

    def reset(self):
        self._cards = [Card(suit, rank) for suit in self.suits for rank in self.ranks]

    def showAllCard(self):
        [print(card) for card in self._cards]




if __name__ == '__main__':
    poker = Poker()
    poker.showAllCard()
    poker.shuffle()
    poker.showAllCard()
