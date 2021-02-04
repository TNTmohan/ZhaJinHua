from Poker import Poker


class Player:
    def __init__(self, name, money=2000):
        self._name = name
        self._money = money
        self._currentGame = None

    def getName(self):
        return self._name

    def shufflePoker(self):
        self._currentGame.getPoker().shuffle()
        print("Player " + self._name + ' has shuffled poker.')


    @staticmethod
    def cutPoker(poker):
        poker.cut()

    def enterGame(self, game):
        self._currentGame = game
        print('Player ' + self._name + ' has entered game ' + str(game.getId()) + '!')
