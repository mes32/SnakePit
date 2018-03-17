import pygame

import position_map

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

    def move(self, new_position):
        self.map.move(self, new_position)

    def delta(self, dx=0, dy=0):
        new_x = self.x + dx
        new_y = self.y + dy
        return Position(self.map, new_x, new_y)
        
