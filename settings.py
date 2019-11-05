import pygame
class Settings():
    """A class to store all settings for alien invasion."""

    def __init__(self):
        """Initialize the game's settings"""
        self.screen_width = 1200
        self.screen_height = 800
        self.image = pygame.image.load('images/night.jpg')
        self.board_color = (38, 38, 38)
        #ship settings
        self.ship_limit = 2

#        bullet settings
        self.bullet_width = 4
        self.bullet_height = 5
        self.bullet_color = (255, 102, 102)
        self.bullets_allowed = 5

        #alien settings
        self.single_drop_speed = 55

        #how quickly the game speeds up
        self.speedup_scale = 1.5

        self.score_scale = 1.5

        self.grenade_speed_factor = 3

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """initialize settings that change throughout the game"""
        self.ship_speed_factor = 16
        self.alien_speed_factor = 12
        self.bullet_speed_factor = 16
        #direction of 1 represnets right, -1 represents left
        self.fleet_direction = 1
        #scoring
        self.alien_points = 10
        self.bonus_points = 5


    def increase_speed(self):
        """increase speed settings."""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
