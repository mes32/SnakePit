import random

import map_entity

from position import Position

class Snake(map_entity.MapEntity):
    """
    The basic snake enemies.
    """

    def __init__(self, creature_map, position):
        super(Snake, self).__init__(creature_map, position)
        self.creature_map = creature_map
        self.current_hp = 1
        self.total_hp = 1

    def wander(self, terrain_map):
        current_position = self.position
        p_move = 0.3
        if (random.random() <= p_move):
            pos_up = current_position.delta(dy=-1)
            pos_down = current_position.delta(dy=1)
            pos_left = current_position.delta(dx=-1)
            pos_right = current_position.delta(dx=1)

            available_positions = list()
            if self.creature_map.is_vacant(pos_up) and terrain_map.is_vacant(pos_up):
                available_positions.append(pos_up)
            if self.creature_map.is_vacant(pos_down) and terrain_map.is_vacant(pos_down):
                available_positions.append(pos_down)
            if self.creature_map.is_vacant(pos_left) and terrain_map.is_vacant(pos_left):
                available_positions.append(pos_left)
            if self.creature_map.is_vacant(pos_right) and terrain_map.is_vacant(pos_right):
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
