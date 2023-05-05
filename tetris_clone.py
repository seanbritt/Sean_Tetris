
from pieces import *
from board import *
from game import *
from controls import *

if __name__ == "__main__":
    board = Board()
    game = Game(board=board)
    game.run()