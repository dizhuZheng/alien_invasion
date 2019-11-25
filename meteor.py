import random
import pygame
from bonus import Bonus

class Meteor(Bonus):
    def __init__(self, ai_settings, screen, meteor_images):
        super().__init__(ai_settings, screen)
        self.image_orig = random.choice(meteor_images)
        self.image_orig.set_colorkey((0, 0, 0))
        self.image = self.image_orig.copy()
        self.radius = int(self.rect.width * .85 / 2)
        self.speedy = random.randrange(12, 18)
        self.speedx = random.randrange(-8, 8)
        self.rot = 0
        self.rot_speed = random.randrange(-20, 20)
        self.last_update = pygame.time.get_ticks()

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > 40:
            self.last_update = now
            self.rot = (self.rot + self.rot_speed) % 360
            new_image = pygame.transform.rotate(self.image_orig, self.rot)
            old_center = self.rect.center
            self.image = new_image
            self.rect = self.image.get_rect()
            self.rect.center = old_center
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.bottom >= self.settings.screen_height + 20 or self.rect.left <= -20 or self.rect.right >= self.settings.screen_width + 20:
            self.kill()
