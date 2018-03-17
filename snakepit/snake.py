import random

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

    def wander(self):
        current_position = self.position
        p_move = 0.3
        if (random.random() <= p_move):
            pos_up = current_position.delta(y=-1)
            pos_down = current_position.delta(y=1)
            pos_left = current_position.delta(x=-1)
            pos_right = current_position.delta(x=1)

            available_positions = list()
            if self.position_lookup.is_vacant(pos_up):
                available_positions.append(pos_up)
            if self.position_lookup.is_vacant(pos_down):
                available_positions.append(pos_down)
            if self.position_lookup.is_vacant(pos_left):
                available_positions.append(pos_left)
            if self.position_lookup.is_vacant(pos_right):
                available_positions.append(pos_right)

            if len(available_positions) > 0:
                random_index = random.randint(0, len(available_positions)-1)
                self.move_position(available_positions[random_index])

    def take_damage(self, damage):
        self.current_hp = self.current_hp - damage
        if self.current_hp < 0:
            self.current_hp = 0

    def is_dead(self):
        if self.current_hp <= 0:
            return True
        else:
            return False
