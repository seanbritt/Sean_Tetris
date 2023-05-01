
from pieces import *
from board import *
from game import *
from controls import *

if __name__ == "__main__":
    piece = Piece(1)
    board = Board()
    game = Game(board=board,piece=piece)
    game.run()