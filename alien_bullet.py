import pygame
from bullet import Bullet

class AlienBullet(Bullet):
    """A class to manage bullets fired from the alien"""

    def __init__(self, ai_settings, screen, alien):
        """Create a bullet at the ship's current position"""
        super().__init__(ai_settings, screen, alien)
        self.rect.centerx = alien.rect.centerx
        self.rect.bottom = alien.rect.bottom
        self.alien_bullet_color = ai_settings.alien_bullet_color

    def update(self):
        """move the bullet up the screen"""
        #update the decimal position of the bullet
        self.y += self.speed_factor
        #update the rect position
        self.rect.y = self.y

    def draw_bullet(self):
        """draw the bullet to screen"""
        pygame.draw.rect(self.screen, self.alien_bullet_color, self.rect, 5)
