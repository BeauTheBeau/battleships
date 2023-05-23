# Battleships Game

This is a Battleships game created in Python using Object-Oriented Programming. It includes local multiplayer,
single-player vs AI, and online multiplayer modes.

## Contents

- [Section 1: Designing the solution](#"section-1-designing-the-solution--9-marks")
  - [The Introduction](#"the-introduction")
  - [How I will solve the problem](#"how-i-will-solve-the-problem")
  - [Success Criteria](#"success-criteria")
  - [Variables and Data Structures](#"variables-and-data-structures")
    - [Variables](#"variables")
    - [Data Structures](#"data-structures")
- [Section 2: Creating the solution](#"section-2-creating-the-solution--30-marks")
  - [Explain sections of your code](#"explain-sections-of-your-code")
- [Section 3: Testing the solution](#"section-3-testing-the-solution--21-marks")
  - [Tests](#"tests")
    - [Evidence of testing](#"evidence-of-testing")
    

## SECTION 1: Designing the solution  (9 marks)


### The Introduction

The problem I am trying to solve is to create a Battleships game that can be played by two players locally, or by one
player against an AI. The game will be played on a 10x10 grid, and each player will have 5 ships to place on the grid.
The ships will be of different sizes, and the players will take turns to guess the location of the other player's ships.
The first player to sink all of the opposing player's ships wins. The game will be played in the console, and will be
created using Object-Oriented Programming. The game will have two modes: local multiplayer and single-player vs AI.

### How I will solve the problem

I will create classes for the game, ships, players and the board. The game class will contain the main game loop, and
will be responsible for running the game. The ships class will contain the attributes of the ships, such as their size
and their location on the board. The players class will contain the attributes of the players, such as their name and
their score. The board class will contain the attributes of the board, such as the grid and the ships.

### Success Criteria

- [ ] The game must be able to be played by two players locally
- [ ] The game must be able to be played by one player against an AI
- [ ] The game must be able to be played on a 10x10 grid
- [ ] The game must have 5 ships of different sizes
- [ ] The game must be created using Object-Oriented Programming
- [ ] The game must have an easy-to-use interface for the players
- [ ] The game must have a main menu with options for the players to choose from

### Variables and Data Structures

#### Variables

Global variables include:

- `SHIP_SIZES` An array containing the sizes of the ships
- `SHIP_NAMES` An array containing the names of the ships
- `SYMBOLS` An array containing symbols for items on the board
- `DEV_MODE` A boolean variable that determines whether the game is in developer mode or not (used for testing)

Other variables are stored in the `__init__` method of the classes. These include:

- `self.name` - The name of the player
- `self.grid` - The grid of the board


#### Data Structures

The data structures used in the game are:
- `Arrays` - Used to store the ship sizes, ship names, symbols and the grid
- `Dictionaries` - Used to store the ship locations and the ship hits
- `Booleans` - Used to store whether the game is in developer mode or not 
- `Integers` - Used to store the player's score and the ship sizes
- `Strings` - Used to store the player's name and the ship names


---

## SECTION 2: Creating the solution (30 marks)

### Explain sections of your code


#### things

```python
# INTITIATION!!!

# Importing modules
import colorama
import numpy as np
from colorama import Fore, Style
import random
import argparse 

# Global variables
SHIP_SIZES = [5, 4, 3, 3, 2]
SHIP_NAMES = ['Carrier', 'Battleship', 'Cruiser', 'Submarine', 'Destroyer']
SYMBOLS = ['S', 'X', '+', 'O', ' ']
DEV_MODE = False

# Flags
parser = argparse.ArgumentParser(description='Battleships game.')
parser.add_argument('--dev', action='store_true', help='Enable developer mode')
args = parser.parse_args()
DEV_MODE = args.dev

# Init colorama for colored outputs
colorama.init()
```


#### Classes

##### Board
```python
# Board class
class Board:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.grid = np.zeros((rows, cols), dtype=int)
        self.ships = []

    def place_ship(self, ship, row, col, direction):
        if direction == 'h':
            for c in range(col, col + ship.size):
                if c >= self.cols or self.grid[row][c] != 0:
                    return False
            for c in range(col, col + ship.size):
                self.grid[row][c] = len(self.ships) + 1
            self.ships.append(ship)
            return True
        else:
            for r in range(row, row + ship.size):
                if r >= self.rows or self.grid[r][col] != 0:
                    return False
            for r in range(row, row + ship.size):
                self.grid[r][col] = len(self.ships) + 1
            self.ships.append(ship)
            return True

    def fire_shot(self, row, col):
        if self.grid[row][col] == 0:
            self.grid[row][col] = -1
            return False
        else:
            ship = self.ships[self.grid[row][col] - 1]
            ship.hits += 1
            self.grid[row][col] = -2
            return True

    def is_game_over(self):
        for ship in self.ships:
            if not ship.is_sunk():
                return False
        return True
```

##### Player class
```python
# Player class
class Player:

    # Initiailsie the player and create a baordc for them
    def __init__(self, name):
        self.name = name
        self.board = Board(10, 10) 

    def place_ships(self, ship_sizes):
        print(f'{self.name.upper()}, place your ships on the board.\n')

        for i, size in enumerate(ship_sizes): # Loop through each possible ship
        
            # Place automatically if dev mode is enabled
            if DEV_MODE:
                self.board.place_ship(Ship(SHIP_NAMES[i], size), i, 0, 'h')
                continue

            while True:
                try: 
                    # Take row, col and direction
                    print(f'Place your {SHIP_NAMES[i]} ({size} spaces):')
                    # row, col, direction = input('> Enter row, column, and direction (h or v): ').split()
                    # row, col = int(row), int(col)

                    # Take row and col
                    print(f'> Place your {SHIP_NAMES[i]} ({size} spaces):')
                    print(f'> EXAMPLE: 0 5')
                    row, col = map(int, input('> Enter row and column: ').split())

                    # Show menu for direction
                    direction = Menu.show_menu('Choose direction', ['Horizontally', 'Vertically'])
                    direction = 'h' if direction == 1 else 'v' # validate the users input and convert to h or v

                    if direction.lower() == 'h':
                        if col + size > 10:
                            print('> Ship is off the board, try again.')
                            continue
                    else:
                        if row + size > 10:
                            print('> Ship is off the board, try again.')
                            continue

                    ship = Ship(SHIP_NAMES[i], size)

                    if self.board.place_ship(ship, row, col, direction):
                        print(f'> Your {SHIP_NAMES[i]} has been placed at ({row}, {col}) going {direction.replace("h", "horizontally").replace("v", "vertically")}.')
                        print()

                        # Print board
                        self.print_board()                        

                        break
                    else:
                        print('> There is already a ship in the way, try again.')
                        print()

                # If the user enters an invalid input, such as a string
                except ValueError: 
                    print('> Invalid input, try again.')
                    print()

    # print the player's own baord, with ships, hits and etc. 
    def print_board(self): 
        colours = [Fore.RED, Fore.GREEN, Fore.BLUE, Fore.YELLOW, Fore.MAGENTA, Fore.CYAN, Fore.WHITE]

        for i, row in enumerate(self.board.grid):
            print(i, end=' ')
            for col in row:
                if col == 0 or col == -1:
                    print('-', end=' ')
                elif col == -2:
                    print('X', end=' ')
                else:
                    print(colours[col - 1] + 'S' + Style.RESET_ALL, end=' ')
            print()
        print(colours[0] + '  0 1 2 3 4 5 6 7 8 9' + Style.RESET_ALL)
        print()

    # print the player's opponent's board, with only hits and misses
    def print_board_opponent(self):
        colours = [Fore.RED, Fore.GREEN, Fore.BLUE, Fore.YELLOW, Fore.MAGENTA, Fore.CYAN, Fore.WHITE]

        for i, row in enumerate(self.board.grid):
            print(i, end=' ')
            for col in row:
                if col == 0 or col == -1:
                    print('-', end=' ')
                elif col == -2:
                    print('X', end=' ')
                else:
                    print('-', end=' ')
            print()
        print(colours[0] + '  0 1 2 3 4 5 6 7 8 9' + Style.RESET_ALL)
```

##### Ship class
```python
# AI class
class AIPlayer(Player):

    # Initialise the class
    def __init__(self):
        super().__init__('AI')

    # Randoml;y place all ships on the board
    def place_ships(self, ship_sizes):
        for i, size in enumerate(ship_sizes):
            while True:
                row = random.randint(0, 9)
                col = random.randint(0, 9)
                direction = random.choice(['h', 'v'])
                ship = Ship(SHIP_NAMES[i], size)
                if self.board.place_ship(ship, row, col, direction):
                    break

    # Fire a shot at the opponent
    def fire_shot(self):
        while True:
            row = random.randint(0, 9)
            col = random.randint(0, 9)
            if self.board.grid[row][col] == 0 or self.board.grid[row][col] == -1:
                break
        return row, col
```

##### Game class
```python
# Game class
class Game:
    # Initialise the game and create the players
    def __init__(self, players):
        self.players = players

    # LET THE GAME BEGIN!!! (game begins)
    def play(self):
        current_player = 0
        opponent_player = 1

        # turn handling
        while True:
            print(f"{self.players[current_player].name}'s turn:")
            print("Your Board:")
            self.players[current_player].print_board()
            print("Opponent's Board:")
            self.players[opponent_player].print_board_opponent()

            while True:
                # Make the player pick a shot
                # If the player is an AI, the AI will pick a shot

                try:
                    row, col = map(int, input("Enter row and column to fire a shot: ").split())
                    if row < 0 or row > 9 or col < 0 or col > 9:
                        raise ValueError
                    break
                except ValueError: 
                    # if input is a string, not an int, then it will raise a ValueError and 
                    # the user will be asked to try again
                    print("> Invalid input, try again.")
                    print()

            # check if is a hit 
            hit = self.players[opponent_player].board.fire_shot(row, col)

            if hit:
                print("> Hit!")
                if self.players[opponent_player].board.is_game_over():
                    print(f"\n{self.players[current_player].name} wins!")
                    return
            else:
                print("> Miss!")

            current_player, opponent_player = opponent_player, current_player
            print()
```

---

#### Functions
```python
def main():
    menu_choice = Menu.show_menu('Main Menu', ['Local Multiplayer', 'Single Player vs AI', 'Quit'])

    # Local multiplayer
    if menu_choice == 1:
        player1_name = input("> Enter Player 1's name: ")
        player2_name = input("> Enter Player 2's name: ")

        player1 = Player(player1_name)
        player2 = Player(player2_name)

        player1.place_ships(SHIP_SIZES)
        player2.place_ships(SHIP_SIZES)

        game = Game([player1, player2])
        game.play()

    # Single player vs AI
    elif menu_choice == 2:
        player_name = input("Enter your name: ")

        # Create players and ships for ai and non-ai
        player = Player(player_name) 
        player.place_ships(SHIP_SIZES) 

        ai = AIPlayer()
        ai.place_ships(SHIP_SIZES)

        # Create game and play
        game = Game([player, ai])
        game.play()

    # Quit
    print("Goodbye!")
```

```python
# Entry point
if __name__ == '__main__':
    main()
```


## SECTION 3: Testing the solution (21 marks)

### Tests
#### Must include: `test`, `test_data`, `data_type`, `expected_result`, `actual_result`, `pass/fail`

| Test | Test Data     | Data Type | Expected Result | Actual Result | Outcome |
|------|---------------|-----------|-----------------|---------------|:-------:|
| `placeholder` | `placeholder` | `placeholder` | `placeholder` | `placeholder` | `placeholder` |


### Evidence of testing

## SECTION 4: Potential enhancements and refinements (10 marks)


