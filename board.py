class Board():
    def __init__(self, bounds = None):
        if bounds == None:
            self.bounds = (500, 650)  #standard
        else:
            self.bounds = bounds
        self.pieces = []

    def get_pieces(self):
        return self.pieces
    
    def end_round(self, coords, color): 
        
        #add coords to list of blocks stuck to the board
        for coord in coords:
            self.pieces.append({'color':color, 'coord':coords})
        print("pieces: ", self.pieces)

    def check_coords(self, coords):

        for coord in coords:
            if coord in self.pieces:
                return False
            if coord[0] > self.bounds[0] or coord[0] < 0:
                return False
            if coord[1] > self.bounds[1] or coord[1] < 0:
                return False

        return True
