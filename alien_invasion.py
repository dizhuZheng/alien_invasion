import pygame
from settings import Settings
from ship import Ship
from pygame.sprite import Group
import game_functions as gf
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
from bonus import Bonus

def run_game():
    #initialize the game and create a screen obj
    pygame.init()

    ai_settings = Settings()

    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))

    pygame.display.set_caption('Alien Invasion')

    #make a ship
    ship = Ship(ai_settings, screen)

    COUNT = pygame.USEREVENT + 1

    pygame.time.set_timer(COUNT, 5000)

    # Make many bullets
    bullets = Group()

    #make an alien
    aliens = Group()

    bonus = Group()

    #create the fleet of aliens
    gf.create_fleet(ai_settings, screen, ship, aliens)

    #create an instance to store game stats and a scoreboard.
    stats = GameStats(ai_settings)

    sb = Scoreboard(ai_settings, screen, stats)

    #make a button
    play_button = Button(screen, 'Play', 200, 50, 48)

    #game over button
    over_button = Button(screen, 'Game Over', 200, 50, 48)

    #make a quit button
    q_button = Button(screen, 'quit', 60, 50, 30)

    #make a small play button
    p_button = Button(screen, 'play again', 60, 50, 30)

    #make a clock
    start_ticks = pygame.time.get_ticks()

    #start the main loop for the game
    while True:
        #watch for keyboard and mouse events.
        screen.blit(ai_settings.image, (0, 0))
        # pygame.mixer.init() # for sound
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, COUNT, bonus)
        if stats.game_active:
            seconds = (pygame.time.get_ticks() - start_ticks)/1000
            if seconds > stats.timer or stats.timer == 0:
                stats.game_active = False
            else:
                stats.timer -= 1
            sb.prep_clock()
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            # gf.update_bonus(ai_settings, bonus, stats, sb, ship)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)
        #redraw the screen
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, bonus, play_button, q_button, p_button, over_button)

run_game()
