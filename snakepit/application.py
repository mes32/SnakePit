import pygame
from pygame.locals import *
from game_session import GameSession

class Application():

    def __init__(self):
        pygame.init()

    def run(self):
        GameSession()