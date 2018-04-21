import pygame

import position_map

class MapPosition():
    """
    A position on the playing field
    """

    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)
        self.tuple = (self.x, self.y)

    def delta(self, dx=0, dy=0):
        new_x = self.x + int(dx)
        new_y = self.y + int(dy)
        return MapPosition(new_x, new_y)

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"
        
