import random
import pygame
from bonus import Bonus
class Meteor(Bonus):
    def __init__(self, ai_settings, screen):
        super().__init__(ai_settings, screen)
        self.image = pygame.image.load('images/meteorBrown_med1.bmp')
        self.radius = int(self.rect.width * .85 / 2)
        self.speedy = random.randrange(12, 18)
        self.speedx = random.randrange(-8, 8)
