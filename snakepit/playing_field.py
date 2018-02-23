import pygame
import random

from player_character import PlayerCharacter
from playing_field_view import PlayingFieldView
from snake import Snake

DIMENSIONS = width, height = 10, 10

class PlayingField():
    """
    The current level of the game.
    """

    def __init__(self, player_character):
        self.dimensions = DIMENSIONS
        self.all_objects = dict()
        self.view = PlayingFieldView(self)

        self.player_character = player_character
        self.enemies = list()

        self._init_player_character()
        self._init_enemies()
        

    def _init_player_character(self):
        x = random.randint(1, 8)
        y = random.randint(1, 8)
        self.player_character.set_position(x, y)

    def _init_enemies(self):
        num_enemies = 2
        for e in range(0, num_enemies):
            enemy = None
            while enemy == None:
                x = random.randint(1, 8)
                y = random.randint(1, 8)
                player_position = self.player_character.position
                player_x = player_position[0]
                player_y = player_position[1]
                if x != player_x or y != player_y:
                    enemy = Snake(x, y)
            self.enemies.append(enemy)

    def update(self):
        self._update_player_character(self.player_character)
        #self._update_enemies()

    def _update_player_character(self, player):
        position = player.position
        new_x = position[0] + player.delta_x
        new_y = position[1] + player.delta_y
        new_position = new_x, new_y

        if self._is_wall(new_position):
            return
        else:
            player.finalize_walk()

    def _is_wall(self, position):
        x = position[0]
        y = position[1]

        if x == 0 or x == self.dimensions[0] - 1 or y == 0 or y == self.dimensions[1] - 1:
            return True
        return False

    def display(self, screen):
        self.view.render(screen)