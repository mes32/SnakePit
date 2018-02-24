import pygame

class Position():
    """
    A position on the playing field
    """

    def __init__(self, x=0, y=0):
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

    def delta_position(self, delta):
        if delta == None:
            x = self.x
            y = self.y
            return Position(x, y)
        else:
            x = self.x + delta.get_x()
            y = self.y + delta.get_y()
            return Position(x, y)
        
