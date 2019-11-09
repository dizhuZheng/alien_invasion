import random
import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """alien in the fleet"""

    def __init__(self, ai_seetings, screen):
        """Initialize the alien and set its starting position"""
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_seetings
        #load the alien image and set its rect attribute
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
        #start each new alien near the top left of the screen
        self.screen_rect = self.screen.get_rect()
        self.rect.x = random.randrange(-10, self.ai_settings.screen_width)
        self.rect.y = random.randrange(-30, -5)
        self.numberx = random.randrange(-18, 10)
        self.numbery = random.randrange(-18, 10)


    def blitme(self):
        """Draw the alien at its current location """
        self.screen.blit(self.image, self.rect)


    def update(self):
        """move the alien up and right"""
        self.rect.x += self.numberx
        self.rect.y += self.numbery


    def check_edges(self):
        """return true if alien is at the edge of screen"""
        if self.rect.right >= self.screen_rect.right + 30 or self.rect.left <= -30 or self.rect.top <= -30 or self.rect.bottom >= self.screen_rect.bottom + 30:
            self.kill()
            return True
        return False
