import pygame

class GameOverMenu():
    """
    Menu shown when the current game ends
    """

    PROMPT_TEXT = "You have died. Play again: y/n?"
    WHITE = (255, 255, 255)

    def __init__(self, screen, field):
        field.set_dim(True)
        field.display()

        screen_width = screen.get_width()
        screen_height = screen.get_height()
        
        defaultfont = pygame.font.Font('freesansbold.ttf', 28)
        text_render = defaultfont.render(self.PROMPT_TEXT, True, self.WHITE)
        text_rect = text_render.get_rect()
        width = text_rect.width
        height = text_rect.height

        screen.blit(text_render, ((screen_width - width)/2.0, (screen_height - height)/2.0))
        pygame.display.flip()
    
    def get_choice(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_n:
                        return True
                    elif event.key == pygame.K_y:
                        return False