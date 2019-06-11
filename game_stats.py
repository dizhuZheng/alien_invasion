class GameStats():
    """Track stats fot alien invasion."""

    def __init__(self, ai_settings):
        """Initialize stats"""
        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_active = False

    def reset_stats(self):
        """Initialize stats that can chenge during the game"""
        self.ships_left = self.ai_settings.ship_limit
