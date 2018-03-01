import pygame
import position
import playing_field
import player_character

from dimensions import Dimensions

DISPLAY_BAR_HEIGHT = 20
GRID_CELL = Dimensions(64, 64)
COLOR_BLACK = 0, 0, 0

class PlayingFieldView():
    player_image = pygame.image.load("./resources/images/PlayerCharacter.png")
    wall_image = pygame.image.load("./resources/images/Wall.png")
    snake_image = pygame.image.load("./resources/images/Snake.png")
    heart_image = pygame.image.load("./resources/images/Heart.png")

    def __init__(self, field, screen):
        self.field = field
        self.screen = screen

    def render(self):
        self.screen.fill(COLOR_BLACK)
        self._render_terrain()
        self._render_items()
        self._render_enemies()
        self._render_player()
        pygame.display.flip()

    def _cell_at(self, position):
        x = position.get_x()
        y = position.get_y()
        width = GRID_CELL.get_width()
        height = GRID_CELL.get_height()

        x0 = x * width
        y0 = y * height + DISPLAY_BAR_HEIGHT
        x1 = (x + 1) * width
        y1 = (y + 1) * height + DISPLAY_BAR_HEIGHT
        return pygame.Rect(x0, y0, x1, y1)

    def _draw_at(self, image, position):
        rect = self._cell_at(position)
        self.screen.blit(image, rect)

    def _render_terrain(self):
        terrain = self.field.terrain
        for tile in terrain:
            self._draw_at(self.wall_image, tile.position)

    def _render_items(self):
        items = self.field.items
        for item in items:
            self._draw_at(self.heart_image, item.position)         

    def _render_enemies(self):
        enemies = self.field.enemies
        for enemy in enemies:
            self._draw_at(self.snake_image, enemy.position)

    def _render_player(self):
        player = self.field.player
        self._draw_at(self.player_image, player.position)
