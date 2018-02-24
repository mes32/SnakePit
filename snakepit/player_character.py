import pygame

from mappable_entity import MappableEntity
from position import Position

class PlayerCharacter(MappableEntity):
    """
    The player's character in the game.
    """

    def __init__(self, position_lookup, position):
        super(PlayerCharacter, self).__init__(position_lookup, position)
        self.current_hp = 0
        self.total_hp = 0
        # self.delta_position = Position()

    def copy_stats(self, stats):
        self.current_hp = int(stats.current_hp)
        self.total_hp = int(stats.total_hp)

    def set_position(self, position):
        self.position = position

    # def indicate_walk(self, delta_x, delta_y):
    #     self.delta_position = Position(delta_x, delta_y)

    # def finalize_walk(self):
    #     self.position = self.position.delta_position(self.delta_position)
        

