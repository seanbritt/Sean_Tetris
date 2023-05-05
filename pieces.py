#first four are the coordinates
# last is the location of the 'center'

import random

SQUARE = [  
    [0,0],
    [0,-1],
    [-1,0],
    [-1,-1]
]
# TEE = ((0,1,2),(1),(1))
# J_LEFT = ((1),(1),(0,1))
# J_RIGHT = ((0),(0),(0,1))
# S_LEFT = ((0,1),(1,2))
# S_RIGHT = ((1,2),(0,1))
# LONG = ((0),(0),(0),(0))

# _OPTIONS = [SQUARE, TEE, J_LEFT,J_RIGHT, S_LEFT, S_RIGHT, LONG]
_OPTIONS = [SQUARE]

class Piece():
    def __init__(self, middle):
        self.coords = _OPTIONS[random.randint(0, len(_OPTIONS)-1)]
        self.position = [middle, 0]
        self.color = (50,220, 50)

    def get_color(self):
        return self.color
    
    def rotate(self, rotation):
        if not rotation:
            return self.coords
        coords = []
        for coord in self.coords:
            coords.append([
                int(-(coord[1]+0.5)-0.5),
                int(coord[0])
            ])
        return coords
    
    def translate(self, direction, rotatedCoords):
        newCoords = []
        for coord in rotatedCoords:
            newCoords.append(
                [(coord[0]+self.position[0]+direction[0]),
                (coord[1]+self.position[1]+direction[1])]
            )
        # print("new coords: ", newCoords[0])
        return newCoords

    def save_move(self, direction, newRot):

        self.coords = newRot
        self.position[0] += direction[0]
        self.position[1] += direction[1]

    # def move(self, direction, rotation):
    #     #rotation is an integer: -1, 0, 1
    #     newCoords = self.rotate(rotation)
    #     newCoords = self.translate(direction, newCoords)
    #     return newCoords
    
    def get_rot(self):
        return self.coords

    def get_coords(self):
        returnCoords = []
        for coord in self.coords:
            returnCoords.append([coord[0]+self.position[0], coord[1]+self.position[1]])
        return returnCoords

