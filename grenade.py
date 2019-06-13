from bullet import Bullet
import pygame

class Grenade(Bullet):

    def __init__(self, ai_settings, screen, alien):
        super().__init__(ai_settings, screen, alien)
        self.color = (244, 113, 66)
        self.rect = pygame.Rect(0,0,5,4)
        self.speed_factor = ai_settings.grenade_speed_factor
        self.rect.centerx = alien.rect.x
        self.rect.bottom = alien.rect.y

    def update(self):
        """move the bullet down the screen"""
        #update the decimal position of the bullet
        self.y += self.speed_factor
        #update the rect position
        self.rect.y = self.y
