import pygame
from pygame.time import Clock
from pieces import *
from board import *
from game import *
from controls import *

_BOUNDARY = 50
_PIECE_SIZE = 20


class Game():
    def __init__(self, piece=None, board=None):
        self.board = board
        self.current_piece = Piece(int((self.board.bounds[0])/2))
        self.window = pygame.display.set_mode((self.board.bounds[0]*_PIECE_SIZE+_BOUNDARY*2, self.board.bounds[1]*_PIECE_SIZE+_BOUNDARY*2))
        self.boardScreen = pygame.Surface((self.board.bounds[0]*_PIECE_SIZE, self.board.bounds[1]*_PIECE_SIZE))

    def run(self):
        running = True
        clock = Clock()
        drop_counter = 0
        oldCoords = self.current_piece.get_coords()
        oldRotation = self.current_piece.get_rot()
        while(running):

            #get rotation and direction choices
            roundCheck = False
            rotation = False
            direction = [0,0]       #0 is nothing, -1 is left, 1 is right, 2 is down
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        rotation = True
                    if event.key == pygame.K_LEFT:
                        direction[0] = -1
                    if event.key == pygame.K_RIGHT:
                        direction[0] = 1
                    if event.key == pygame.K_DOWN:
                        direction[1] = 1
                        drop_counter = 0
                if event.type == pygame.QUIT:
                    running = False
                    break
            
            #the piece has to drop 
            drop_counter = (drop_counter + 1) % 5
            if drop_counter == 0:
                direction[0] = 0
                direction[1] = 1
                rotation = False
                roundCheck=True

            #calculate the move and check if it's legal
            rotatedCoords = self.current_piece.rotate(rotation)
            newCoords = self.current_piece.translate(direction, rotatedCoords)
            if not self.board.check_coords(newCoords):
                newCoords = oldCoords
                if roundCheck == True:
                    roundCheck = False

                    #do all the board resolution in this step
                    print(newCoords)
                    self.board.end_round(newCoords, self.current_piece.get_color())


                    #get a new piece and see if it overlaps anything on the board
                    self.current_piece = Piece(int((self.board.bounds[0])/2))
                    newCoords = self.current_piece.get_coords()
                    if not self.board.check_coords(newCoords):
                        running = False
                        print("you lose")
                    oldRotation = self.current_piece.get_rot()
            else:
                self.current_piece.save_move(direction, rotatedCoords)
            
            #now render everything with the new coordinates
            self.render(newCoords)
        
            oldCoords = newCoords
            #final rendering
            pygame.display.flip()
            clock.tick(18)


    def render(self, currentCoords):
        #render the viewing window
        self.window.fill((100,100,200))
        self.boardScreen.fill((0,0,0))

        #render the pieces
        grid = self.board.get_grid()
        for i in range(0, self.board.get_height()):
            for j in range(0, self.board.get_width()):
                pygame.draw.rect(self.boardScreen, grid[i*self.board.get_width() + j], (i*_PIECE_SIZE, j*_PIECE_SIZE, _PIECE_SIZE, _PIECE_SIZE))

        #render the piece
        for coord in currentCoords:
            pygame.draw.rect(self.boardScreen, self.current_piece.get_color(), (coord[0]*_PIECE_SIZE, coord[1]*_PIECE_SIZE, _PIECE_SIZE, _PIECE_SIZE))

        #blit the board onto the window
        self.window.blit(self.boardScreen, (_BOUNDARY, _BOUNDARY))