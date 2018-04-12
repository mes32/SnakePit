import pygame

import game_loop
import game_level_view

title = "Snake Pit"
# screen_size = width, height = 576, 596

class Application():
    """
    The main application window
    """

    def __init__(self):
        pygame.init()
        pygame.display.set_caption(title)

        fov = game_level_view.GameLevelView.FIELD_OF_VIEW
        cell_dim = game_level_view.GameLevelView.GRID_CELL
        display_dim = game_level_view.GameLevelView.DISPLAY_BAR_CELL
        width = fov.width * cell_dim.width
        height = fov.height * cell_dim.height + display_dim.height
        screen_size = (width, height)

        self.screen = pygame.display.set_mode(screen_size)

    def run(self):
        game_loop.GameLoop(self.screen)