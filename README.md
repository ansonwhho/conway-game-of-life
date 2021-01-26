# John Conway's Game of Life
## Description
This is an interactive implementation of [John Conway's game of life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life) using Python 3 and Pygame. The basic rules of the game are (from Wikipedia): 

> 1. Any live cell with two or three live neighbours survives.
> 2. Any dead cell with three live neighbours becomes a live cell.
> 3. All other live cells die in the next generation. Similarly, all other dead cells stay dead.

The game starts off in a *dead state* by default, where a blank grid is displayed. The option is provided to set the state to a *random state*, or a particular initial state can be set up by clicking on desired squares (i.e. *mouse editing*). To run or move to the next iteration, mouse editing must be disabled. "Runs" or automatic iterations can be paused, and after enabling mouse editing the new state can then be modified. 

## Controls
Note that some keys will not work unless certain conditions are met. These are described in italics. 

- **SPACE**: Enable/disable mouse editing. 
- **RIGHT_ARROW**: Next iteration of Life. *Requires disabled mouse editing.*
- **P**: Play/pause automatic iterations. *Requires disabled mouse editing.*
- **D**: Dead state, or an empty board. *Requires disabled mouse editing.*
- **R**: Random state. *Requires disabled mouse editing.*

When mouse editing is enabled, squares can be clicked on to change their state. Live cells are blue and dead cells are white. Other features like the board size, rate of iteration, colours, etc. are defined in the "constants.py" file. 

## Inspiration
Inspiration for this project came from reading about my university course, [MT4512 Automata, Languages and Complexity](https://www.st-andrews.ac.uk/subjects/modules/catalogue/?code=MT4512&academic_year=2020%2F1). I found [Robert Heaton's blog](https://robertheaton.com/2018/07/20/project-2-game-of-life/) as a helpful starting point. 
