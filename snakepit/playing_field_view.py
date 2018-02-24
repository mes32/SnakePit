import pygame
import position
import playing_field
import player_character

from dimensions import Dimensions

GRID_CELL = Dimensions(64, 64)
COLOR_BLACK = 0, 0, 0

class PlayingFieldView():
    
    def __init__(self, field):
        self.field = field

        self.player_image = pygame.image.load("./resources/images/PlayerCharacter.png")
        self.wall_image = pygame.image.load("./resources/images/Wall.png")
        self.snake_image = pygame.image.load("./resources/images/Snake.png")

    def render(self, screen):
        screen.fill(COLOR_BLACK)
        self._render_walls(screen)
        #self._render_items(screen)
        self._render_enemies(screen)
        self._render_player(screen)
        pygame.display.flip()

    def _cell_at(self, position):
        x = position.get_x()
        y = position.get_y()
        width = GRID_CELL.get_width()
        height = GRID_CELL.get_height()

        x0 = x * width
        y0 = y * height
        x1 = (x + 1) * width
        y1 = (y + 1) * height
        return pygame.Rect(x0, y0, x1, y1)

    def _render_walls(self, screen):
        dimensions = self.field.dimensions
        width = dimensions.get_width()
        height = dimensions.get_height()

        for x in range(0, width):
            for y in range(0, height):
                if x == 0 or x == width-1 or y == 0 or y == height-1:
                    rect = self._cell_at(position.Position(x, y))
                    screen.blit(self.wall_image, rect)

    def _render_enemies(self, screen):
        enemies = self.field.enemies
        for enemy in enemies:
            rect = self._cell_at(enemy.position)
            screen.blit(self.snake_image, rect)

    def _render_player(self, screen):
        position = self.field.player_character.position
        rect = self._cell_at(position)
        screen.blit(self.player_image, rect)
