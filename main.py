from Poker import *
from Game import Game
from Player import Player

if __name__ == '__main__':
    playerNameList = ['ntt', 'wby', 'lhq', 'wqw', 'dlf', 'kxm', 'njq']
    players = [Player(name) for name in playerNameList]
    game = Game(players, 0)
    players[0].shufflePoker()
    game.licensing()
    game.showAllPair()