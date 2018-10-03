import pygame

class Tile:
    def __init__(self, letter, number, piece):
        self.letter = letter
        self.number = number
        self.piece  = piece
        self.posx1 = None
        self.posx2 = None
        self.posy1 = None
        self.posy2 = None
        global busy



