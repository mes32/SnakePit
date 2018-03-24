import sys
import pygame

import game_level

from game_over_menu import GameOverMenu
from player_stats import PlayerStats
from position import Position

class GameLoop():
    """
    The current game session. Contains the main game loop.
    """

    def __init__(self, screen):
        player_stats = PlayerStats()
        level = game_level.GameLevel(screen, player_stats)
        player = level.player
        level.display()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif player.has_died():
                    menu = GameOverMenu(screen, level)
                    quit = menu.get_choice()
                    if quit:
                        sys.exit()
                    else:
                        level = PlayingField(screen, player_stats)
                        player = level.player
                        break
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        player.plan_walk(y=-1)
                    elif event.key == pygame.K_DOWN:
                        player.plan_walk(y=1)
                    elif event.key == pygame.K_LEFT:
                        player.plan_walk(x=-1)
                    elif event.key == pygame.K_RIGHT:
                        player.plan_walk(x=1)
                    level.update()
                    level.display()