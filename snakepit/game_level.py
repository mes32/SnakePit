import pygame
import random

import position
import terrain_map

from dimensions import Dimensions
from game_level_view import GameLevelView
from heart import Heart
from player_character import PlayerCharacter
from position import Position
from position_map import PositionMap
from snake import Snake
from terrain import Terrain

class GameLevel():
    """
    The current level of the game.
    """

    dimensions = Dimensions(10, 10)
    terrain_map = terrain_map.TerrainMap(dimensions)
    player_map = PositionMap(dimensions)
    creature_map = PositionMap(dimensions)
    item_map = PositionMap(dimensions)

    def __init__(self, screen, player_stats):
        
        self.view = GameLevelView(self, screen)
        self.dim = False

        self._init_terrain()
        self._init_player(player_stats)
        self._init_creatures()
        self._init_items()

    def _init_terrain(self):
        width = self.dimensions.get_width()
        height = self.dimensions.get_height()

        for x in range(0, width):
            for y in range(0, height):
                walkable = True
                if x == 0 or x == width-1 or y == 0 or y == height-1:
                    walkable = False
                else:
                    walkable = True
                position = Position(x, y)
                terrain = Terrain(self.terrain_map, position, walkable)
                self.terrain_map.insert(position, terrain)

    def _init_player(self, player_stats):
        position = self._rand_vacant()
        self.player = PlayerCharacter(self.player_map, position)
        self.player.copy_stats(player_stats)
        self.player_map.insert(position, self.player)

    def _init_creatures(self):
        num_enemies = 1
        for e in range(0, num_enemies):
            position = self._rand_vacant()
            enemy = Snake(self.creature_map, position)
            self.creature_map.insert(position, enemy)

    def _init_items(self):
        item_map = self.item_map
        num_items = 3
        for i in range(0, num_items):
            position = self._rand_vacant()
            item = Heart(item_map, position)
            item_map.insert(position, item)

    def update(self):
        print("in update()")
        self._update_player_character()
        self._update_items()
        self._update_enemies()

    def _update_items(self):
        item_list = self.item_map.list
        for item in item_list:
            if type(item) is Heart and item.is_consumed == True:
                self.item_map.remove(item)

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
            else:
                player.walk()

    def _update_enemies(self):
        creature_list = self.creature_map.list
        for enemy in creature_list:
            if enemy.is_dead():
                creature_list.remove(enemy)

        # for enemy in creature_list:
        #     enemy.wander(self.terrain_map)

    def _rand_vacant(self):
        max_x = self.dimensions.get_width() - 1
        max_y = self.dimensions.get_height() - 1
        while True:
            x = random.randint(0, max_x)
            y = random.randint(0, max_y)
            test_position = position.Position(x, y)
            if self.terrain_map.is_vacant(test_position) and self.player_map.is_vacant(test_position) and self.creature_map.is_vacant(test_position):
                return test_position

    def set_dim(self, dim):
        self.dim = dim

    def display(self):
        self.view.render()