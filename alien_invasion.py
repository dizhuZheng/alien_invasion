import pygame
from settings import Settings
from ship import Ship
from pygame.sprite import Group
import game_functions as gf
from alien import Alien

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
        alien = Alien(ai_settings, screen)

        #start the main loop for the game
        while True:
                #watch for keyboard and mouse events.
                gf.check_events(ai_settings, screen, ship, bullets)
                ship.update()
                gf.update_bullets(bullets)
                #redraw the screen
                gf.update_screen(ai_settings, screen, ship, alien, bullets)

run_game()
