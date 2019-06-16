import pygame.font
from pygame.sprite import Group
from ship import Ship

class Scoreboard():
    """A class to report scoring info"""

    def __init__(self, ai_settings, screen, stats):
        """Initialize scorekeeping attributes."""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        #Font settings for scoring infos
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 28)
        self.font2 = pygame.font.SysFont(None, 88)
        #prepare the initial score image.
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()


    def prep_score(self):
        """Turn the score into a rendered image."""
        rounded_score = int(round(self.stats.score, -1))
        score_str = "{} {:,}".format('Current Score:', rounded_score)
        #creates the image
        self.score_image = self.font.render(score_str, True, self.text_color, self.ai_settings.bg_color)

        #display the score at the top right
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20


    def prep_high_score(self):
        """Turn the high score into a rendered image."""
        high_score = int(round(self.stats.high_score, -1))
        high_score_str = "{} {:,}".format('Highest Score:', high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color,
        self.ai_settings.bg_color)

        #center the high score at the top of the screen
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx + 20
        self.high_score_rect.top = self.score_rect.top


    def show_score(self):
        """Draw score and level to the screen"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)


    def prep_level(self):
        """Turn the level into a rendered image"""
        level_str = "{} {:,}".format('Level:', self.stats.level)
        self.level_image = self.font.render(level_str, True, self.text_color, self.ai_settings.bg_color)

        #position the level below the score
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 20


    def prep_ships(self):
        """show how many ships are left."""
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_settings, self.screen)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)


    def game_over(self):
        self.msg2_image = self.font2.render('Game  Over', True, (0, 128, 0))
        self.msg2_image_rect = self.msg2_image.get_rect()
        self.msg2_image_rect.centerx = self.screen_rect.centerx
        self.msg2_image_rect.centery = self.screen_rect.centery+100
        self.screen.blit(self.msg2_image, self.msg2_image_rect)
