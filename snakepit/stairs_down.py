import pygame

import terrain

class StairsDown(terrain.Terrain):
    """
    Type of Terrrain that is a downward staircase to a lower level
    """

    image = pygame.image.load("./resources/images/StairsDown.png")
    walkable = True
    open = False
