import pygame

import terrain

class Floor(terrain.Terrain):
    """
    Type of Terrrain that is a vacant space of floor
    """

    image = pygame.image.load("./resources/images/Floor.png")
    walkable = True
