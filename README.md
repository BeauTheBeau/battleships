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

```python
class Ship:
    
    # __init__ method: Called when a new instance of the class is created. It takes three parameters:
    #   - name: The name of the ship
    #   - size: The size of the ship
    #   - hits: The number of hits the ship has taken
    # It sets the name, size and hits attributes of the ship to the values passed in as parameters.
    # also setting the sunk attribute of the ship to False. 
    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.hits = 0

    # __str__ method: Called when the print() function is called on an instance of the class. It returns a string
    # containing the name and size of the ship.
        
    def __str__(self):
        return f'{self.name} ({self.size} spaces)'

    # is_sunk method: Called to check if the ship has been sunk. It returns True if the number of hits the ship has
    # taken is equal to the size of the ship, otherwise False returned
    def is_sunk(self):
        return self.hits == self.size
```
```python

class Board:
  
    # __init__ method: Called when a new instance of the class is created. It takes two parameters:
    #   - rows: The number of rows on the board
    #   - cols: The number of columns on the board
    # It sets the rows and cols attributes of the board to the values passed in as parameters, and creates a grid
    # of zeros with the size of the board.
  
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.grid = np.zeros((rows, cols), dtype=int)
        self.ships = []

    # __str__ method: Called when the print() function is called on an instance of the class. It returns a string
    # containing the grid of the board.
        
    def __str__(self):
        return str(self.grid)
        
    # place_ship method: Called to place a ship on the board. It takes four parameters:
    #   - ship: The ship to be placed
    #   - row: The row to place the ship on
    #   - col: The column to place the ship on
    #   - direction: The direction to place the ship in
    # It checks if the ship can be placed on the board, and if it can, it places the ship on the board and returns
    # True. If it can't, it returns False.
    
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

        
    # fire_shot method: Called to fire a shot at a position on the board. It takes two parameters:
    #   - row: The row to fire the shot at
    #   - col: The column to fire the shot at
    # Checks if the shot is a hit or a miss, and returns True if it is a hit, otherwise False.
    
    def fire_shot(self, row, col):
        if self.grid[row][col] == 0:
            self.grid[row][col] = -1
            return False
        else:
            ship = self.ships[self.grid[row][col] - 1]
            ship.hits += 1
            self.grid[row][col] = -2
            return True
        
    # is_game_over method: Called to check if the game is over. It returns True if all the ships on the board have
    # been sunk, otherwise returns False.

    def is_game_over(self):
        for ship in self.ships:
            if not ship.is_sunk():
                return False
        return True
```




---

## SECTION 3: Testing the solution (21 marks)

### Tests
#### Must include: `test`, `test_data`, `data_type`, `expected_result`, `actual_result`, `pass/fail`

| Test | Test Data     | Data Type | Expected Result | Actual Result | Outcome |
|------|---------------|-----------|-----------------|---------------|:-------:|
| `placeholder` | `placeholder` | `placeholder` | `placeholder` | `placeholder` | `placeholder` |


### Evidence of testing

## SECTION 4: Potential enhancements and refinements (10 marks)


