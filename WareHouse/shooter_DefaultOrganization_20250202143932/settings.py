'''
Contains game settings and constants.
'''
import curses
# Frames per second
FPS = 30
# Player settings
PLAYER_CHAR = '^'
PLAYER_SPEED = 1  # Movement speed per keypress
# Bullet settings
BULLET_CHAR = '|'
BULLET_SPEED = 1  # Cells per update
# Enemy settings
ENEMY_CHAR = 'V'
ENEMY_SPEED = 1  # Cells per update
ENEMY_SPAWN_RATE = 10  # Frames between enemy spawns