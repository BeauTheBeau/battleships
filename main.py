# TUI Battleships Game using OOP
import random
from simple_term_menu import TerminalMenu
 
# GLOBAL VARIABLES



# CLASSES
class Ship:

    def __init__(self, name, length):
        self.name = name
        self.length = length
        self.health = length
        self.sunk = False

    def hit(self):
        self.health -= 1
        if self.health == 0:
            self.sunk = True
            print(f"You sunk my {self.name}!")

    def __str__(self):
        return f"{self.name} ({self.length})"
    


class Board:

    def __init__(self, size):
        self.size = size
        self.board = []
        self.ships = []
        self.hits = []
        self.misses = []


    def add_ship(self, ship):
        self.ships.append(ship)


    def print_board(self):

        # print column numbers
        print(" ", end=" ")
        for i in range(self.size):
            print(i, end=" ")
        print()

        # print row numbers and board
        for row in range(self.size):
            print(row, end=" ")
            for col in range(self.size):
                if (row, col) in self.hits:
                    print("X", end=" ")
                elif (row, col) in self.misses:
                    print("O", end=" ")
                else:
                    print(".", end=" ")
            print()


    def place_ship(self, ship, row, col, direction):
        if direction == "h":
            for i in range(ship.length):
                self.board[row][col + i] = ship
        elif direction == "v":
            for i in range(ship.length):
                self.board[row + i][col] = ship

    def check_hit(self, row, col):
        if self.board[row][col] == None:
            self.misses.append((row, col))
            return False
        else:
            self.hits.append((row, col))
            self.board[row][col].hit()
            return True
        
    def check_sunk(self, ship):
        if ship.sunk:
            print(f"You sunk my {ship.name}!")
            return True
        else:
            return False

# FUNCTIONS

def play():
    
    print("Welcome to Battleships!")
    print()
    print("Single or multiplayer?")
    menu = TerminalMenu(["Single Player", "Multiplayer"])
    menu_entry_index = menu.show()
    
    

def menu():
    menu = TerminalMenu(["Play", "Quit"])
    menu_entry_index = menu.show()

    if menu_entry_index == 0:
        play()
    elif menu_entry_index == 1:
        quit()

    print(menu_entry_index)

menu()