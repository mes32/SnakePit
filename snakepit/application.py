import pygame

from game_session import GameSession

title = "Snake Pit"
screen_size = width, height = 640, 640

class Application():
    """
    The main application window
    """

    def __init__(self):
        pygame.init()
        pygame.display.set_caption(title)
        self.screen = pygame.display.set_mode(screen_size)

    def run(self):
        GameSession(self.screen)