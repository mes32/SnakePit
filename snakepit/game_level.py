
import random

import game_level_generator
import heart
import snake
import stairs_down

class GameLevel():
    """
    The current level of the game.
    """

    def __init__(self, screen, player_stats):
        self.depth = 1
        self.kills = 0
        self.timestamp = ""

        self.initial_player_stats = player_stats
        self.player = None
        
        self.terrain_map = None
        self.player_map = None
        self.creature_map = None
        self.item_map = None

        game_level_generator.GameLevelGenerator(self)

    def update(self):
        self._update_player_character()
        self._update_items()
        self._update_enemies()

    def player_can_walk(self, position):
        terrain = self.terrain_map
        creatures = self.creature_map
        if terrain.is_walkable(position) and creatures.is_vacant(position):
            return True
        return False

    def player_can_drop(self, position):
        terrain = self.terrain_map
        creatures = self.creature_map
        items = self.item_map
        if terrain.is_open(position) and creatures.is_vacant(position) and items.is_vacant(position):
            return True
        return False

    def item_can_drop(self, position):
        terrain = self.terrain_map
        creatures = self.creature_map
        items = self.item_map
        if terrain.is_open(position) and creatures.is_vacant(position) and items.is_vacant(position):
            return True
        return False

    def enemy_can_walk(self, position):
        terrain = self.terrain_map
        creatures = self.creature_map
        items = self.item_map
        if terrain.is_open(position) and creatures.is_vacant(position) and items.is_vacant(position):
            return True
        return False

    def enemy_can_drop(self, position):
        # TODO: Test distance from player
        terrain = self.terrain_map
        creatures = self.creature_map
        items = self.item_map
        if terrain.is_open(position) and creatures.is_vacant(position) and items.is_vacant(position):
            return True
        return False

    def _update_items(self):
        item_list = self.item_map.list()
        for item in item_list:
            if type(item) is heart.Heart and item.is_consumed == True:
                item.delete()

    def _update_player_character(self):
        player = self.player
        position = player.position
        dx = player.delta_position.x
        dy = player.delta_position.y
        new_position = position.delta(dx, dy)

        terrain_map = self.terrain_map
        item_map = self.item_map
        creature_map = self.creature_map

        terrain = terrain_map.entity_at(new_position)
        if terrain.is_walkable():
            item = item_map.entity_at(new_position)
            creature = creature_map.entity_at(new_position)
            if item is not None and type(item) is heart.Heart:
                player.pickup(item)
                player.walk()
            elif creature is not None and type(creature) is snake.Snake:
                player.attack(creature)
                player.reset()
            elif type(terrain) is stairs_down.StairsDown:
                player.walk()
                self._down_level()
            else:
                player.walk()

    def _update_enemies(self):
        creature_map = self.creature_map
        creature_list = creature_map.list()
        for enemy in creature_list:
            if enemy.is_dead():
                enemy.delete()
                self.kills = self.kills + 1

        for enemy in creature_list:
            enemy.wander(self)

    def _down_level(self):
        self.depth = self.depth + 1
        game_level_generator.GameLevelGenerator(self)
