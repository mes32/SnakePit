import pygame

class Dimensions():
    """
    Two dimensions: width and height
    """

    def __init__(self, width, height):
        self.width = int(width)
        self.height = int(height)

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height