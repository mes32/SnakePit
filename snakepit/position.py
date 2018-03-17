import pygame

import position_lookup

class Position():
    """
    A position on the playing field
    """

    def __init__(self, map, x, y):
        self.map = map
        self.x = int(x)
        self.y = int(y)

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_tuple(self):
        return (self.x, self.y)

    def set(self, x, y):
        self.x = x
        self.y = y

    def delta(self, x=0, y=0):
        new_x = self.x + x
        new_y = self.y + y
        return Position(self.map, new_x, new_y)
        
