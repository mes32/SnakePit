import pygame
import random

from dimensions import Dimensions
from player_character import PlayerCharacter
from playing_field_view import PlayingFieldView
from position import Position
from position_lookup import PositionLookup
from snake import Snake
from terrain import Terrain

DIMENSIONS = Dimensions(10, 10)

class PlayingField():
    """
    The current level of the game.
    """

    def __init__(self, screen, player_stats):
        self.dimensions = DIMENSIONS
        self.lookup = PositionLookup(self.dimensions)
        self.view = PlayingFieldView(self, screen)

        self._init_terrain()
        self._init_player(player_stats)
        self._init_enemies()
        # self._init_items()

    def _init_terrain(self):
        self.terrain = list()
        width = self.dimensions.get_width()
        height = self.dimensions.get_height()

        for x in range(0, width):
            for y in range(0, height):
                if x == 0 or x == width-1 or y == 0 or y == height-1:
                    position = Position(x, y)
                    wall_tile = Terrain(self.lookup, position)
                    self.terrain.append(wall_tile)

    def _init_player(self, player_stats):
        position = self.lookup.rand_vacant()
        self.player = PlayerCharacter(self.lookup, position)
        self.player.copy_stats(player_stats)

    def _init_enemies(self):
        self.enemies = list()

        num_enemies = 3
        for e in range(0, num_enemies):
            position = self.lookup.rand_vacant()
            enemy = Snake(self.lookup, position)
            self.enemies.append(enemy)

    def update(self):
        self._update_player_character()
        self._update_enemies()

    def _update_player_character(self):
        player = self.player
        position = player.position
        new_position = position.delta_position(player.delta_position)

        entity = self.lookup.entity_at(new_position)
        if entity is None:
            player.walk()
        elif type(entity) is Snake:
            player.attack(entity)
            player.reset()

    def _update_enemies(self):
        for enemy in self.enemies:
            if enemy.is_dead():
                self.enemies.remove(enemy)
                self.lookup.remove(enemy)

    def display(self):
        self.view.render()