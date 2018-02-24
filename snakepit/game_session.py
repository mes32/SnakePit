import sys
import pygame

from player_stats import PlayerStats
from playing_field import PlayingField

class GameSession():
    """
    The current game session. Contains the main game loop.
    """

    def __init__(self, screen):
        player_stats = PlayerStats()
        field = PlayingField(screen, player_stats)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        i = 0
                        # player.indicate_walk(0, -1)
                    elif event.key == pygame.K_DOWN:
                        i = 0
                        # player.indicate_walk(0, 1)
                    elif event.key == pygame.K_LEFT:
                        i = 0
                        # player.indicate_walk(-1, 0)
                    elif event.key == pygame.K_RIGHT:
                        i = 0
                        # player.indicate_walk(1, 0)
            field.update()
            field.display()
