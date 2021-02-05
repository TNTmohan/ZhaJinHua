from Poker import *


class Pair:
    def __init__(self, cards=[]):
        self._cards = cards
        self.sortPair()
        self._value = self._getValue()

        # todo 可以加一些数据结构储存牌的Inedx信息方便比较大小

    def __str__(self):
        return ', '.join([str(card) for card in self._cards])

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
                    return self._cards[2].getRankIndex() * 16 ** 6 + \
                           self._cards[1].getRankIndex() * 16 ** 5 + self._cards[2].getRankIndex() * 16 ** 4
                else:
                    return self._cards[2].getRankIndex() * 16 ** 4 + \
                           self._cards[1].getRankIndex() * 16 ** 3 + self._cards[2].getRankIndex() * 16 ** 2
            else:
                if self.isShunJin():
                    return 2 * 16 ** 6 + 1 * 16 ** 5 + 13 * 16 ** 4
                else:
                    return 2 * 16 ** 4 + 1 * 16 ** 3 + 13 * 16 ** 2
        if self.isJinHua():
            return self._cards[2].getRankIndex() * 16 ** 5 + \
                   self._cards[1].getRankIndex() * 16 ** 4 + self._cards[0].getRankIndex() * 16 ** 3
        if self.isDuiZi():
            if self._cards[0].getRankIndex() == self._cards[1].getRankIndex():
                return self._cards[0].getRankIndex() * 16 ** 3 + self._cards[2].getRankIndex() * 16 ** 2
            else:
                return self._cards[2].getRankIndex() * 16 ** 3 + self._cards[0].getRankIndex() * 16 ** 2
        else:
            return self._cards[2].getRankIndex() * 16 ** 2 + \
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
        self._flopState = [False] * self._lenPlayer
        self._chipPool = 0
        self._baseChip = 10
        [player.enterGame(self, index) for index, player in enumerate(players)]

    def shuffle(self):
        self._poker.shuffle()
        print('牌已经洗好了')

    def getId(self):
        return self._id

    def getPlayerState(self):
        return self._playersState.copy()

    def licensing(self):
        self.shuffle()
        for index in range(self._lenPlayer):
            cards = [self._poker[index + i * self._lenPlayer] for i in range(3)]
            self._pairs.append(Pair(cards))
            self._players[index]


    def showPair(self, playerId):
        print('Player ' + self._players[playerId].getName() + ' has: ', str(self._pairs[playerId]) +
              ' Value is ' + str(self._pairs[playerId].getValue()))

    def showAllPair(self):
        [self.showPair(i) for i in range(self._lenPlayer)]

    def recall(self, playlerIndex):
        chip = (self._flopState[playlerIndex] + 1) * self._baseChip
        self._chipPool += chip
        return chip

    def reRaise(self, playerIndex, rate):
        self._baseChip *= rate
        chip = self.recall(playerIndex)
        return chip

    def reQuit(self, playerIndex):
        self._playersState[playerIndex] = False

    def reFlop(self, playerIndex):
        self._flopState[playerIndex] = True
        return str(self._pairs[playerIndex])

    def resetGame(self):
        self._poker.reset()
        self._pairs = []
        self._chipPool = 0
        self._baseChip = 10
        self._playersState = [0] * self._lenPlayer

    def isGameEnd(self):
        return sum(self._playersState) == 1

    def endGame(self):
        winner = self._players[self._playersState.index(True)]
        print('本局游戏结束，获胜者为' + winner.getName())
        winner.winGame(self._chipPool)
        self.resetGame()


