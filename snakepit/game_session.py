import sys
import pygame

from game_over_menu import GameOverMenu
from player_stats import PlayerStats
from playing_field import PlayingField
from position import Position

class GameSession():
    """
    The current game session. Contains the main game loop.
    """

    def __init__(self, screen):
        player_stats = PlayerStats()
        field = PlayingField(screen, player_stats)
        player = field.player
        while True:
            field.display()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif player.has_died():
                    menu = GameOverMenu(screen, field)
                    quit = menu.get_choice()
                    if quit:
                        sys.exit()
                    else:
                        field = PlayingField(screen, player_stats)
                        player = field.player
                        break
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        player.plan_walk(Position(y=-1))
                    elif event.key == pygame.K_DOWN:
                        player.plan_walk(Position(y=1))
                    elif event.key == pygame.K_LEFT:
                        player.plan_walk(Position(x=-1))
                    elif event.key == pygame.K_RIGHT:
                        player.plan_walk(Position(x=1))
                    field.update()
                    field.display()