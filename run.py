# Import libraries
import time
import sys
import random

# Battlefield area variables
PLAYER_FIELD = [[" "] * 8 for i in range(8)]
COMPUTER_FIELD = [[" "] * 8 for i in range(8)]
PLAYER_GUESS = [[" "] * 8 for i in range(8)]
COMPUTER_GUESS = [[" "] * 8 for i in range(8)]

def print_fast(str):
    """
    Creates a fast moving typing effect for the user.
    """
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.01)

def print_slow(str):
    """
    Creates a slow moving typing effect for the user.
    """
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.05)

# Contains the length of each ship on the battlefield area
SHIP_LENGTHS = [2, 3, 3, 4, 5]

# Welcome screen message
def welcome_screen():
    """
    Displays the main screen for users on loading the game for the first time,
    or when selecting to start a new game.
    """
    print_slow("\033[34m Got ships? Let's battle!\n")
    time.sleep(3)
    print_fast("""\
    \u001b[34m
  ____        _   _   _           _     _           
 |  _ \      | | | | | |         | |   (_)          
 | |_) | __ _| |_| |_| | ___  ___| |__  _ _ __  ___ 
 |  _ < / _` | __| __| |/ _ \/ __| '_ \| | '_ \/ __|
 | |_) | (_| | |_| |_| |  __/\__ \ | | | | |_) \__ |
 |____/ \__,_|\__|\__|_|\___||___/_| |_|_| .__/|___/
                                         | |        
                                         |_| 
\u001b[0m""")

# Player instructions and rules
    print_slow("\n\u001b[34mBefore we begin...let's set out some rules:\n")
    time.sleep(1)
    print_slow("\nYour battlefield consists of an 8x8 grid.\n")
    print_slow("\nYou will have access to the following vessels:\n")
    time.sleep(1)
    print("\n\u001b[31mDESTROYER - 2 spaces on the grid\n")
    print("\u001b[32mSUBMARINE - 3 spaces on the grid\n")
    print("\u001b[33mCRUISER - 3 spaces on the grid\n")
    print("\u001b[34mBATTLESHIP - 4 spaces on the grid\n")
    print("\u001b[35mCARRIER - 5 spaces on the grid\n")
    time.sleep(1)
    print_slow("\n\u001b[34mTake your time to place your ships on the \
battlefield - think tactically!\n")
    print_slow("\nIt is then up to you to route out the enemy's ships \
and destroy them!\n")
    print_slow("\nThe first player to successfuly sink all of their \
opponent's ships\n") 
    print_slow("(17 successful hits in total) wins!\n")
    time.sleep(2)

def display_field(field):
    """
    Displays the battlefield 8x8 grid to the player, ensuring
    placeholders are present to allow manipulation throughout
    the game.
    """
    print("  A B C D E F G H")
    print("  ---------------")
    row_number = 1
    for row in field:
        print("%d|%s|" % (row_number, "|".join(row)))
        row_number += 1

def place_ship(field):
    """
    Allows the computer and player to place their ships on the 
    battlefield area. The function loops through the various ship
    lengths and checks to see if there is overlap during user input.
    """
    for ship_length in SHIP_LENGTHS:
        while True:
            if field == COMPUTER_FIELD:
                orientation, row, column = random.choice(["H", "V"]), \
                    random.randint(0, 7), random.randint(0, 7)
                if orientation == "H":
                    for i in range(column, column + ship_length):
                        field[row][i] = "$"
                else:
                    for i in range(row, row + ship_length):
                        field[column][i] = "$"
        

welcome_screen()
display_field(PLAYER_FIELD)