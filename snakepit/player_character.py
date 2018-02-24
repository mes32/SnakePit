import pygame

from position import Position

class PlayerCharacter():
    """
    The player's character in the game.
    """

    def __init__(self):
        self.current_hp = 5
        self.total_hp = 5
        self.position = Position()
        # self.delta_position = Position()

    def set_position(self, x, y):
        self.position.set(x, y)

    # def indicate_walk(self, delta_x, delta_y):
    #     self.delta_position = Position(delta_x, delta_y)

    # def finalize_walk(self):
    #     self.position = self.position.delta_position(self.delta_position)
        

