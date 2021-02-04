from Poker import *


class Pair:
    def __init__(self, cards=[]):
        self._cards = cards
        self.sortPair()
        self._value = self._getValue()

        #todo 可以加一些数据结构储存牌的Inedx信息方便比较大小

    def __str__(self):
        return str([str(card) for card in self._cards])

    def __eq__(self, other):
        return self.__hash__() == other.__hash__()

    def __le__(self, other):
        return self.__hash__() < other.__hash__()

    def sortPair(self):
        self._cards = sorted(self._cards)

    def _getValue(self):
        if self.isBaoZi():
            return self._cards[2].getRankIndex() * 16 ** 7
        if self.isShunZi():
            if self._cards[0].getRankIndex() + 2 == self._cards[2]:
                if self.isShunJin():
                    return self._cards[2].getRankIndex() * 16 ** 6 +\
                           self._cards[1].getRankIndex() * 16 ** 5 + self._cards[2].getRankIndex() * 16 ** 4
                else:
                    return self._cards[2].getRankIndex() * 16 ** 4 +\
                           self._cards[1].getRankIndex() * 16 ** 3 + self._cards[2].getRankIndex() * 16 ** 2
            else:
                if self.isShunJin():
                    return 2 * 16 ** 6 + 1 * 16 ** 5 + 13 * 16 ** 4
                else:
                    return 2 * 16 ** 4 + 1 * 16 ** 3 + 13 * 16 ** 2
        if self.isJinHua():
            return self._cards[2].getRankIndex() * 16 ** 5 +\
                           self._cards[1].getRankIndex() * 16 ** 4 + self._cards[0].getRankIndex() * 16 ** 3
        if self.isDuiZi():
            if self._cards[0].getRankIndex() == self._cards[1].getRankIndex():
                return self._cards[0].getRankIndex() * 16 ** 3 + self._cards[2].getRankIndex() * 16 ** 2
            else:
                return self._cards[2].getRankIndex() * 16 ** 3 + self._cards[0].getRankIndex() * 16 ** 2
        else:
            return self._cards[2].getRankIndex() * 16 ** 2 +\
                   self._cards[1].getRankIndex() * 16 + self._cards[0].getRankIndex()

    def getValue(self):
        return self._value

    def isBaoZi(self):
        return self._cards[0].getRankIndex() == self._cards[2].getRankIndex()

    def isJinHua(self):
        return self._cards[0].getSuitIndex() == self._cards[1].getSuitIndex() \
               and self._cards[1].getSuitIndex() == self._cards[2].getSuitIndex()

    def isShunZi(self):
        return self._cards[0].getRankIndex() + 2 == self._cards[2] or \
               (self._cards[0].getRankIndex == 0 and self._cards[1].getRankIndex == 1
                and self._cards[2].getRankIndex == 13)

    def isShunJin(self):
        return self.isJinHua() and self.isShunZi()

    def isDuiZi(self):
        return (self._cards[0].getRankIndex() == self._cards[1].getRankIndex()
                or self._cards[1].getRankIndex() == self._cards[2].getRankIndex()) \
               and self._cards[0].getRankIndex() != self._cards[2].getRankIndex()


class Game:
    def __init__(self, players, gameId):
        self._players = players
        self._id = gameId
        self._poker = Poker()
        self._lenPlayer = len(players)
        self._pairs = []
        self._playersState = [True] * self._lenPlayer
        self._chipPool = 0
        [player.enterGame(self) for player in players]

    def getId(self):
        return self._id

    def getPoker(self):
        return self._poker

    def licensing(self):
        for index in range(self._lenPlayer):
            cards = [self._poker[index+i*self._lenPlayer] for i in range(3)]
            self._pairs.append(Pair(cards))

    def showPair(self, playerId):
        print('Player ' + self._players[playerId].getName() + ' has: ', str(self._pairs[playerId]) +
              ' Value is ' + str(self._pairs[playerId].getValue()))

    def showAllPair(self):
        [self.showPair(i) for i in range(self._lenPlayer)]

    def resetGame(self):
        self._poker.reset()
        self._pairs = []
        self._chipPool = 0
        self._playersState = [True] * self._lenPlayer

    def endGame(self):
        self._players[self._playersState.index(True)].addMoney(self._chipPool)



