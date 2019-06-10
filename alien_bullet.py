import pygame
from pygame.sprite import Sprite

class AlienBullet(Sprite):
    """A class to manage bullets fired from the ship"""

    def __init__(self, ai_settings, screen, alien):
        """Create a bullet at the ship's current position"""
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        #create a bullet rect at(0,0) and then set correct position
        self.rect = pygame.Rect(0, 0, ai_settings.alien_bullet_width, ai_settings.alien_bullet_height)
        self.rect.centerx = alien.rect.centerx
        self.rect.bottom = alien.rect.bottom
        #store the bullet's position as a decimal value.
        self.y = float(self.rect.y)
        #alien bullet image
        self.alien_bullet_color = ai_settings.alien_bullet_color
        self.alien_bullet_speed_factor = ai_settings.alien_bullet_speed_factor

    def update(self):
        """move the bullet up the screen"""
        #update the decimal position of the bullet
        self.y += self.alien_bullet_speed_factor
        #update the rect position
        self.rect.y = self.y

    def draw_alien_bullet(self):
        """draw the bullet to screen"""
        pygame.draw.rect(self.screen, self.alien_bullet_color, self.rect, 5)
