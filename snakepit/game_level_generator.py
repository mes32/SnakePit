import random
import pygame

import snake
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
# from snake import Snake

class GameLevelGenerator():
    """
    Procedural generator for GameLevel.
    """

    def __init__(self, level):
        self.level = level

        level.terrain_map = terrain_map.TerrainMap(level.dimensions)
        if level.depth == 1:
            level.player_map = PositionMap(level.dimensions)
        level.creature_map = PositionMap(level.dimensions)
        level.item_map = PositionMap(level.dimensions)

        self._init_terrain()
        if level.depth == 1:
            self._init_player(self.level.initial_player_stats)
        else:
            position = self.level.rand_vacant()
            self.level.player.move_position(position)

        self._init_creatures()
        self._init_items()

    def _init_terrain(self):
        width = 30
        # height = self.level.dimensions.get_height()
        height = 30

        # for x in range(0, width):
        #     for y in range(0, height):
        #         position = Position(x, y)
        #         # if x == 0 or x == width-1 or y == 0 or y == height-1:
        #         new_terrain = wall.Wall(self.level.terrain_map, position)
        #         # else:
        #         #     new_terrain = terrain.Terrain(self.level.terrain_map, position)

        # self._carve_room()

        x_room = random.randint(1, 1)
        y_room = random.randint(1, 1)
        w_room = random.randint(5, 8)
        h_room = random.randint(5, 8)

        for x in range(0, width):
            for y in range(0, height):
                position = Position(x, y)
                new_terrain = wall.Wall(self.level.terrain_map, position)

        for x in range(0, width):
            for y in range(0, height):
                position = Position(x, y)
                if x >= x_room and  x < x_room + w_room and y >= y_room and y < y_room + h_room:
                    new_terrain = terrain.Terrain(self.level.terrain_map, position)
                # elif x >= x_room + w_room or y >= y_room + h_room:
                #      new_terrain = wall.Wall(self.level.terrain_map, position)
                # elif x == 0 or x == width-1 or y == 0 or y == height-1:
                #     new_terrain = wall.Wall(self.level.terrain_map, position)
                # else:
                #     new_terrain = terrain.Terrain(self.level.terrain_map, position)

        position = self.level.rand_vacant()
        new_terrain = stairs_down.StairsDown(self.level.terrain_map, position)

    def _carve_room(self):
        width = random.randint(7, 14) 
        height = 7

        # x_start = random.randint(1, 50)
        # y_start = random.randint(1, 50)
        x_start = 2
        y_start = 2

        # for x in range(x_start, width):
        #     for y in range(y_start, height):
        #         position = Position(x, y)
        #         new_terrain = terrain.Terrain(self.level.terrain_map, position)

        for x in range(0, 100):
            for y in range(0, 100):
                position = Position(x, y)
                if x >= 50 and x < 80 and y >= 50 and y < 80:
                    new_terrain = terrain.Terrain(self.level.terrain_map, position)
                else:
                    new_terrain = wall.Wall(self.level.terrain_map, position)

    def _init_player(self, player_stats):
        position = self.level.rand_vacant()
        self.level.player = PlayerCharacter(self.level.player_map, position)
        self.level.player.move_position(position)
        self.level.player.copy_stats(player_stats)

    def _init_creatures(self):
        num_enemies = self.level.depth
        for e in range(0, num_enemies):
            position = self.level.rand_vacant()
            enemy = snake.Snake(self.level.creature_map, position)

    def _init_items(self):
        item_map = self.level.item_map
        num_items = 2
        for i in range(0, num_items):
            position = self.level.rand_vacant()
            item = Heart(item_map, position)
