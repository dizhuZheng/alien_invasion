class Settings():
    """A class to store all settings for alien invasion."""

    def __init__(self):
        """Initialize the game's settings"""
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (192, 192, 192)

        #ship settings
        self.ship_speed_factor = 7.5
        self.ship_limit = 3

#        bullet settings
        self.bullet_speed_factor = 10
        self.bullet_width = 4
        self.bullet_height = 5
        self.bullet_color = (50, 50, 50)
        self.bullets_allowed = 15

        #alien settings
        self.alien_speed_factor = 3
        self.single_drop_speed = 35
        #direction of 1 represnets right, -1 represents left
        self.fleet_direction = 1
        self.alien_bullet_height = 5
        self.alien_bullet_width = 4
        self.alien_bullet_color = (255, 117, 26)
        self.alien_bullet_speed_factor = 10
