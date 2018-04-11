import sys
import pygame

import game_level
import game_level_view
import save_menu
import load_menu

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
        view = game_level_view.GameLevelView(level, screen)
        player = level.player
        view.render()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif player.has_died():
                    menu = GameOverMenu(screen, view)
                    quit = menu.get_choice()
                    if quit:
                        sys.exit()
                    else:
                        level = game_level.GameLevel(screen, player_stats)
                        view = game_level_view.GameLevelView(level, screen)
                        player = level.player
                        view.render()
                        continue
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        player.plan_walk(y=-1)
                    elif event.key == pygame.K_DOWN:
                        player.plan_walk(y=1)
                    elif event.key == pygame.K_LEFT:
                        player.plan_walk(x=-1)
                    elif event.key == pygame.K_RIGHT:
                        player.plan_walk(x=1)
                    elif event.key == pygame.K_z:
                        player.plan_walk(0, 0)
                    elif event.key == pygame.K_s:
                        save_menu.SaveMenu(screen, view, level)
                    elif event.key == pygame.K_l:
                        menu = load_menu.LoadMenu(screen, view, level)
                        loaded_level = menu.run()
                        if loaded_level is not None:
                            level = loaded_level
                            view = game_level_view.GameLevelView(level, screen)
                            player = level.player
                            view.render()
                            continue
                    level.update()
                    view.render()