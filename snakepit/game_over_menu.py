import pygame

class GameOverMenu():
    """
    Menu shown when the current game ends
    """

    TYPE_FACE = 'freesansbold.ttf'
    FONT_SIZE = 28
    PROMPT_TEXT = 'You have died. Play again: y/n?'
    WHITE = (255, 255, 255)

    def __init__(self, screen, view):
        view.render_dim()

        screen_width = screen.get_width()
        screen_height = screen.get_height()
        
        defaultfont = pygame.font.Font(self.TYPE_FACE, self.FONT_SIZE)

        prompt_text_render = defaultfont.render(self.PROMPT_TEXT, True, self.WHITE)
        prompt_text_rect = prompt_text_render.get_rect()
        width = prompt_text_rect.width
        height = prompt_text_rect.height

        stat_text = 'Depth: {}, Kills: {}'.format(view.field.depth, view.field.kills)
        stat_text_render = defaultfont.render(stat_text, True, self.WHITE)

        screen.blit(prompt_text_render, ((screen_width - width)/2.0, (screen_height - height)/2.0))
        screen.blit(stat_text_render, ((screen_width - width)/2.0, ((screen_height - height)/2.0) - 3.0 * height))
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