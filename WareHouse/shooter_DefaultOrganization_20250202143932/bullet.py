'''
Defines the Bullet class representing bullets fired by the player.
'''
from settings import *
class Bullet:
    def __init__(self, game, x, y):
        self.game = game
        self.x = x
        self.y = y
    def update(self):
        self.y -= BULLET_SPEED
    def draw(self):
        if 1 <= self.y < self.game.height - 1:
            try:
                self.game.stdscr.addch(self.y, self.x, BULLET_CHAR)
            except curses.error:
                pass