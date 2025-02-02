'''
This is the main file for the chess game.
'''
import tkinter as tk
from chess_board import ChessBoard
class ChessGame:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Chess Game")
        self.chess_board = ChessBoard(self.root)
        self.chess_board.pack()
        self.root.mainloop()
if __name__ == "__main__":
    game = ChessGame()