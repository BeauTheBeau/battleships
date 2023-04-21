# Battleships Game
## Descriptiom 

The program will be written in Python and will use a TUI and Object Oriented Programming. A GUI was not feasable due to being unable to preview it in a cloud based environment.

There are two players. Each has seven ships.
- 1x Aircraft carrier   (5 squares)
- 1x Battleship         (4 squares)
- 1x Cruiser            (3 squares)
- 2x Destroyer          (2 squares)
- 2x Submarine          (1 squares)

Ships can be placed in a 10x10 grid, horizontally or vertically. Ships can't overlap nor can they be placed diagonally.

The game is played in turns. Each turn, a player announces a square in the opponent's grid to attack, the program will state whether or not the attack hit or missed. The program notes the hit/miss on both players' grids. The game ends when one player has no more ships left.


## Todo

- [ ] Classes   
    - [ ] Ship
    - [ ] Player
    - [ ] Board
    - [ ] Game

- [ ] Functions
    - [ ] Place ships
    - [ ] Attack
    - [ ] Check if ship is sunk
    - [ ] Check if game is over

- [ ] GUI
    - [ ] Pygame
    - [ ] Grid
    - [ ] Ships
    - [ ] Buttons
    - [ ] Text
    - [ ] Images