# This is a Battleships game created in Python using Object-Oriented Programming. It includes local multiplayer,
# single-player vs AI, and online multiplayer modes.

import colorama
import numpy as np
from colorama import Fore, Style

# GLOBAL VARIABLES
SHIP_SIZES = [5, 4, 3, 3, 2]
SHIP_NAMES = ['Carrier', 'Battleship', 'Cruiser', 'Submarine', 'Destroyer']
SYMBOLS = ['S', 'X', '-', 'O', ' ']
DEV_MODE = True

# COLORS
colorama.init()
COLORS = [Fore.RED, Fore.GREEN, Fore.BLUE, Fore.YELLOW, Fore.MAGENTA, Fore.CYAN, Fore.WHITE]

if DEV_MODE:
    print('DEV MODE ON!')
    print(' > Ships will be placed automatically.')


# GLOBAL FUNCTIONS

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

class Player:
    def __init__(self, name):
        self.name = name
        self.board = Board(10, 10)

    def place_ships(self, ship_sizes):

        print(f'{self.name.upper()}, place your ships on the board.')
        print()

        for i, size in enumerate(ship_sizes):

            if DEV_MODE:

                if i == 0:
                    self.board.place_ship(Ship(SHIP_NAMES[i], size), 0, 0, 'h')
                elif i == 1:
                    self.board.place_ship(Ship(SHIP_NAMES[i], size), 1, 0, 'h')
                elif i == 2:
                    self.board.place_ship(Ship(SHIP_NAMES[i], size), 2, 0, 'h')
                elif i == 3:
                    self.board.place_ship(Ship(SHIP_NAMES[i], size), 3, 0, 'h')
                elif i == 4:
                    self.board.place_ship(Ship(SHIP_NAMES[i], size), 4, 0, 'h')
                else:
                    pass

                continue

            while True:
                print(f'Place your {SHIP_NAMES[i]} ({size} spaces):')
                row, col, direction = input('> Enter row, column, and direction (h or v): ').split()
                row, col = int(row), int(col)
                if direction.lower() == 'h':
                    if col + size > 10:
                        print('> Ship goes off the board, try again.')
                        continue
                else:
                    if row + size > 10:
                        print('> Ship goes off the board, try again.')
                        continue
                ship = Ship(SHIP_NAMES[i], size)
                if self.board.place_ship(ship, row, col, direction):
                    print(
                        f'> Your {SHIP_NAMES[i]} has been placed at ({row}, {col}) going {direction.replace("h", "horizontally").replace("v", "vertically")}.')
                    print()
                    break
                else:
                    print('> There is already a ship in the way, try again.')
                    print()

    def print_board(self):
        colours = [Fore.RED, Fore.GREEN, Fore.BLUE, Fore.YELLOW, Fore.MAGENTA, Fore.CYAN, Fore.WHITE]

        for i, row in enumerate(self.board.grid):
            print(i, end=' ')
            for col in row:

                # colour each ship differently
                if col == 0 or col == -1:
                    print('-', end=' ')
                elif col == -2:
                    print('X', end=' ')
                else:
                    print(colours[col - 1] + 'S' + Style.RESET_ALL, end=' ')

            print()

        print(colours[0] + '  0 1 2 3 4 5 6 7 8 9' + Style.RESET_ALL)
        print()

    def print_board_opponent(self):
        colours = [Fore.RED, Fore.GREEN, Fore.BLUE, Fore.YELLOW, Fore.MAGENTA, Fore.CYAN, Fore.WHITE]

        # colour the axis
        for i, row in enumerate(self.board.grid):
            print(i, end=' ')
            for col in row:

                # colour each ship differently
                if col == 0 or col == -1:
                    print('-', end=' ')
                elif col == -2:
                    print('X', end=' ')
                else:
                    print(colours[0] + 'S' + Style.RESET_ALL, end=' ')

            print(i, end=' ')
            print()

        print(colours[0] + '  0 1 2 3 4 5 6 7 8 9' + Style.RESET_ALL)
        print()


class Game:
    def __init__(self, players):
        self.players = players

    def play(self):
        pass


# Test player class
players = [Player('Player 1'), Player('Player 2')]

for player in players:
    player.place_ships(SHIP_SIZES)
    player.print_board()
