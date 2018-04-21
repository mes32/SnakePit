import dimensions
import pygame
import random

class PositionMap():
    """
    A dictionary of all MapEntities inside the GameLevel
    """

    def __init__(self, dimensions):
        self.dimensions = dimensions
        self.table = dict()
        self.set = set()

    def entity_at(self, position):
        tuple = position.tuple
        if not tuple in self.table:
            return None
        else:
            return self.table[tuple]

    def insert(self, position, item):
        # TODO: This if allows inserting at the same position twice
        # Eventually should take a closer look at delete() and remove() 
        if not self.is_vacant(position):
            entity = self.entity_at(position)
            self.delete(position)
            if entity in self.set:
                self.set.remove(entity)
            
        # self.remove(entity)
        tuple = position.tuple
        self.table[tuple] = item
        self.set.add(item)

    def delete(self, position):
        if self.is_vacant(position):
            return False
        tuple = position.tuple
        del self.table[tuple]
        return True

    def remove(self, entity):
        position = entity.position
        if entity in self.set:
            self.set.remove(entity)
            self.delete(position)

    def get_list(self):
        return list(self.set)

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