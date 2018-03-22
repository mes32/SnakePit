import pygame

import position_map

class Position():
    """
    A position on the playing field
    """

    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_tuple(self):
        return (self.x, self.y)

    def delta(self, dx=0, dy=0):
        new_x = self.x + dx
        new_y = self.y + dy
        return Position(new_x, new_y)

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"
        
