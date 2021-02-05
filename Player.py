from Poker import Poker


class Player:
    def __init__(self, name, money=2000):
        self._name = name
        self._money = money
        self._currentGame = None
        self._currentIndex = None

    def getName(self):
        return self._name

    def shufflePoker(self):
        self._currentGame.shuffle()
        print("Player " + self._name + ' has shuffled poker.')

    def enterGame(self, game, index):
        self._currentGame = game
        self._currentIndex = index
        print('Player ' + self._name + ' has entered game ' + str(game.getId()) + '!')

    def call(self):
        chip = self._currentGame.recall(self._currentIndex)
        self._money -= chip
        print('%s跟注了%d个筹码' % (self._name, chip))

    def quit(self):
        self._currentGame.reQuit(self._currentIndex)
        print('%s弃牌了' % self._name)

    def Raise(self, rate=2):
        chip = self._currentGame.reRaise(self._currentIndex, rate)
        self._money -= chip
        print('%s加注了%d个筹码' % (self._name, chip))

    def flop(self):
        cardsStr = self._currentGame.reFlop(self._currentIndex)
        print('你的牌是: ' + cardsStr)

    def winGame(self, money):
        self._money += money

