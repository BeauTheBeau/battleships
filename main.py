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

# ========================
# Classes
# ========================

# Menu class
class Menu:
    @staticmethod
    def show_menu(title, array):
        print(title)
        for i, item in enumerate(array):
            print(f'{i + 1}. {item}')
        try:
            choice = int(input('> '))
            if choice < 1 or choice > len(array):
                raise ValueError
            return choice
        except ValueError:
            print('> Invalid input, try again.')
            return Menu.show_menu(title, array)

# Ship class
class Ship:
    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.hits = 0

    def __str__(self):
        return f'{self.name} ({self.size} spaces)'

    def is_sunk(self):
        return self.hits == self.size

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

# Player class
class Player:


    def __init__(self, name):
        self.name = name
        self.board = Board(10, 10)

    def place_ships(self, ship_sizes):
        print(f'{self.name.upper()}, place your ships on the board.\n')

        for i, size in enumerate(ship_sizes):
            if DEV_MODE:
                self.board.place_ship(Ship(SHIP_NAMES[i], size), i, 0, 'h')
                continue

            while True:
                try: 
                    print(f'Place your {SHIP_NAMES[i]} ({size} spaces):')
                    # row, col, direction = input('> Enter row, column, and direction (h or v): ').split()
                    # row, col = int(row), int(col)

                    # Take row and col
                    print(f'> Place your {SHIP_NAMES[i]} ({size} spaces):')
                    print(f'> EXAMPLE: 0 5')
                    row, col = map(int, input('> Enter row and column: ').split())

                    # Show menu for direction
                    direction = Menu.show_menu('Choose direction', ['Horizontally', 'Vertically'])
                    direction = 'h' if direction == 1 else 'v'

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
                except ValueError:
                    print('> Invalid input, try again.')
                    print()

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
    
# AI class
class AIPlayer(Player):
    def __init__(self):
        super().__init__('AI')

    def place_ships(self, ship_sizes):
        for i, size in enumerate(ship_sizes):
            while True:
                row = random.randint(0, 9)
                col = random.randint(0, 9)
                direction = random.choice(['h', 'v'])
                ship = Ship(SHIP_NAMES[i], size)
                if self.board.place_ship(ship, row, col, direction):
                    break

    def fire_shot(self):
        while True:
            row = random.randint(0, 9)
            col = random.randint(0, 9)
            if self.board.grid[row][col] == 0 or self.board.grid[row][col] == -1:
                break
        return row, col


# Game class
class Game:
    def __init__(self, players):
        self.players = players

    def play(self):
        current_player = 0
        opponent_player = 1

        while True:
            print(f"{self.players[current_player].name}'s turn:")
            print("Your Board:")
            self.players[current_player].print_board()
            print("Opponent's Board:")
            self.players[opponent_player].print_board_opponent()

            while True:
                try:
                    row, col = map(int, input("Enter row and column to fire a shot: ").split())
                    if row < 0 or row > 9 or col < 0 or col > 9:
                        raise ValueError
                    break
                except ValueError:
                    print("> Invalid input, try again.")
                    print()

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


# ========================
# Main
# ========================

def main():
    menu_choice = Menu.show_menu('Main Menu', ['Local Multiplayer', 'Single Player vs AI', 'Quit'])

    if menu_choice == 1:
        player1_name = input("> Enter Player 1's name: ")
        player2_name = input("> Enter Player 2's name: ")

        player1 = Player(player1_name)
        player2 = Player(player2_name)

        player1.place_ships(SHIP_SIZES)
        player2.place_ships(SHIP_SIZES)

        game = Game([player1, player2])
        game.play()
    elif menu_choice == 2:
        player_name = input("Enter your name: ")

        player = Player(player_name)
        player.place_ships(SHIP_SIZES)

        ai = AIPlayer()
        ai.place_ships(SHIP_SIZES)

        game = Game([player, ai])
        game.play()

    print("Goodbye!")

# Entry point
if __name__ == '__main__':
    main()
