import pygame
from pygame.sprite import Sprite
import random

class Bonus(Sprite):

    def __init__(self, screen, ai_settings):
        """Create a bullet at the ship's current position"""
        super().__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 20, 20)
        self.rect.center = (random.randint(0, ai_settings.screen_width), 0)
        self.y = float(self.rect.y)
        self.color = (244, 134, 66)
        self.speed_factor = 10

    def update(self):
        """move the bullet up the screen"""
        #update the decimal position of the bullet
        self.y += self.speed_factor
        #update the rect position
        self.rect.y = self.y

    def draw(self):
        """draw the bullet to screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
