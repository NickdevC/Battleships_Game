# Import libraries
import time
import sys
import random

# The four overlapping 'fields' of play
PLAYER_FIELD = [[" "] * 10 for i in range(10)]
AI_FIELD = [[" "] * 10 for i in range(10)]
PLAYER_GUESS = [[" "] * 10 for i in range(10)]
AI_GUESS = [[" "] * 10 for i in range(10)]

letters_to_integers = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4,
    'F': 5,
    'G': 6,
    'H': 7,
    'I': 8,
    'J': 9,
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
             |    |    |
            )_)  )_)  )_)             
           )___))___))___)
         ____|____|____|___
     ----\                /----
    ^^^   ^^^^   ^^^  ^^^^   ^^  ^^
        ^^^    ^^    ^^^^   ^^
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
    print_slow("\nYour battlefield consists of an 10x10 grid.\n")
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
opponent's ships wins!\n")
    time.sleep(2)


def display_field(field):
    """
    Displays the battlefield 8x8 grid to the player, ensuring
    placeholders are present to allow manipulation throughout
    the game.
    """
    print("  A B C D E F G H I J")
    print("  ------------------")
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
            if field == AI_FIELD:
                placement, row, column = random.choice(["H", "V"]), \
                    random.randint(0, 9), random.randint(0, 9)
                if check_placement(ship_length, row, column, placement):
                    if not check_overlap(ship_length, row, column, placement,
                                         display_field):
                        if placement == "H":
                            for i in range(column, column + ship_length):
                                field[row][i] = "$"
                        else:
                            for i in range(row, row + ship_length):
                                field[column][i] = "$"
                        break
            else:
                place_ship = True
                print_slow("Place your ship with a length of " + 
                           str(ship_length))
                row, column, placement = player_input(place_ship)
                if check_placement(ship_length, row, column, placement):
                    if check_overlap(ship_length, row, column, placement,
                                     display_field):
                        print("Cannot place ship. Pick again!\n")
                    else:
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
    opponents' ships.
    """
    if place_ship:
        while True:
            try:
                placement = input("Vertical(V) or horizontal(H) placement?\n")
                if placement == "H" or "V":
                    break
                else:
                    raise ValueError
            except ValueError:
                print("Please enter a valid orientation (V or H)\n")
        while True:
            try:
                row = input("Which row (1-10)?\n")
                if row in "1,2,3,4,5,6,7,8,9,10":
                    row = int(row)-1
                    break
                else:
                    raise ValueError
            except ValueError:
                print("Please enter a valid integer between 1-10\n")
        while True:
            try:
                column = input("Which column (A-J)?\n")
                if column not in "A,B,C,D,E,F,G,H,I,J":
                    print("Please enter a valid letter (A-J)\n")
                else:
                    column = letters_to_integers[column]
                    break
            except KeyError:
                print("Please enter a valid letter (A-J)\n")
        return row, column, placement
    else:
        while True:
            try:
                row = input("Which row (1-10)?\n")
                if row in "1,2,3,4,5,6,7,8,9,10":
                    row = int(row) - 1
                    break
                else:
                    raise ValueError
            except ValueError:
                print("Please enter a valid integer between 1-10\n")
        while True:
            try:
                column = input("Which column (A-J)?\n")
                if column not in "A,B,C,D,E,F,G,H,I,J":
                    print("Please enter a valid letter (A-J)\n")
                else:
                    column = letters_to_integers[column]
                    break
            except KeyError:
                print("Please enter a valid letter (A-J)\n")
        return row, column


def check_overlap(SHIP_LENGTH, row, column, placement, display_field):
    """
    When users place a ship, checks to see if there is overlap with existing
    placements.
    """
    if placement == "H":
        for i in range(column, column + SHIP_LENGTH):
            if display_field[row][i] == "$":
                return True
    else:
        for i in range(row, row + SHIP_LENGTH):
            if display_field[column][i] == "$":
                return True
    return False


def check_placement(SHIP_LENGTH, row, column, placement):
    """
    Checks that the ship placement fits to the perameters of each field.
    If the check returns 'False' then a error message is raised to user
    in the place_ship function.
    """
    if placement == "H":
        if column + SHIP_LENGTH > 10:
            return False
        else:
            return True
    else:
        if row + SHIP_LENGTH > 10:
            return False
        else:
            return True


def player_computer_cycle(display_field):
    """
    Cycles through the player and computer turns. Ensures that the
    computer turn is a random selection using randint method.
    Indicates when a ship has been successfully hit and provides
    feedback to user.
    """
    if display_field == PLAYER_GUESS:
        column, row = player_input(PLAYER_GUESS)
        if display_field[column][row] == "-":
            player_computer_cycle(display_field)
        elif display_field[column][row] == "X":
            player_computer_cycle(display_field)
        elif AI_FIELD[column][row] == "$":
            display_field[column][row] == "X"
            print_fast("Hit!")
        else:
            display_field[column][row] = "-"
            print_fast("Missed!")
    else:
        column, row = random.randint(0, 9), random.randint(0, 9)
        if display_field[column][row] == "-":
            player_computer_cycle(display_field)
        elif display_field[column][row] == "X":
            player_computer_cycle(display_field)
        elif PLAYER_FIELD[column][row] == "$":
            display_field[column][row] == "X"
            print_fast("We have been hit!")
        else:
            display_field[column][row] = "-"
            print_fast("They missed!")


def start_game():
    """
    Executes the game functions.
    """
    start_button = input("Press B to begin...\n").upper()
    while start_button != 'B':
        start_button = input("Press B to begin...\n").upper()
    place_ship(AI_FIELD)
    display_field(PLAYER_FIELD)
    place_ship(PLAYER_FIELD)

    while True:
        while True:
            print_fast("Your turn! Start firing!\n")
            display_field(PLAYER_GUESS)
            player_computer_cycle(PLAYER_GUESS)
            break
        while True:
            player_computer_cycle(AI_GUESS)
            break
        display_field(AI_GUESS)


welcome_screen()
start_game()
