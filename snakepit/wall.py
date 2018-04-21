import pygame

import terrain

class Wall(terrain.Terrain):
    """
    Type of Terrrain that is an non-traversable wall
    """

    image = pygame.image.load("./resources/images/Wall.png")
    walkable = False
    open = False
