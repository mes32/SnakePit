import pygame
import random

import position
import terrain_map
import terrain
import wall
import stairs_down

from dimensions import Dimensions
from game_level_view import GameLevelView
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
        
        self.view = GameLevelView(self, screen)
        self.dim = False

        self.terrain_map = terrain_map.TerrainMap(self.dimensions)
        self.player_map = PositionMap(self.dimensions)
        self.creature_map = PositionMap(self.dimensions)
        self.item_map = PositionMap(self.dimensions)

        self._init_terrain()
        self._init_player(player_stats)
        self._init_creatures()
        self._init_items()

    def _init_terrain(self):
        width = self.dimensions.get_width()
        height = self.dimensions.get_height()

        for x in range(0, width):
            for y in range(0, height):
                position = Position(x, y)
                if x == 0 or x == width-1 or y == 0 or y == height-1:
                    new_terrain = wall.Wall(self.terrain_map, position)
                else:
                    new_terrain = terrain.Terrain(self.terrain_map, position)

        position = self._rand_vacant()
        new_terrain = stairs_down.StairsDown(self.terrain_map, position)

    def _init_player(self, player_stats):
        position = self._rand_vacant()
        self.player = PlayerCharacter(self.player_map, position)
        self.player.copy_stats(player_stats)

    def _init_creatures(self):
        num_enemies = 3
        for e in range(0, num_enemies):
            position = self._rand_vacant()
            enemy = Snake(self.creature_map, position)

    def _init_items(self):
        item_map = self.item_map
        num_items = 2
        for i in range(0, num_items):
            position = self._rand_vacant()
            item = Heart(item_map, position)

    def update(self):
        self._update_player_character()
        self.display()
        self._update_items()
        self.display()
        self._update_enemies()
        self.display()

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
            else:
                player.walk()

    def _update_enemies(self):
        creature_map = self.creature_map
        creature_list = creature_map.get_list()
        for enemy in creature_list:
            if enemy.is_dead():
                enemy.delete()

        for enemy in creature_list:
            enemy.wander(self)

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