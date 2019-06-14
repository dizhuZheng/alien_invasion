from button import Button
import pygame.font

class PauseButton(Button):
    """make a shield botton"""

    def __init__(self, ai_settings, screen, msg):
        super().__init__(ai_settings, screen, msg)
        self.button_color = (66, 134, 244)
        self.width, self.height = 60, 30
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.right = self.screen_rect.right - 20
        self.rect.bottom = self.screen_rect.bottom - 50
