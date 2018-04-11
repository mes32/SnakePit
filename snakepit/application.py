import pygame

import game_loop

title = "Snake Pit"
screen_size = width, height = 576, 596

class Application():
    """
    The main application window
    """

    def __init__(self):
        pygame.init()
        pygame.display.set_caption(title)
        self.screen = pygame.display.set_mode(screen_size)

    def run(self):
        game_loop.GameLoop(self.screen)