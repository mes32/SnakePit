import pygame

from mappable_entity import MappableEntity
from position import Position

class Snake(MappableEntity):
    """
    The basic snake enemies.
    """

    def __init__(self, position_lookup, position):
        super(Snake, self).__init__(position_lookup, position)
        self.current_hp = 1
        self.total_hp = 1
