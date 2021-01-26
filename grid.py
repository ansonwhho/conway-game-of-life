# Set up
import pygame
import constants
import states

class cell():
    """Clickable rectangular cells"""
    def __init__(self, colour, x, y, width, height):
        self.colour = colour
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw_cell(self, screen):
        pygame.draw.rect(screen, self.colour, (self.x, self.y, self.width, self.height))

def grid_cells(screen, rows, cols, width, height):
    sqr_width = int(width // cols)
    sqr_height = int(height // rows)
    cells = []

    # Map the screen with square (rectangular) cells
    for j in range(rows):
        row = []
        for i in range(cols):
            x = i * sqr_width
            y = j * sqr_height
            row.append(cell(constants.WHITE, x, y, sqr_width, sqr_height))
        cells.append(row)
    return cells

class button():
    """Button to start and stop the simulation"""
    def __init__(self, colour, x, y, width, height):
        self.colour = colour
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    
    def draw_square(self, win):
        pygame.draw.rect(win, self.colour, (self.x,self.y,self.width,self.height))
    
    def draw_triangle(self, win, coords):
        pygame.draw.polygon(win, self.colour, coords)

def show_iteration(win, iteration, font_name, font_size, font_colour, x, y):
    font = pygame.font.Font(font_name, font_size)
    it_num = font.render("ITERATION : " + str(iteration), True, font_colour)
    win.blit(it_num, (x, y))