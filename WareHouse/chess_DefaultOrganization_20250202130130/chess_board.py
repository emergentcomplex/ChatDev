'''
This file contains the ChessBoard class which represents the chessboard GUI.
'''
import tkinter as tk
from chess_pieces import Pawn, Rook, Knight, Bishop, Queen, King
class ChessBoard(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.board = [[None for _ in range(8)] for _ in range(8)]
        self.create_board()
    def create_board(self):
        for row in range(8):
            for col in range(8):
                if (row + col) % 2 == 0:
                    color = "white"
                else:
                    color = "black"
                square = tk.Frame(self, width=80, height=80, bg=color)
                square.grid(row=row, column=col)
                self.board[row][col] = square
        # Place chess pieces on the board
        self.place_pieces()
    def place_pieces(self):
        # Place pawns
        for col in range(8):
            self.board[1][col].piece = Pawn("black")
            self.board[1][col].piece.place(self.board[1][col])
            self.board[6][col].piece = Pawn("white")
            self.board[6][col].piece.place(self.board[6][col])
        # Place rooks
        self.board[0][0].piece = Rook("black")
        self.board[0][0].piece.place(self.board[0][0])
        self.board[0][7].piece = Rook("black")
        self.board[0][7].piece.place(self.board[0][7])
        self.board[7][0].piece = Rook("white")
        self.board[7][0].piece.place(self.board[7][0])
        self.board[7][7].piece = Rook("white")
        self.board[7][7].piece.place(self.board[7][7])
        # Place knights
        self.board[0][1].piece = Knight("black")
        self.board[0][1].piece.place(self.board[0][1])
        self.board[0][6].piece = Knight("black")
        self.board[0][6].piece.place(self.board[0][6])
        self.board[7][1].piece = Knight("white")
        self.board[7][1].piece.place(self.board[7][1])
        self.board[7][6].piece = Knight("white")
        self.board[7][6].piece.place(self.board[7][6])
        # Place bishops
        self.board[0][2].piece = Bishop("black")
        self.board[0][2].piece.place(self.board[0][2])
        self.board[0][5].piece = Bishop("black")
        self.board[0][5].piece.place(self.board[0][5])
        self.board[7][2].piece = Bishop("white")
        self.board[7][2].piece.place(self.board[7][2])
        self.board[7][5].piece = Bishop("white")
        self.board[7][5].piece.place(self.board[7][5])
        # Place queens
        self.board[0][3].piece = Queen("black")
        self.board[0][3].piece.place(self.board[0][3])
        self.board[7][3].piece = Queen("white")
        self.board[7][3].piece.place(self.board[7][3])
        # Place kings
        self.board[0][4].piece = King("black")
        self.board[0][4].piece.place(self.board[0][4])
        self.board[7][4].piece = King("white")
        self.board[7][4].piece.place(self.board[7][4])