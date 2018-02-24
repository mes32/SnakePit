import pygame

from position import Position

class Snake():
    """
    The basic snake enemies.
    """

    def __init__(self, position):
        self.current_hp = 1
        self.total_hp = 1
        self.position = position