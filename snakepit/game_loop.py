import os
import sys
import pickle
import pygame

import game_level
import game_level_view

from game_over_menu import GameOverMenu
from player_stats import PlayerStats
from position import Position

class GameLoop():
    """
    The current game session. Contains the main game loop.
    """

    def __init__(self, screen):

        script_dir = os.path.dirname(__file__)
        path = "../data/savegame/001.pickle"
        # path = os.path.relpath("../data/savegame/001.pickle")
        save_file = os.path.join(script_dir, path)
        print(save_file)

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
                    elif event.key == pygame.K_1:
                        print(" -- save game.")
                        fh = open(save_file, "wb")
                        pickle.dump(level, fh)
                        continue
                    elif event.key == pygame.K_2:
                        if os.path.exists(save_file):
                            print(" -- load game.")
                            fh = open(save_file, "rb")
                            level = pickle.load(fh)
                            view = game_level_view.GameLevelView(level, screen)
                            player = level.player
                            view.render()
                            continue
                    level.update()
                    view.render()