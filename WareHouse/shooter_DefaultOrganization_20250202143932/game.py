'''
This module contains the Game class which manages the game loop and overall game state.
'''
import curses
import time
import random
from settings import *
from player import Player
from enemy import Enemy
from bullet import Bullet
class Game:
    def __init__(self, stdscr):
        self.stdscr = stdscr
        curses.curs_set(0)  # Hide the cursor
        self.stdscr.nodelay(True)  # Non-blocking input
        self.stdscr.timeout(int(1000 / FPS))
        self.height, self.width = self.stdscr.getmaxyx()
        self.running = True
        self.player = Player(self, self.width // 2, self.height - 2)
        self.bullets = []
        self.enemies = []
        self.spawn_timer = 0
        self.score = 0
    def run(self):
        while self.running:
            self.handle_input()
            self.update()
            self.draw()
        self.game_over()
    def handle_input(self):
        key = self.stdscr.getch()
        if key != -1:
            if key == curses.KEY_LEFT or key == ord('a'):
                self.player.move(-PLAYER_SPEED)
            elif key == curses.KEY_RIGHT or key == ord('d'):
                self.player.move(PLAYER_SPEED)
            elif key == ord(' ') or key == ord('w'):
                bullet = self.player.shoot()
                if bullet:
                    self.bullets.append(bullet)
            elif key == ord('q'):
                self.running = False
    def update(self):
        # Update bullets
        for bullet in self.bullets[:]:
            bullet.update()
            if bullet.y < 1:
                self.bullets.remove(bullet)
        # Update enemies
        for enemy in self.enemies[:]:
            enemy.update()
            if enemy.y >= self.height - 1:
                self.enemies.remove(enemy)
                self.score -= 1  # Penalty for missed enemies
            elif enemy.x == self.player.x and enemy.y == self.player.y:
                self.running = False  # Player hit by enemy
        # Check for bullet-enemy collisions
        for bullet in self.bullets[:]:
            for enemy in self.enemies[:]:
                if bullet.x == enemy.x and bullet.y == enemy.y:
                    self.bullets.remove(bullet)
                    self.enemies.remove(enemy)
                    self.score += 1
                    break
        # Spawn enemies periodically
        self.spawn_timer += 1
        if self.spawn_timer >= ENEMY_SPAWN_RATE:
            self.spawn_timer = 0
            enemy = Enemy(self)
            self.enemies.append(enemy)
    def draw(self):
        self.stdscr.clear()
        # Draw player
        self.player.draw()
        # Draw bullets
        for bullet in self.bullets:
            bullet.draw()
        # Draw enemies
            for enemy in self.enemies:
                enemy.draw()
        # Draw score
        score_text = f"Score: {self.score}"
        try:
            self.stdscr.addstr(0, 2, score_text)
        except curses.error:
            pass
        self.stdscr.refresh()
    def game_over(self):
        self.stdscr.nodelay(False)
        self.stdscr.clear()
        game_over_text = "GAME OVER"
        score_text = f"Your Score: {self.score}"
        exit_text = "Press any key to exit"
        self.stdscr.addstr(self.height // 2 - 1, (self.width - len(game_over_text)) // 2, game_over_text, curses.A_BOLD)
        self.stdscr.addstr(self.height // 2, (self.width - len(score_text)) // 2, score_text)
        self.stdscr.addstr(self.height // 2 + 2, (self.width - len(exit_text)) // 2, exit_text)
        self.stdscr.refresh()
        self.stdscr.getch()