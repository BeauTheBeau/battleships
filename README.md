# Battleships Game

This is a Battleships game created in Python using Object-Oriented Programming. It includes local multiplayer,
single-player vs AI, and online multiplayer modes.

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

---

## SECTION 3: Testing the solution (21 marks)

### Tests
#### Must include: `test`, `test_data`, `data_type`, `expected_result`, `actual_result`, `pass/fail`

| Test | Test Data     | Data Type | Expected Result | Actual Result | Outcome |
|------|---------------|-----------|-----------------|---------------|:-------:|
| `placeholder` | `placeholder` | `placeholder` | `placeholder` | `placeholder` | `placeholder` |


### Evidence of testing

## SECTION 4: Potential enhancements and refinements (10 marks)


