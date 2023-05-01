
SQUARE = ((0,1),(0,1))
TEE = ((0,1,2),(1),(1))
J_LEFT = ((1),(1),(0,1))
J_RIGHT = ((0),(0),(0,1))
S_LEFT = ((0,1),(1,2))
S_RIGHT = ((1,2),(0,1))
LONG = ((0),(0),(0),(0))

OPTIONS = [SQUARE, TEE, J_LEFT,J_RIGHT, S_LEFT, S_RIGHT, LONG]

class Piece():
    def __init__(self, type):
        self.type = OPTIONS[type]
        self.rotation = 0
    def render(self):
        print(self.type)
