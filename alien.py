import math
import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """alien in the fleet"""

    def __init__(self, ai_seetings, screen, direction):
        """Initialize the alien and set its starting position"""
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_seetings
        self.direction = direction
        #load the alien image and set its rect attribute
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
        #start each new alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #store the alien's exact position
        self.x = float(self.rect.x)
        # self.y = float(self.rect.y)

    def blitme(self):
        """Draw the alien at its current location """
        self.screen.blit(self.image, self.rect)


    def update(self):
        """move the alien up and right"""
        self.x += self.ai_settings.alien_speed_factor * self.direction
        # self.y += math.sin(math.pi/6) * self.x
        self.rect.x = self.x
        # self.rect.y = self.y


    def check_edges(self):
        """return true if alien is at the edge of screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right > screen_rect.right or self.rect.left <= 0 :
            return True
