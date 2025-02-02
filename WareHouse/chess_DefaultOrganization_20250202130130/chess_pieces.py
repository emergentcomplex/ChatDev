'''
This file contains the classes for different chess pieces.
'''
import tkinter as tk
class Piece:
    def __init__(self, color):
        self.color = color
        self.image = None
    def place(self, square):
        self.square = square
        self.image = tk.Label(square, image=self.get_image())
        self.image.pack()
    def get_image(self):
        # Return the image based on the piece type and color
        pass
class Pawn(Piece):
    def __init__(self, color):
        super().__init__(color)
    def get_image(self):
        # Return the pawn image based on the color
        if self.color == "black":
            return tk.PhotoImage(file="black_pawn.png")
        else:
            return tk.PhotoImage(file="white_pawn.png")
class Rook(Piece):
    def __init__(self, color):
        super().__init__(color)
    def get_image(self):
        # Return the rook image based on the color
        if self.color == "black":
            return tk.PhotoImage(file="black_rook.png")
        else:
            return tk.PhotoImage(file="white_rook.png")
class Knight(Piece):
    def __init__(self, color):
        super().__init__(color)
    def get_image(self):
        # Return the knight image based on the color
        if self.color == "black":
            return tk.PhotoImage(file="black_knight.png")
        else:
            return tk.PhotoImage(file="white_knight.png")
class Bishop(Piece):
    def __init__(self, color):
        super().__init__(color)
    def get_image(self):
        # Return the bishop image based on the color
        if self.color == "black":
            return tk.PhotoImage(file="black_bishop.png")
        else:
            return tk.PhotoImage(file="white_bishop.png")
class Queen(Piece):
    def __init__(self, color):
        super().__init__(color)
    def get_image(self):
        # Return the queen image based on the color
        if self.color == "black":
            return tk.PhotoImage(file="black_queen.png")
        else:
            return tk.PhotoImage(file="white_queen.png")
class King(Piece):
    def __init__(self, color):
        super().__init__(color)
    def get_image(self):
        # Return the king image based on the color
        if self.color == "black":
            return tk.PhotoImage(file="black_king.png")
        else:
            return tk.PhotoImage(file="white_king.png")