class Board():
    def __init__(self, bounds = None):
        if bounds == None:
            self.bounds = (10, 20)  #standard
        else:
            self.bounds = bounds

        #the entry will be a color value, the coords will be the index there
        self.grid = [(0,0,0)]*(self.bounds[0]*self.bounds[1])
        
    def get_width(self):
        return self.bounds[0]
    def get_height(self):
        return self.bounds[1]

    def get_grid(self):
        return self.grid
    
    def end_round(self, coords, color): 
        #you can use .pop() to remove an index
        #add coords to list of blocks stuck to the board
        for coord in coords:
            if coord[1] >= 0 and coord[0] >= 0:
                try: 
                    print("trying to add coords to grid")
                    print("row: ", coord[1])
                    print("column: ", coord[0])
                    self.grid[coord[1]*self.bounds[0] + coord[0]] = color
                except:
                    print("end round fail coord", coord)
        self.print_grid()
        

    def check_coords(self, coords):

        for coord in coords:
            if coord[0] > self.bounds[0]-1 or coord[0] < 0:
                return False
            if coord[1] > self.bounds[1]-1:
                return False
            
            if coord[0] >= 0 and coord[1] >= 0:
                try:
                    if self.grid[coord[1]*self.bounds[0] + coord[0]] is not (0,0,0):
                        return False
                except:
                    print("failed coords in check_coords: ", coord)
                    print("column len: ", len(self.grid))
                    print("row len: ", len(self.grid[0]))
        
        return True


    def print_grid(self):

        for i in range(0, self.bounds[1]):
            line = []
            for j in range(0, self.bounds[0]):
                line.append(self.grid[i * self.bounds[0]] + j)
            print(line)