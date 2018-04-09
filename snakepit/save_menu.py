import datetime
import os
import pickle
import pygame
import time

class SaveMenu():
    """
    Menu shown when saving the current game
    """

    MEDIUM_TYPEFACE = "resources/fonts/Raleway-Medium.ttf"
    BOLD_TYPEFACE = "resources/fonts/Raleway-SemiBold.ttf"
    ITALIC_TYPEFACE = "resources/fonts/Raleway-Regular-Italic.ttf"
    FONT_SIZE = 26
    NOTE_SIZE = 16
    WHITE = (255, 255, 255)
    OFF_WHITE = (200, 200, 200)
    
    PATH_0 = "../data/savegame/0.pickle"
    PATH_1 = "../data/savegame/1.pickle"
    PATH_2 = "../data/savegame/2.pickle"
    PATH_3 = "../data/savegame/3.pickle"
    PATH_4 = "../data/savegame/4.pickle"

    SCRIPT_DIR = os.path.dirname(__file__)
    FILE_0 = os.path.join(SCRIPT_DIR, PATH_0)
    FILE_1 = os.path.join(SCRIPT_DIR, PATH_1)
    FILE_2 = os.path.join(SCRIPT_DIR, PATH_2)
    FILE_3 = os.path.join(SCRIPT_DIR, PATH_3)
    FILE_4 = os.path.join(SCRIPT_DIR, PATH_4)

    SAVE_SLOTS = [FILE_0, FILE_1, FILE_2, FILE_3, FILE_4]
    NUM_SLOTS = len(SAVE_SLOTS)

    TITLE_TEXT = "+++ SAVE GAME +++"

    def __init__(self, screen, view, level):
        self.screen = screen
        self.view = view
        self.level = level

        self.line_counter = 0
        self.selected = 0

        self.screen_width = screen.get_width()
        self.screen_height = screen.get_height()
        pygame.font.init()
        self.medium_type = pygame.font.Font(self.MEDIUM_TYPEFACE, self.FONT_SIZE)
        self.bold_type = pygame.font.Font(self.BOLD_TYPEFACE, self.FONT_SIZE)
        self.note_type = pygame.font.Font(self.ITALIC_TYPEFACE, self.NOTE_SIZE)

        self.display_slots = []
        for i in range(self.NUM_SLOTS):
            if os.path.exists(self.SAVE_SLOTS[i]):
                fh = open(self.SAVE_SLOTS[i], 'rb')
                temp_level = pickle.load(fh)
                timestamp = temp_level.timestamp
                self.display_slots.append("%d.    %s" % ((i+1), timestamp))
            else:
                self.display_slots.append("%d.    (empty)" % (i+1))

        self._run()

    def _display(self):
        self.line_counter = 0
        self.view.render_dim()
        self._center_text(self.TITLE_TEXT)
        for i in range(self.NUM_SLOTS):
            line_str = self.display_slots[i]
            if i == self.selected:
                self._left_text(line_str, True)
            else:
                self._left_text(line_str)

        self._note_text("")
        self._note_text("Use arrows keys to select a save slot. Press ESC to cancel.")
        pygame.display.flip()

    def _center_text(self, text):
        text_render = self.medium_type.render(text, True, self.OFF_WHITE)
        text_rect = text_render.get_rect()
        width = text_rect.width
        height = text_rect.height

        self.line_counter = self.line_counter + 1
        self.screen.blit(text_render, ((self.screen_width - width) / 2.0, (2.0 * self.line_counter) * self.FONT_SIZE))

    def _left_text(self, text, bold=False):
        if (bold):
            text_render = self.bold_type.render(text, True, self.WHITE)
        else:
            text_render = self.medium_type.render(text, True, self.OFF_WHITE)
        text_rect = text_render.get_rect()
        width = text_rect.width
        height = text_rect.height

        self.line_counter = self.line_counter + 1
        self.screen.blit(text_render, (80.0, (2.0 * self.line_counter) * self.FONT_SIZE))

    def _note_text(self, text):
        text_render = self.note_type.render(text, True, self.OFF_WHITE)
        text_rect = text_render.get_rect()
        width = text_rect.width
        height = text_rect.height

        self.line_counter = self.line_counter + 1
        self.screen.blit(text_render, ((self.screen_width - width) / 2.0, (2.0 * self.line_counter) * self.FONT_SIZE))

    def _run(self):
        self._display()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    k = event.key
                    if k == pygame.K_ESCAPE:
                        return;
                    elif k == pygame.K_RETURN:
                        if self.selected in range(self.NUM_SLOTS):
                            epoch_time = time.time()
                            timestamp = datetime.datetime.fromtimestamp(epoch_time).strftime("%x    %I:%M:%S %p")
                            fh = open(self.SAVE_SLOTS[self.selected], 'wb')
                            self.level.timestamp = timestamp
                            pickle.dump(self.level, fh)
                            return
                    elif k == pygame.K_DOWN:
                        self.selected = self.selected + 1
                        if self.selected >= self.NUM_SLOTS:
                            self.selected = 0
                        self._display()
                    elif k == pygame.K_UP:
                        self.selected = self.selected - 1
                        if self.selected < 0:
                            self.selected = self.NUM_SLOTS - 1
                        self._display()
                    elif k == pygame.K_1:
                        self.selected = 0
                        self._display()
                    elif k == pygame.K_2:
                        self.selected = 1
                        self._display()
                    elif k == pygame.K_3:
                        self.selected = 2
                        self._display()
                    elif k == pygame.K_4:
                        self.selected = 3
                        self._display()
                    elif k == pygame.K_5:
                        self.selected = 4
                        self._display()
