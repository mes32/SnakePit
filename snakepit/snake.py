import pygame

class Snake():
    """
    The basic snake enemies.
    """

    def __init__(self, x, y):
        self.current_hp = 1
        self.total_hp = 1
        self.position = (x, y)