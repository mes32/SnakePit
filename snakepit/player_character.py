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
        self.delta_position = Position()

    def copy_stats(self, stats):
        self.current_hp = int(stats.current_hp)
        self.total_hp = int(stats.total_hp)

    def plan_walk(self, delta_position):
        self.delta_position = delta_position

    def walk(self):
        new_position = self.position.delta_position(self.delta_position)
        self.move_position(new_position)
        self.delta_position = Position()

