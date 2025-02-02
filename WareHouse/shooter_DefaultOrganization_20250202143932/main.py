'''
The main module to start the game.
'''
import sys
import platform
try:
    import curses
except ImportError as e:
    if platform.system() == 'Windows':
        print("Error importing curses module. On Windows, please install the 'windows-curses' package:")
        print("pip install windows-curses")
    else:
        print("Error importing curses module:", e)
    sys.exit(1)
from game import Game
def main(stdscr):
    game = Game(stdscr)
    game.run()
if __name__ == '__main__':
    try:
        curses.wrapper(main)
    except curses.error as e:
        print("Error initializing curses.")
        print("Ensure you are running the game in a proper terminal that supports curses.")
        if platform.system() == 'Windows':
            print("On Windows, please install the 'windows-curses' package:")
            print("pip install windows-curses")
        print("Error details:", e)
        sys.exit(1)