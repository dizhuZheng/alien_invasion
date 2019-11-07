import random
import pygame
from pygame.sprite import Sprite

class Bonus(Sprite):

    def __init__(self, screen, ai_settings):
        super().__init__()
        self.screen = screen
        self.settings = ai_settings
        self.image = pygame.image.load('images/star_gold.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.x = random.randrange(ai_settings.screen_width - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(8, 16)
        self.speedx = random.randrange(-6, 6)


    def update(self):
        """move the bullet up the screen"""
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > self.settings.screen_height + 10 or self.rect.left < -30 or self.rect.right > self.settings.screen_width + 30:
            self.kill()

    def blitme(self):
        """draw the bonus at its current location"""
        self.screen.blit(self.image, self.rect)
