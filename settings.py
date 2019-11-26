import pygame

class Settings():
    """A class to store all settings for alien invasion."""

    def __init__(self):
        """Initialize the game's settings"""
        self.screen_width = 1200
        self.screen_height = 800
        self.image = pygame.image.load('images/night.jpg')
        self.alien_image = pygame.image.load('images/alien.bmp')
        self.board_color = (38, 38, 38)
        self.ship_limit = 1
        self.bullets_allowed = 5
        self.alien_number = 5
        self.initialize_dynamic_settings()


    def initialize_dynamic_settings(self):
        """initialize settings that change throughout the game"""
        self.ship_speed_factor = 20
        self.alien_speed_factor = 12
        self.bullet_speed_factor = 16
        #scoring
        self.alien_points = 10
        self.bonus_points = 30


    def increase_level(self, stats):
        """increase level settings."""
        stats.level += 1
        if stats.level == 2:
            self.image = pygame.image.load('images/space.jpg')
            self.alien_image = pygame.image.load('images/ufo.png')
            self.alien_number = 7
        elif stats.level == 3:
            pass
