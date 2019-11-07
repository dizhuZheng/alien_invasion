import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage bullets fired from the ship"""

    def __init__(self, ai_settings, screen, ship):
        """Create a bullet at the ship's current position"""
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        #create a bullet rect at(0,0) and then set correct position
        self.image = pygame.image.load('images/fire05.bmp')
        self.rect = self.image.get_rect()
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        #store the bullet's position as a decimal value.
        self.y = float(self.rect.y)
        self.speed_factor = ai_settings.bullet_speed_factor


    def update(self):
        """move the bullet up the screen"""
        #update the decimal position of the bullet
        self.y -= self.speed_factor
        #update the rect position
        self.rect.y = self.y
        if self.rect.bottom <= 0:
            self.kill()

    def draw_bullet(self):
        """draw the bullet to screen"""
        self.screen.blit(self.image, self.rect)
