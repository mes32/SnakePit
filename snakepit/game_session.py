import sys
import pygame
from pygame.locals import *

class GameSession():

    def __init__(self):
        pygame.display.set_caption("Snake Pit")

        size = width, height = 640, 640
        speed = [3, 2]
        black = 0, 0, 0

        screen = pygame.display.set_mode(size)
        player_image = pygame.image.load("./resources/images/PlayerCharacter.png")
        player_rect = player_image.get_rect()

        # field = PlayingField()
        # player = PlayerCharacter()

        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()

            player_rect = player_rect.move(speed)
            if player_rect.left < 0 or player_rect.right > width:
                speed[0] = -speed[0]
            if player_rect.top < 0 or player_rect.bottom > height:
                speed[1] = -speed[1]

            screen.fill(black)
            screen.blit(player_image, player_rect)
            pygame.display.flip()

    