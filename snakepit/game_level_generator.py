import random
import pygame

import floor
import map_position
import snake
import stairs_down
import terrain_map
import terrain
import wall

from dimensions import Dimensions
from game_level_view import GameLevelView
from heart import Heart
from player_character import PlayerCharacter
from position_map import PositionMap

class GameLevelGenerator():
    """
    Procedural generator for GameLevel.
    """

    _DROP_COUNT = 40

    def __init__(self, level):
        self.level = level

        level.terrain_map = terrain_map.TerrainMap()
        if level.depth == 1:
            level.player_map = PositionMap()
        level.creature_map = PositionMap()
        level.item_map = PositionMap()

        self._init_terrain()
        if level.depth == 1:
            self._init_player(self.level.initial_player_stats)
        else:
            position = self._drop_player()
            self.level.player.move_position(position)

        self._init_creatures()
        self._init_items()

    def _drop_stairs(self):
        terrain = self.level.terrain_map
        while True:
            position = terrain.rand_position()
            if self.level.player_can_walk(position):
                return position

    def _drop_player(self):
        terrain = self.level.terrain_map
        while True:
            position = terrain.rand_position()
            if self.level.player_can_drop(position):
                return position

    def _drop_item(self):
        count = 0
        terrain = self.level.terrain_map
        while count < self._DROP_COUNT:
            count += 1
            position = terrain.rand_position()
            if self.level.item_can_drop(position):
                return position
        return None

    def _drop_enemy(self):
        count = 0
        terrain = self.level.terrain_map
        while count < self._DROP_COUNT:
            count += 1
            position = terrain.rand_position()
            if self.level.item_can_drop(position):
                return position
        return None

    def _init_terrain(self):
        depth = self.level.depth
        width = 30 + depth
        # height = self.level.dimensions.get_height()
        height = 30 + depth

        # for x in range(0, width):
        #     for y in range(0, height):
        #         position = Position(x, y)
        #         # if x == 0 or x == width-1 or y == 0 or y == height-1:
        #         new_terrain = wall.Wall(self.level.terrain_map, position)
        #         # else:
        #         #     new_terrain = terrain.Terrain(self.level.terrain_map, position)

        # self._carve_room()

        x_room = random.randint(1, 10)
        y_room = random.randint(1, 10)
        w_room = random.randint(5 + depth, 8 + depth)
        h_room = random.randint(5 + depth, 8 + depth)

        for x in range(0, width):
            for y in range(0, height):
                position = map_position.MapPosition(x, y)
                new_terrain = wall.Wall(self.level.terrain_map, position)

        for x in range(0, width):
            for y in range(0, height):
                position = map_position.MapPosition(x, y)
                if x >= x_room and  x < x_room + w_room and y >= y_room and y < y_room + h_room:
                    new_terrain = floor.Floor(self.level.terrain_map, position)
                # elif x >= x_room + w_room or y >= y_room + h_room:
                #      new_terrain = wall.Wall(self.level.terrain_map, position)
                # elif x == 0 or x == width-1 or y == 0 or y == height-1:
                #     new_terrain = wall.Wall(self.level.terrain_map, position)
                # else:
                #     new_terrain = terrain.Terrain(self.level.terrain_map, position)

        position = self._drop_stairs()
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
        #         position = map_position.MapPosition(x, y)
        #         new_terrain = terrain.Terrain(self.level.terrain_map, position)

        for x in range(0, 100):
            for y in range(0, 100):
                position = Position(x, y)
                if x >= 50 and x < 80 and y >= 50 and y < 80:
                    new_terrain = terrain.Terrain(self.level.terrain_map, position)
                else:
                    new_terrain = wall.Wall(self.level.terrain_map, position)

    def _init_player(self, player_stats):
        position = self._drop_player()
        self.level.player = PlayerCharacter(self.level.player_map, position)
        self.level.player.move_position(position)
        self.level.player.copy_stats(player_stats)

    def _init_creatures(self):
        num_enemies = self.level.depth
        for e in range(0, num_enemies):
            position = self._drop_enemy()
            if position is None:
                print("lvl-%d Unable to find open spot for (enemy)." % self.level.depth)
            else:
                enemy = snake.Snake(self.level.creature_map, position)

    def _init_items(self):
        item_map = self.level.item_map
        num_items = 2
        for i in range(0, num_items):
            position = self._drop_item()
            if position is None:
                print("lvl-%d Unable to find open spot for (item)." % self.level.depth)
            else:
                item = Heart(item_map, position)
