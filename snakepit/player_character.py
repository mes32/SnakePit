import pygame

class PlayerCharacter():
    """
    The player's character in the game.
    """

    def __init__(self):
        self.current_hp = 5
        self.total_hp = 5
        self.position = (-1, -1)

        self.delta_x = 0
        self.delta_y = 0

    def set_position(self, x, y):
        self.position = (x, y)

    def indicate_walk(self, delta_x, delta_y):
        self.delta_x = delta_x
        self.delta_y = delta_y

    def finalize_walk(self):
        x = self.position[0]
        y = self.position[1]
        x = x + self.delta_x
        y = y + self.delta_y

        self.position = x, y
        self.delta_x = 0
        self.delta_y = 0
        

