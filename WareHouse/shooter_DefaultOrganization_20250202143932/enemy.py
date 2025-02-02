'''
Defines the Enemy class representing enemy characters.
'''
import random
from settings import *
class Enemy:
    def __init__(self, game):
        self.game = game
        self.x = random.randint(1, self.game.width - 2)
        self.y = 1
    def update(self):
        self.y += ENEMY_SPEED
    def draw(self):
        if 1 <= self.y < self.game.height - 1:
            try:
                self.game.stdscr.addch(self.y, self.x, ENEMY_CHAR)
            except curses.error:
                pass