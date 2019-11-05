import pygame
from pygame.sprite import Sprite
import random

class Bonus(Sprite):

    def __init__(self, screen, ai_settings):
        """Create a bullet at the ship's current position"""
        super().__init__()
        self.screen = screen
        self.image = pygame.image.load('images/star.bmp')
        self.ai_settings = ai_settings
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.x = random.randrange(ai_settings.screen_width - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speed_factor = random.randrange(1, 8)

    def update(self):
        """move the bullet up the screen"""
        self.rect.y += self.speed_factor


    def blitme(self):
        """draw the bonus at its current location"""
        self.screen.blit(self.image, self.rect)
