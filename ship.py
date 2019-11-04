import pygame
from pygame.sprite import Sprite

class Ship(Sprite):

    def __init__(self, ai_settings, screen):
        """Initialize the ship and set its starting position"""
        super().__init__()
        self.screen = screen

        self.ai_settings = ai_settings

        #load the ship image and get its rect.
        self.image = pygame.image.load('images/rocket.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #start each new ship at the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #store a decimal value for ship's centerx and centery
        self.center = float(self.rect.centerx)
        self.vert = float(self.rect.centery)

        #movement flag
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def center_ship(self):
        """center the ship on the screen"""
        self.center = self.screen_rect.centerx
        #centery isn't rect.bottom, should use centerx and centery to locate the surface
        self.vert = self.screen_rect.bottom - self.rect.height/2

    def update(self):
        """update the ship's position based on the movement flag"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor

        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.vert -= self.ai_settings.ship_speed_factor

        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.vert += self.ai_settings.ship_speed_factor

        #update rect obj from self.center
        self.rect.centerx = self.center
        self.rect.centery = self.vert


    def blitme(self):
        """draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)
