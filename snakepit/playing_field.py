import pygame

from player_character import PlayerCharacter
from playing_field_view import PlayingFieldView

DIMENSIONS = width, height = 10, 10

class PlayingField():
    """
    The current level of the game.
    """

    def __init__(self, player_character):
        self.dimensions = DIMENSIONS
        self.player_character = player_character

        self.player_character.set_position(2, 2)
        self.view = PlayingFieldView(self)

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