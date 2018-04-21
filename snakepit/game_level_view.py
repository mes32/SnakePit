import pygame

import game_level
import heart
import map_position
import player_character

from dimensions import Dimensions

class GameLevelView():

    FIELD_OF_VIEW = Dimensions(9, 9)
    DISPLAY_BAR_CELL = Dimensions(20, 20)
    GRID_CELL = Dimensions(64, 64)

    COLOR_BLACK = (0, 0, 0)
    COLOR_DIM = (0, 0, 0, 200)

    player_image = pygame.image.load("./resources/images/PlayerCharacter.png")
    # wall_image = pygame.image.load("./resources/images/Wall.png")
    snake_image = pygame.image.load("./resources/images/Snake.png")
    heart_image = pygame.image.load("./resources/images/Heart.png")
    display_heart_full = pygame.image.load("./resources/images/IndicatorHeart_Full.png")
    display_heart_empty = pygame.image.load("./resources/images/IndicatorHeart_Empty.png")

    def __init__(self, field, screen):
        width = self.FIELD_OF_VIEW.width
        height = self.FIELD_OF_VIEW.height

        width_pixels = width * self.GRID_CELL.width
        height_pixels = height * self.GRID_CELL.height + self.DISPLAY_BAR_CELL.height
        self.field = field
        self.player = field.player
        screen = pygame.display.set_mode((width_pixels, height_pixels))
        self.screen = screen


    def render(self):
        self.screen.fill(self.COLOR_BLACK)
        self._render_terrain()
        self._render_items()
        self._render_enemies()
        self._render_player()
        self._render_display_bar()
        pygame.display.flip()

    def render_dim(self):
        self.screen.fill(self.COLOR_BLACK)
        self._render_terrain()
        self._render_items()
        self._render_enemies()
        self._render_player()
        self._render_display_bar()
        self._render_dim_overlay()
        pygame.display.flip()

    def _cell_at(self, position):
        offset_vertical = self.DISPLAY_BAR_CELL.get_height()
        x = position.x
        y = position.y
        width = self.GRID_CELL.width
        height = self.GRID_CELL.height

        x0 = x * width
        y0 = y * height + offset_vertical
        x1 = x0 + width
        y1 = y0 + height
        return pygame.Rect(x0, y0, x1, y1)

    def _draw_at(self, image, position):
        relative_position = self._relative_position(position)
        if relative_position is None or image is None:
            return
        rect = self._cell_at(relative_position)
        self.screen.blit(image, rect)

    def _relative_position(self, pos):
        full_x = self.FIELD_OF_VIEW.width
        full_y = self.FIELD_OF_VIEW.height
        half_x = int(self.FIELD_OF_VIEW.width / 2.0)
        half_y = int(self.FIELD_OF_VIEW.height / 2.0)

        rel_x = (pos.x - self.player.position.x) + half_x
        rel_y = (pos.y - self.player.position.y) + half_y

        if rel_x < 0 or rel_x >= full_x or rel_y < 0 or rel_y >= full_y:
            return None
        else:
            return map_position.MapPosition(rel_x, rel_y)

    def _render_terrain(self):
        terrain_list = self.field.terrain_map.list()
        for terrain in terrain_list:
            self._draw_at(terrain.image, terrain.position)

    def _render_items(self):
        item_list = self.field.item_map.list()
        for item in item_list:
            if type(item) is heart.Heart:
                self._draw_at(self.heart_image, item.position)

    def _render_enemies(self):
        enemies = self.field.creature_map.list()
        for enemy in enemies:
            self._draw_at(self.snake_image, enemy.position)

    def _render_player(self):
        player = self.field.player
        self._draw_at(self.player_image, player.position)

    def _render_display_bar(self):
        total_hearts = self.field.player.total_hp
        full_hearts = self.field.player.current_hp
        empty_hearts = total_hearts - full_hearts

        for f in range(0, full_hearts):
            self._display_bar(self.display_heart_full, f, total_hearts)

        for e in range(0, empty_hearts):
            self._display_bar(self.display_heart_empty, e + full_hearts, total_hearts)

    def _display_bar(self, image, slot, total_slots):
        height = self.DISPLAY_BAR_CELL.height
        width = self.DISPLAY_BAR_CELL.width
        screen_width = self.GRID_CELL.width * self.FIELD_OF_VIEW.width
        offset_horizontal = 60
        back_slot = total_slots - slot - 1

        x0 = screen_width - (back_slot * width) - offset_horizontal
        y0 = 0
        x1 = x0 + width
        y1 = height
        rect = pygame.Rect(x0, y0, x1, y1)

        self.screen.blit(image, rect)

    def _render_dim_overlay(self):
        width = self.screen.get_width()
        height = self.screen.get_height()
        overlay = pygame.Surface((width, height), pygame.SRCALPHA)
        overlay.fill(self.COLOR_DIM)
        self.screen.blit(overlay, (0,0))