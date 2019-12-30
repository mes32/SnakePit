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
        depth = level.depth
        level.terrain_map = terrain_map.TerrainMap()
        if depth == 1:
            level.player_map = PositionMap()
        level.creature_map = PositionMap()
        level.item_map = PositionMap()

        # Level parameters
        floor_area = 256
        room_buffer_width = 1 # eventually -> unif(1, 5)
        room_area = 64
        # room_area_var = N/A
        # floor_horizontal_bias = 1
        # room_horizontal_bias = 1
        num_rooms = 4
        # graph_connectivity = N/A
        heart_spat_period = 64
        snake_spat_period = 64

        # 1. Create room seeds
        # 2. Place room seeds
        # 3. Grow rooms seeds until done
        # 4. Place stairs
        # 5. Place snakes
        # 6. Place hearts

        self._init_terrain()

        if depth == 1:
            self._init_player(level.initial_player_stats)
        else:
            position = self._drop_player()
            level.player.move_position(position)

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
        floor_width = 19
        floor_height = 19

        x_room = 1
        y_room = 1
        w_room = 5
        h_room = 5

        for x in range(0, floor_width):
            for y in range(0, floor_height):
                position = map_position.MapPosition(x, y)
                new_terrain = wall.Wall(self.level.terrain_map, position)

        for x in range(0, floor_width):
            for y in range(0, floor_height):
                position = map_position.MapPosition(x, y)
                if x >= x_room and  x < x_room + w_room and y >= y_room and y < y_room + h_room:
                    new_terrain = floor.Floor(self.level.terrain_map, position)

        position = self._drop_stairs()
        new_terrain = stairs_down.StairsDown(self.level.terrain_map, position)

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
