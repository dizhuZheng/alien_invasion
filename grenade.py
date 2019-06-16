from bullet import Bullet
import pygame

class Grenade(Bullet):

    def __init__(self, ai_settings, screen, alien):
        super().__init__(ai_settings, screen, alien)
        self.rect = pygame.Rect(0, 0, 5, 5)
        self.rect.center = alien.centerx, alien.centery
        self.speed_factor = ai_settings.grenade_speed_factor
        self.color = (244, 140, 66)

    def update(self):
        """move the bullet down the screen"""
        #update the decimal position of the bullet
        self.y += self.speed_factor
        #update the rect position
        self.rect.y = self.y

    def draw(self):
        """draw the grenade to the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect, 5)
