import random

import map_entity

class Snake(map_entity.MapEntity):
    """
    The basic snake enemies.
    """

    def __init__(self, creature_map, position):
        super(Snake, self).__init__(creature_map, position)
        self.creature_map = creature_map
        self.current_hp = 1
        self.total_hp = 1

    def wander(self, level):
        current_position = self.position
        p_move = 0.9

        terrain = level.terrain_map
        player = level.player_map
        creature = level.creature_map
        item = level.item_map

        move_up = current_position.delta(dy=-1)
        move_down = current_position.delta(dy=1)
        move_left = current_position.delta(dx=-1)
        move_right = current_position.delta(dx=1)
        positions = [move_up, move_down, move_left, move_right]

        for p in positions:
            if not player.is_vacant(p):
                player.entity_at(p).hit(1, 0.5)

        if (random.random() <= p_move):
            free_positions = list()
            for p in positions:
                if level.enemy_can_walk(p):
                    free_positions.append(p)
            
            if len(free_positions) > 0:
                random_index = random.randint(0, len(free_positions)-1)
                self.move_position(free_positions[random_index])

    def take_damage(self, damage):
        self.current_hp = self.current_hp - damage
        if self.current_hp < 0:
            self.current_hp = 0

    def is_dead(self):
        if self.current_hp <= 0:
            return True
        else:
            return False

    def __str__(self):
        return "snake: " + str(self.position)
