import pygame
from settings import Settings
from ship import Ship
from pygame.sprite import Group
import game_functions as gf
from game_stats import GameStats

def run_game():
        #initialize the game and create a screen obj
        pygame.init()
        ai_settings = Settings()
        screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
        pygame.display.set_caption('Alien Invasion')

        #make a ship
        ship = Ship(ai_settings, screen)

        # Make many bullets
        bullets = Group()

        #make an alien
        aliens = Group()

        #create the fleet of aliens
        gf.create_fleet(ai_settings, screen, ship, aliens)

        #create an instance to store game stats
        stats = GameStats(ai_settings)

        #start the main loop for the game
        while True:
                #watch for keyboard and mouse events.
                gf.check_events(ai_settings, screen, ship, bullets)
                if stats.game_active:
                        ship.update()
                        gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
                        gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
                #redraw the screen
                gf.update_screen(ai_settings, screen, ship, aliens, bullets)

run_game()
