# Packages and libraries
import random
import pygame

class gridstate:
    """Possible board states of Life. State = 2D array. gridstate is the class."""
    def __init__(self, rows, cols): # Dead state by default
        self.rows = rows
        self.cols = cols
        self.size = (rows, cols)
        self.array = [[0] * cols for row in range(rows)]
    
    def dead_state(self): 
        self.array = [[0] * self.cols for row in range(self.rows)]
        return self
    
    # randomise the state of each cell
    def random_state(self):
        for i in range(self.rows):
            for j in range(self.cols): 
                self.array[i][j] = random.randint(0, 1)
        return self
    
    def get_neighbours(self, i, j): # want total neighbours for state[i][j]
        neighbours = 0
        state = [row[:] for row in self.array]
        rows = self.rows
        cols = self.cols

        if i % (rows - 1) != 0 and j % (cols - 1) != 0: # non-edge cases
            for x in range(-1, 2):
                for y in range(-1, 2):
                    neighbours += state[i+x][j+y]
            neighbours -= state[i][j]
        
        # Edge cases - alternative formulation is to have the grid loop round on itself like a torus
        # Corners have 3 neighbours
        elif (i == 0) and (j == 0): # Top left corner - state[0][0]
            neighbours = state[0][1] + state[1][0] + state[1][1]
        elif (i == 0) and (j == cols - 1): # Bottom left corner - state[0][cols-1]
            neighbours = state[0][cols-2] + state[1][cols-2] + state[1][cols-1]
        elif (i == rows - 1) and (j == 0): # Top right corner - state[rows-1][0]
            neighbours = state[rows-2][0] + state[rows-2][1] + state[rows-1][1]
        elif (i == rows - 1) and (j == cols - 1): # Bottom right corner - state[rows-1][cols-1]
            neighbours = state[rows-2][cols-2] + state[rows-2][cols-1] + state[rows-1][cols-2]

        # Edges have 5 neighbours
        elif i == 0: # top row
            neighbours = state[i][j-1] + state[i][j+1]
            for k in range(-1, 2):
                neighbours += state[i+1][j+k]
        elif i == rows - 1: # bottom row
            neighbours = state[i][j-1] + state[i][j+1]
            for k in range(-1, 2):
                neighbours += state[i-1][j+k]
        elif j == 0: # left column
            neighbours = state[i-1][j] + state[i+1][j]
            for k in range(-1, 2):
                neighbours += state[i+k][j+1]
        elif j == cols - 1: # right column
            neighbours = state[i-1][j] + state[i+1][j]
            for k in range(-1, 2):
                neighbours += state[i+k][j-1]

        return neighbours

    def next_board_state(self): 
        new_state = [row[:] for row in self.array] # initialise a state
        rows = self.rows
        cols = self.cols

        for i in range(rows):
            for j in range(cols):
                neighbours = self.get_neighbours(i,j)
                state = self.array[i][j]
                if state == 1:
                    if neighbours < 2 or neighbours > 3: # rules 1 and 3
                        new_state[i][j] = 0
                    else: # rule 2
                        new_state[i][j] = 1
                elif (state == 0) and (neighbours == 3): # rule 4
                    new_state[i][j] = 1
                else: # remaining neighbours stay the same
                    new_state[i][j] = state

        self.array = new_state
        return self