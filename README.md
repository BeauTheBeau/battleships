# Battleships Game

This is a Battleships game created in Python using Object-Oriented Programming. It includes local multiplayer,
single-player vs AI, and online multiplayer modes.

## Modes

### Single-player vs AI

In this mode, you play against an AI opponent that makes random attacks on your board. To play, select the "
Single-player" option from the main menu.

### Local Multiplayer

In this mode, two players take turns on the same computer. Each player has their own game board and ships. To play,
select the "Local Multiplayer" option from the main menu.

### Online Multiplayer

In this mode, two players connect over a network and play against each other. The game handles network communication and
synchronization between the players. To play, select the "Online Multiplayer" option from the main menu.

## Classes

### Board

The Board class represents the game board and includes methods for placing ships and making attacks.

- `__init__(self, size=10)`: Initializes a new Board object with the specified size (default is 10).
- `place_ship(self, ship, x, y, horizontal)`: Places the specified ship on the board at the specified coordinates,
  either horizontally or vertically.
- `attack(self, x, y)`: Makes an attack on the specified coordinates and returns the result ('hit', 'miss', or 'already
  attacked').

### Ship

The Ship class represents a ship on the board and includes methods for placing the ship and checking if the ship has
been hit or sunk.

- `__init__(self, size)`: Initializes a new Ship object with the specified size.
- `place(self, x, y, horizontal)`: Places the ship on the board at the specified coordinates, either horizontally or
  vertically.
- `hit(self, x, y)`: Checks if the ship has been hit at the specified coordinates and returns True if it has.
- `sunk(self)`: Checks if the ship has been sunk and returns True if it has.

### Player

The Player class represents a player and includes methods for setting up the player's board and making attacks.

- `__init__(self, name)`: Initializes a new Player object with the specified name.
- `place_ships(self)`: Places the player's ships on the board.
- `attack(self, other_player, x, y)`: Makes an attack on the specified coordinates of the other player's board.

### AI

The AI class represents the AI opponent and includes methods for making random attacks on the player's board.

- `__init__(self, name): Initializes a new AI object with the specified name.
- `attack(self, other_player): Makes a random attack on the other player's board.

### Game

The Game class manages the overall game and includes methods for starting the game and handling turns.

- `__init__(self)`: Initializes a new Game object.
- `start(self)`: Starts the game and displays the main menu.
- `play_singleplayer(self)`: Starts a single-player game.
- `play_local_multiplayer(self)`: Starts a local multiplayer game.
- `play_online_multiplayer(self)`: Starts an online multiplayer game.
- `check_gameover(self)`: Checks if the game is over.
- `next_turn(self)`: Moves on to the next turn.

### Network

The Network class handles network communication for online multiplayer.

- `__init__(self)`: Initializes a new Network object.
- `connect(self, ip, port)`: Connects to the specified IP address and port.
- `send(self, data)`: Sends data over the network.
- `receive(self)`: Receives data from the network.

## Global Variables

### SHIP_SIZES

List of ship sizes.  
Example: `SHIP_SIZES = [5, 4, 3, 3, 2]`

### SHIP_NAMES

List of ship names.  
Example: `SHIP_NAMES = ['Carrier', 'Battleship', 'Cruiser', 'Submarine', 'Destroyer']`

### SYMBOLS

List of symbols used to represent ships, hits, misses and empty spaces on the board.
Example: `SYMBOLS = ['🛥️', '💥', '🌊', '⬜']`

## Functions

### clear_screen()

Clears the screen.

### get_input(prompt, valid_options)

Gets input from the user and returns it.

- `prompt`: The prompt to display to the user.
- `valid_options`: A list of valid options.

#### Example

```python
name = get_input('Pick an option: ', ['1', '2', '3'])
```

## Packages

### colorama

Library for printing colored text in the terminal. Uses:

- Highlighting the hit and miss cells on the board with different colors.
- Adding color to the game messages to make them stand out from the rest of the output.
- Using different colors to distinguish between different types of ships on the board.

### curses

Library for creating a text-based user interface. Uses:

- Creating a game menu with different options (single-player, multiplayer, etc.) that can be navigated with arrow keys or
  other keys.
- Implementing a dynamic game board that can be updated in real-time as the game progresses.
- Creating a game chat feature that allows players to communicate with each other during online multiplayer mode.

### pandas

Library for creating data structures and performing data analysis. Uses:

- Storing the game data in a DataFrame, which allows for easy manipulation and analysis of the data.
- Analyzing player performance over time by keeping track of game statistics such as hit rate and win rate.
- Creating a leaderboard that displays the top players based on their performance in previous games.

### numpy

Library for performing mathematical operations on arrays. Uses:

- Creating a game board as a 2D numpy array, which allows for easy indexing and manipulation of the data.
- Using the numpy random module to generate random ship placements for the game board.
- Calculating the probability of hitting a ship in a particular cell based on the remaining ships on the board and the
  number of empty cells.

### scikit-learn

Library for machine learning. Uses:

- Using supervised learning algorithms such as decision trees or logistic regression to train a model to make optimal
  guesses about the location of the player's ships.
- Using unsupervised learning algorithms such as clustering to group similar game states together and make better
  decisions based on the current game state.
- Implementing reinforcement learning algorithms such as Q-learning or Monte Carlo Tree Search to create an AI opponent
  that can learn and improve over time.


----
# Path: src/battleships.py
