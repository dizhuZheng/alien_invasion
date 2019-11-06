import pygame
from pygame.sprite import Sprite

class Explosion(Sprite):

    def __init__(self, center, size):
        super().__init__()
        self.size = size
        self.image = exlosion_anim[self.size][0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 50
