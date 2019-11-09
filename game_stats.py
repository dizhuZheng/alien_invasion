class GameStats():
    """Track stats fot alien invasion."""
    def __init__(self, ai_settings):
        """Initialize stats"""
        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_active = False
        self.high_score = 0
        self.timer = 500
        self.pct = 100

    def reset_stats(self):
        """Initialize stats that can change during the game"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
        self.pct = 100
