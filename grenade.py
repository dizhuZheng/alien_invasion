import pygame
from pygame.sprite import Sprite

class Grenade(Sprite):

    def __init__(self, screen, x, y):
        """Create a bullet at the ship's current position"""
        super().__init__()
        self.screen = screen
        self.image = pygame.Surface((5, 15))
        self.image.fill((165, 252, 3))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.y = float(self.rect.y)
        self.last_update = pygame.time.get_ticks()
        self.speed_factor = 15


    def update(self):
        """move the bullet up the screen"""
        self.y += self.speed_factor
        self.rect.y = self.y


    def blitme(self):
        """draw the bullet to screen"""
        self.screen.blit(self.image, self.rect)
        self.update()


    # def check_grenade_ship_collisions(self, ai_settings, aliens, meteors, lose_sound, bullets, stats, sb, ship, grenades):
    #     hits = pygame.sprite.spritecollide(ship, grenades, True, pygame.sprite.collide_rect_ratio(.5))
    #     if hits:
    #         ship_hit(ai_settings, self.screen, stats, sb, ship, aliens, bullets, meteors, lose_sound)
