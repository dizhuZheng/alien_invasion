import pygame
from pygame.sprite import Sprite

class Explosion(Sprite):
    """ explosion class """
    def __init__(self, screen, center, size, explosion_anim):
        super().__init__()
        self.screen = screen
        self.frame = 0
        self.size = size
        self.explosion_anim = explosion_anim
        self.image = explosion_anim[self.size][0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 50


    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(self.explosion_anim[self.size]):
                self.kill()
            else:
                center = self.rect.center #local var
                self.image = self.explosion_anim[self.size][self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center


    def blitme(self):
        """draw the bonus at its current location"""
        self.screen.blit(self.image, self.rect)
