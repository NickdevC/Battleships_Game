# Import libraries
import time
import sys
import random

# The four overlapping 'fields' of play 
PLAYER_FIELD = [[" "] * 8 for i in range(8)]
COMPUTER_FIELD = [[" "] * 8 for i in range(8)]
PLAYER_GUESS = [[" "] * 8 for i in range(8)]
COMPUTER_GUESS = [[" "] * 8 for i in range(8)]

letters_to_integers = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4,
    'F': 5,
    'G': 6,
    'H': 7
}

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
 |  _ \      | | | | | |         | |   (_)                       |    |    |
 | |_) | __ _| |_| |_| | ___  ___| |__  _ _ __  ___             )_)  )_)  )_)
 |  _ < / _` | __| __| |/ _ \/ __| '_ \| | '_ \/ __|           )___))___))___)
 | |_) | (_| | |_| |_| |  __/\__ \ | | | | |_) \__ |         ____|____|____|___
 |____/ \__,_|\__|\__|_|\___||___/_| |_|_| .__/|___/     ----\                /----
                                         | |           ^^^   ^^^^   ^^^  ^^^^   ^^
                                         |_|              ^^^    ^^    ^^^^   ^^
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
                placement, row, column = random.choice(["H", "V"]), \
                    random.randint(0, 7), random.randint(0, 7)
                if placement == "H":
                    for i in range(column, column + ship_length):
                        field[row][i] = "$"
                else:
                    for i in range(row, row + ship_length):
                        field[column][i] = "$"
            else:
                place_ship = True
                print_slow("Place your ship with a length of " + str(ship_length))
                row, column, placement = user_placement(place_ship)
                print("Ship successfully placed\n")
                if placement == "H":
                    for i in range(column, column + ship_length):
                        field[row][i] = "$"
                else:
                    for i in range(row, row + ship_length):
                        field[column][i] = "$"
                display_field(PLAYER_FIELD)
                break

def player_input(place_ship):
    """
    Allows the user to input coordinate data to place their
    ships and also signal where they wish to target their
    opponents ships.
    """
    if place_ship == True:
        while True:
            try:
                placement = input("Is your ship positioned vertically(V) \
                    or horizontally(H)? \n").upper()
                if placement == "H" or "V":
                    break
                else:
                    raise ValueError
            except ValueError:
                print("\u001b[31mPlease enter a valid orientation (V or H)\n")
        while True:
            try:
                row = input("Which row is your ship positioned on (1-8)? \n")
                if row in '12345678':
                    row = int(row) -1
                    break
                else:
                    raise ValueError
            except ValueError:
                print("\u001b[31mPlease enter a valid integer between 1-8 \n")
        while True:
            try:
                column = input("Which column is your ship positioned in \
                    (A-H)? \n").upper()
                if column not in 'ABCDEFGH':
                    print("\u001b[31mPlease enter a valid letter between A-H \n")
                else:
                    column = letters_to_integers[column]
                    break
        return row, column, placement
    else:
        while True:
            try:
                row = input("Which row is your ship positioned on (1-8)? \n")
                if row in '12345678':
                    row = int(row) -1
                    break
                else:
                    raise ValueError
            except ValueError:
                print("\u001b[31mPlease enter a valid integer between 1-8 \n")
        while True:
            try:
                column = input("Which column is your ship positioned in \
                    (A-H)? \n").upper()
                if column not in 'ABCDEFGH':
                    print("\u001b[31mPlease enter a valid letter between A-H \n")
                else: 
                    column = letters_to_integers[column]
                    break
        return column, row

def check_placement(SHIP_LENGTH, row, column, placement):
    """
    Checks that the ship placement fits to the perameters of each field.
    If the check returns 'False' then a error message is raised to user
    in the place_ship function.
    """
    if placement == "H":
        if column + SHIP_LENGTH > 8:
            return False
        else:
            return True
    else:
        if row + SHIP_LENGTH > 8:
            return False
        else:
            return True

welcome_screen()
display_field(PLAYER_FIELD)