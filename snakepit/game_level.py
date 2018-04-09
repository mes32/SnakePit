import pygame
import random

import game_level_generator
import position
import stairs_down
import terrain_map
import terrain
import wall

from dimensions import Dimensions
from heart import Heart
from player_character import PlayerCharacter
from position import Position
from position_map import PositionMap
from snake import Snake

class GameLevel():
    """
    The current level of the game.
    """

    dimensions = Dimensions(10, 10)

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

    def rand_vacant(self):
        max_x = self.dimensions.get_width() - 1
        max_y = self.dimensions.get_height() - 1
        while True:
            x = random.randint(0, max_x)
            y = random.randint(0, max_y)
            test_position = position.Position(x, y)
            if self.terrain_map.is_vacant(test_position) and self.player_map.is_vacant(test_position) and self.creature_map.is_vacant(test_position):
                return test_position

    def _update_items(self):
        item_list = self.item_map.get_list()
        for item in item_list:
            if type(item) is Heart and item.is_consumed == True:
                item.delete()

    def _update_player_character(self):
        player = self.player
        position = player.position
        dx = player.delta_position.get_x()
        dy = player.delta_position.get_y()
        new_position = position.delta(dx, dy)

        terrain_map = self.terrain_map
        item_map = self.item_map
        creature_map = self.creature_map

        terrain = terrain_map.entity_at(new_position)
        if terrain.is_walkable():
            item = item_map.entity_at(new_position)
            creature = creature_map.entity_at(new_position)
            if item is not None and type(item) is Heart:
                player.pickup(item)
                player.walk()
            elif creature is not None and type(creature) is Snake:
                player.attack(creature)
                player.reset()
            elif type(terrain) is stairs_down.StairsDown:
                player.walk()
                self._down_level()
            else:
                player.walk()

    def _update_enemies(self):
        creature_map = self.creature_map
        creature_list = creature_map.get_list()
        for enemy in creature_list:
            if enemy.is_dead():
                enemy.delete()
                self.kills = self.kills + 1

        for enemy in creature_list:
            enemy.wander(self)

    def _down_level(self):
        self.depth = self.depth + 1
        game_level_generator.GameLevelGenerator(self)
