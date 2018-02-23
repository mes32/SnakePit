import pygame
import playing_field
import player_character

GRID_CELL = width, height = 64, 64
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

    def _cell_at(self, x, y):
        x0 = x * GRID_CELL[0]
        y0 = y * GRID_CELL[1]
        x1 = (x + 1) * GRID_CELL[0]
        y1 = (y + 1) * GRID_CELL[1]
        return pygame.Rect(x0, y0, x1, y1)

    def _render_walls(self, screen):
        dim = self.field.dimensions
        width = dim[0]
        height = dim[1]

        for x in range(0, width):
            for y in range(0, height):
                if x == 0 or x == width-1 or y == 0 or y == height-1:
                    rect = self._cell_at(x, y)
                    screen.blit(self.wall_image, rect)

    def _render_enemies(self, screen):
        enemies = self.field.enemies
        for enemy in enemies:
            position = enemy.position
            x = position[0]
            y = position[1]
            rect = self._cell_at(x, y)
            screen.blit(self.snake_image, rect)

    def _render_player(self, screen):
        position = self.field.player_character.position
        x = position[0]
        y = position[1]
        rect = self._cell_at(x, y)
        screen.blit(self.player_image, rect)
