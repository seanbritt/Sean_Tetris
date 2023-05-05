#first four are the coordinates
# last is the location of the 'center'

import random

SQUARE = {'coords':[
        [-1,-1],[0,-1],
        [-1,0],[0,0]
    ],'color':(200,0,0)
}

TEE = {'coords':[
           [0,-1],
    [-1,0],[0,0],[1,0],
    ],'color':(0,200,0)
}

J_LEFT = {'coords':[
               [0,-2],
               [0,-1],
        [-1,0],[0,0]
    ],'color':(0,0,200)
}
J_RIGHT = {'coords':[
        [0,-2],
        [0,-1],
        [0,0], [1,0]
    ],'color':(200,0,200)
}
S_LEFT = {'coords':[
    [-1,-1],[0,-1], 
            [0,0],[1,0]
    ],'color':(0,200,200)
}
S_RIGHT = {'coords':[
            [0,-1],[1,-1],
     [-1,0], [0,0]
    ],'color':(200,200,0)
}
LONG = {'coords':[
        [-1,0],[0,0],[1,0],[2,0]
    ],'color':(200,200,200)
}

_OPTIONS = [SQUARE, TEE, J_LEFT,J_RIGHT, S_LEFT, S_RIGHT, LONG]
# _OPTIONS = [LONG]

class Piece():
    def __init__(self, middle):
        shape = _OPTIONS[random.randint(0, len(_OPTIONS)-1)]
        self.coords = shape['coords']
        self.position = [middle, 0]
        self.color = shape['color']

    def get_color(self):
        return self.color
    
    def rotate(self, rotation):
        if not rotation:
            return self.coords
        coords = []
        for coord in self.coords:
            coords.append([
                int(-(coord[1]+1)),
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

