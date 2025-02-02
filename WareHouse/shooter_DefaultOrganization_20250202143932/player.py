'''
Defines the Player class representing the player's character.
'''
from settings import *
from bullet import Bullet
class Player:
    def __init__(self, game, x, y):
        self.game = game
        self.x = x
        self.y = y
    def move(self, dx):
        new_x = self.x + dx
        if 1 <= new_x < self.game.width - 1:
            self.x = new_x
    def shoot(self):
        return Bullet(self.game, self.x, self.y - 1)
    def draw(self):
        try:
            self.game.stdscr.addch(self.y, self.x, PLAYER_CHAR)
        except curses.error:
            pass