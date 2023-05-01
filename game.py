import pygame
from pygame.time import Clock



class Game():
    def __init__(self, piece=None, board=None):
        self.current_piece = piece
        self.board = board
        self.screen = pygame.display.set_mode((self.board.bounds[0], self.board.bounds[1]))
        
    def run(self):
        self.running = True
        clock = Clock()
        while(self.running):
            for event in pygame.event.get():
                pass
            
            self.board.render()
            self.current_piece.render()
            pygame.draw.rect(self.screen, (100,0,0), (0,0,self.board.bounds[0], self.board.bounds[1]))
            pygame.display.flip()
            clock.tick(18)