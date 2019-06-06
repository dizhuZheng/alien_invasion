class Settings():
    """A class to store all settings for alien invasion."""

    def __init__(self):
        """Initialize the game's settings"""
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (192, 192, 192)
        self.ship_speed_factor = 7.5

#        bullet settings
        self.bullet_speed_factor = 10
        self.bullet_width = 4
        self.bullet_height = 8
        self.bullet_color = (50, 50, 50)
        self.bullets_allowed = 15
