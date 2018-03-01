import pygame

from mappable_entity import MappableEntity
from position import Position
from snake import Snake

class PlayerCharacter(MappableEntity):
    """
    The player's character in the game.
    """

    def __init__(self, position_lookup, position):
        super(PlayerCharacter, self).__init__(position_lookup, position)
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

    def reset(self):
        self.delta_position = Position()

    def attack(self, enemy):
        damage = 1
        enemy.take_damage(damage)
        self.current_hp = self.current_hp - 1
        if self.current_hp < 0:
            self.current_hp = 0

        print("HP: %s / %s" % (self.current_hp, self.total_hp))

    def pickup(self, item):
        item.consume()
        self.current_hp = self.current_hp + 1
        if self.current_hp > self.total_hp:
            self.current_hp = self.total_hp

        print("HP: %s / %s" % (self.current_hp, self.total_hp))


