import dimensions
import pygame
import random

import position

class PositionMap():
    """
    A dictionary of all MapEntities inside the GameLevel
    """

    def __init__(self, dimensions):
        self.dimensions = dimensions
        self.table = dict()
        self.list = list()

    def entity_at(self, position):
        tuple = position.get_tuple()
        if not tuple in self.table:
            return None
        else:
            return self.table[tuple]

    def insert(self, position, item):
        tuple = position.get_tuple()
        self.table[tuple] = item
        self.list.append(item)

    def delete(self, position):
        if self.is_vacant(position):
            return False
        tuple = position.get_tuple()
        del self.table[tuple]
        return True

    def remove(self, entity):
        position = entity.position
        if entity in self.list:
            self.list.remove(entity)
            self.delete(position)

    def move(self, position_start, position_end):
        entity_to_move = self.entity_at(position_start)
        if entity_to_move == None or not self.is_vacant(position_end) or self.is_vacant(position_start):
            return False
        self.delete(position_start)
        self.insert(position_end, entity_to_move)
        return True

    def is_vacant(self, position):
        if self.entity_at(position) == None:
            return True
        else:
            return False