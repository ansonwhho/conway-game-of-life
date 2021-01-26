# Set up
import pygame
import constants
import grid
import states

def main():
    # Start simulation
    pygame.init()

    # Window, fill and caption
    win = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    pygame.display.set_caption(constants.TITLE)
    win.fill(constants.BLACK)

    # Simulation square coordinates
    cells = grid.grid_cells(win, constants.ROWS, constants.COLS, constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)

    # Simulation appearance
    # Arrays from state
    current_state = states.gridstate(constants.ROWS, constants.COLS) # Dead state by default
    click_mode = True # Clicking the board enabled

    # Simulation setup
    run = False # Not iterating forward by default
    clock = pygame.time.Clock()
    iteration = 0

    # Game loop
    while True:
    
        # Draw the grid
        for row in range(constants.ROWS):
            for col in range(constants.COLS):
                if click_mode == True:
                    cells[row][col].draw_cell(win)
                else:
                    if current_state.array[row][col] == 1:
                        pygame.draw.rect(win, constants.BLUE, (col * constants.SQR_WIDTH, row * constants.SQR_HEIGHT, constants.SQR_WIDTH, constants.SQR_HEIGHT))
                    elif current_state.array[row][col] == 0:
                        pygame.draw.rect(win, constants.WHITE, (col * constants.SQR_WIDTH, row * constants.SQR_HEIGHT, constants.SQR_WIDTH, constants.SQR_HEIGHT))

        # Iterate automatically
        if run == True and click_mode == False:
            clock.tick(constants.FPS)
            current_state.array = current_state.next_board_state().array
            iteration += 1

        # User interaction 
        for event in pygame.event.get():
            # Quit Game of Life
            if event.type == pygame.QUIT: 
                pygame.quit()
                quit()

            # Clicks and mouse movements    
            # Find the cell the cursor is in
            pos = pygame.mouse.get_pos()
            cell_i, cell_j = pos[1] // constants.SQR_WIDTH, pos[0] // constants.SQR_HEIGHT

            # Setting up the grid - which cells dead or alive
            if event.type == pygame.MOUSEBUTTONDOWN and click_mode == True: # Click on cell to make dead or alive
                if current_state.array[cell_i][cell_j] == 0:
                    current_state.array[cell_i][cell_j] = 1
                elif current_state.array[cell_i][cell_j] == 1:
                    current_state.array[cell_i][cell_j] = 0
                    
            if event.type == pygame.MOUSEMOTION and click_mode == True: # Turn cell red when hovering over
                for row in range(constants.ROWS):
                    for col in range(constants.COLS):
                        if row == cell_i and col == cell_j:
                            cells[row][col].colour = constants.RED
                        elif current_state.array[row][col] == 0:
                            cells[row][col].colour = constants.WHITE
                        elif current_state.array[row][col] == 1:
                            cells[row][col].colour = constants.BLUE

            # Key presses  
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE: # Click mode on/off
                    if click_mode == False:
                        click_mode = True
                    else:
                        click_mode = False
                if event.key == pygame.K_RIGHT and click_mode == False: # Next state
                    current_state.array = current_state.next_board_state().array
                    iteration += 1
                if event.key == pygame.K_r and click_mode == False: # Random state
                    current_state.array = current_state.random_state().array
                    iteration = 0
                if event.key == pygame.K_d and click_mode == False: # Dead state
                    current_state.array = current_state.dead_state().array
                    iteration = 0
                if event.key == pygame.K_p and click_mode == False: # Change whether iterating automatically
                    if run == False:
                        run = True
                    else:
                        run = False

        # Update pygame display
        grid.show_iteration(win, iteration, constants.FONT_NAME, constants.FONT_SIZE, constants.RED, constants.TEXT_X, constants.TEXT_Y)
        pygame.display.update()

if __name__ == "__main__":
    main()