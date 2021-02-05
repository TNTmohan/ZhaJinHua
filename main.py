from Poker import *
from Game import Game
from Player import Player

if __name__ == '__main__':
    playerNameList = ['ntt', 'wby', 'lhq']  # , 'wqw', 'dlf', 'kxm', 'njq']
    players = [Player(name) for name in playerNameList]
    game = Game(players, 0)
    for i in range(3):
        print('*' * 15 + '第' + str(i + 1) + '局' + '*' * 15)
        game.licensing()
        game.showAllPair()
        while game.isGameEnd() is not True:
            for index, player in enumerate(players):
                if game.getPlayerState()[index] is not True:
                    continue
                print('轮到玩家' + player.getName() + '说话，请输入命令')
                print('[0]跟注, [1]加注, [2]弃牌, [3]看牌')
                order = int(input())
                if order == 0:
                    player.call()
                elif order == 1:
                    player.Raise()
                elif order == 2:
                    player.quit()
                elif order == 3:
                    player.flop()  # 这里先简单认为看牌后必须跟注，且不存在重复看牌的情况
                    player.call()

        game.resetGame()
