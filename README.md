# The-Life-Game
The Game of Life is an implementation of the cellular automaton designed by the British mathematician John Horton Conway.

## Rules

- A dead cell with exactly 3 live neighbors will live.
- A living cell with 2 or 3 living neighbors will remain alive.

- If a cell has less than 2 living neighbors it will die of loneliness.

- If a cell has more than 3 living neighbors it will die of overpopulation.


## Installation
- clone the repository

    `git clone https://github.com/Mitchell-Mirano/The-Life-Game.git`

- Install python virtual environment

    `python3 -m venv env`

- Activate the virtual environment

    `source env/bin/activate`

- Install the dependencies

    `pip install -r requirements.txt`

- Run the game

    `python life.py`

## Usage

In the game window press the game pause key and draw the initial population of cells with the maus

 - If you click on a cell it will live. 
 - If you anti-click on a live cell this cell will die.


