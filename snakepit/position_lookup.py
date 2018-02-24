import pygame

from position import Position

class PositionLookup():
    """
    A dictionary of all items inside the PlayingField
    """

    def __init__(self):
        self.table = dict()

    def item_at(self, position):
        tuple = position.get_tuple()
        if not tuple in self.table:
            return None
        else:
            return self.table[tuple]

    def insert(self, position, item):
        tuple = position.get_tuple()
        self.table[tuple] = item

    def delete(self, position):
        tuple = position.get_tuple()
        del self.table[tuple]

    def move(self, position_start, position_end):
        item = self.item_at(position_start)
        if item == None:
            return False
        self.delete(position_start)
        self.insert(position_end, item)
        return True

    def is_vacant(self, position):
        tuple = position.get_tuple()
        if self.item_at(position) == None:
            return True
        else:
            return False