import pygame

class Position():
    """
    A position on the playing field
    """

    def __init__(self, x=None, y=None):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_tuple(self):
        return (x, y)

    def set(self, x, y):
        self.x = x
        self.y = y

    def delta_position(self, delta):
        self.x = self.x + delta.get_x()
        self.y = self.y + delta.get_y()
        
