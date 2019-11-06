import random
import pygame
from pygame.sprite import Sprite

class Meteor(Sprite):

    def __init__(self, ai_settings, screen):
        super().__init__()
        self.screen = screen
        self.image = pygame.image.load('images/meteorBrown_med1.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.x = random.randrange(ai_settings.screen_width - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 8)
        self.speedx = random.randrange(-3, 3)


    def update(self, ai_settings):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        # if self.rect.top > ai_settings.screen_height + 10 or self.rect.left < -25 or self.rect.right > ai_settings.screen_width + 20:
        #     self.rect.x = random.randrange(ai_settings.screen_width - self.rect.width)
        #     self.rect.y = random.randrange(-100, -40)
        #     self.speedy = random.randrange(1, 8)
        #     self.speedx = random.randrange(-3, 3)

    def blitme(self):
        """draw the bonus at its current location"""
        self.screen.blit(self.image, self.rect)
