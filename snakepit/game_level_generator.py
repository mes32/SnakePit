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
        self._init_creatures()
        self._init_items()

        # self._init_terrain()
        # self._init_player(player_stats)
        # self._init_creatures()
        # self._init_items()

    def _init_terrain(self):
        width = self.level.dimensions.get_width()
        height = self.level.dimensions.get_height()

        for x in range(0, width):
            for y in range(0, height):
                position = Position(x, y)
                if x == 0 or x == width-1 or y == 0 or y == height-1:
                    new_terrain = wall.Wall(self.level.terrain_map, position)
                else:
                    new_terrain = terrain.Terrain(self.level.terrain_map, position)
        position = self.level.rand_vacant()
        new_terrain = stairs_down.StairsDown(self.level.terrain_map, position)

    def _init_player(self, player_stats):
        position = self.level.rand_vacant()
        self.level.player = PlayerCharacter(self.level.player_map, position)
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
