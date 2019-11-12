import pygame
from pygame.sprite import Sprite

class Grenade(Sprite):

    def __init__(self, screen, x, y):
        """Create a bullet at the ship's current position"""
        super().__init__()
        self.screen = screen
        self.image = pygame.image.load('images/fire12.bmp')
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.y = float(self.rect.y)
        self.speed_factor = 15

    def update(self):
        """move the bullet up the screen"""
        self.y += self.speed_factor
        self.rect.y = self.y

    def blitme(self):
        """draw the bullet to screen"""
        self.screen.blit(self.image, self.rect)
