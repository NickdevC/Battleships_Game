# Import libraries
import time
import sys

def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.01)


def welcome_screen():
    """
    Displays the main screen for users on loading the game for the first time,
    or when selecting to start a new game.
    """
    print("\033[34m Got ships? Let's battle!")
    time.sleep(3)
    print_slow("""\
    \u001b[34m
  ____        _   _   _           _     _           
 |  _ \      | | | | | |         | |   (_)          
 | |_) | __ _| |_| |_| | ___  ___| |__  _ _ __  ___ 
 |  _ < / _` | __| __| |/ _ \/ __| '_ \| | '_ \/ __|
 | |_) | (_| | |_| |_| |  __/\__ \ | | | | |_) \__ |
 |____/ \__,_|\__|\__|_|\___||___/_| |_|_| .__/|___/
                                         | |        
                                         |_| 
\u001b[0m       
""")


welcome_screen()