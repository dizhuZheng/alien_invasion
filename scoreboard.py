import pygame.font
import pygame
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
        self.text_color = (255, 255, 26)
        self.font = pygame.font.SysFont(None, 28)
        self.font2 = pygame.font.SysFont(None, 88)

        #prepare the initial score image.
        self.prep_score()
        self.prep_energy()
        self.prep_level()
        self.prep_clock()
        self.prep_ships()


    def prep_score(self):
        """Turn the score into a rendered image."""
        rounded_score = int(round(self.stats.score, -1))
        score_str = "{} {:,}".format('Current Score:', rounded_score)
        #creates the image
        self.score_image = self.font.render(score_str, True, self.text_color, self.ai_settings.board_color)

        #display the score at the top right
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20


    def prep_energy(self):
        """Turn the high score into a rendered image."""
        if self.stats.pct < 0:
            self.stats.pct = 0
        elif self.stats.pct > 100:
            self.stats.pct = 100
        BAR_LENGTH = 100
        BAR_HEIGHT = 10
        fill = (self.stats.pct / 100) * BAR_LENGTH
        outline_rect = pygame.Rect(self.screen_rect.left + 180, self.score_rect.top, BAR_LENGTH, BAR_HEIGHT)
        fill_rect = pygame.Rect(self.screen_rect.left + 180, self.score_rect.top, fill, BAR_HEIGHT)
        pygame.draw.rect(self.screen, (0, 255, 0), fill_rect)
        pygame.draw.rect(self.screen, (255, 255, 255), outline_rect, 2)


    def show_score(self):
        """Draw score and level to the screen"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.screen.blit(self.clock_image, self.clock_rect)
        self.ships.draw(self.screen)


    def prep_level(self):
        """Turn the level into a rendered image"""
        level_str = "{} {:,}".format('Level:', self.stats.level)
        self.level_image = self.font.render(level_str, True, self.text_color, self.ai_settings.board_color)

        #position the level below the score
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 20


    def prep_clock(self):
        """Turn the clock score into a rendered image."""
        clock_str = "{} {:,}".format('Left Time:', self.stats.timer)
        self.clock_image = self.font.render(clock_str, True, self.text_color, self.ai_settings.board_color)

        #position the clock below the level
        self.clock_rect = self.clock_image.get_rect()
        self.clock_rect.right = self.screen_rect.centerx + 180
        self.clock_rect.top = self.score_rect.top


    def prep_ships(self):
        """show how many ships are left."""
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_settings, self.screen)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)
