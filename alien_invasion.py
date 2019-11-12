import pygame
from settings import Settings
from ship import Ship
from pygame.sprite import Group
import game_functions as gf
from os import path
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
import time


def run_game():
    #initialize the game and create a screen obj
    pygame.init()

    ai_settings = Settings()

    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))

    screen_rect = screen.get_rect()

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

    img_dir = path.join(path.dirname(__file__), 'images')
    snd_dir = path.join(path.dirname(__file__), 'sound')

    # sound
    shoot_sound = pygame.mixer.Sound(path.join(snd_dir, 'biu.ogg'))
    star_sound = pygame.mixer.Sound(path.join(snd_dir, 'star.ogg'))
    lose_sound = pygame.mixer.Sound(path.join(snd_dir, 'lose.ogg'))
    exp_sounds = []
    for snd in ['expl3.wav', 'expl6.wav']:
        exp_sounds.append(pygame.mixer.Sound(path.join(snd_dir, snd)))

    pygame.mixer.music.load(path.join(snd_dir, 'tgfcoder-FrozenJam-SeamlessLoop.ogg'))
    pygame.mixer.music.set_volume(0.4)

    meteor_images = []
    meteor_list = ['meteorBrown_big1.png', 'meteorBrown_med1.png',
        'meteorGrey_med1.png', 'meteorBrown_med3.png',
        'meteorBrown_small1.png', 'meteorBrown_small2.png',
        'meteorBrown_tiny1.png']
    for img in meteor_list:
        meteor_images.append(pygame.image.load(path.join(img_dir, img)).convert())

    #make meteors
    meteors = Group()

    #explosions
    explosion_anim = []

    for i in range(9):
        file_name = 'Explosions_kenney/regularExplosion0{}.png'.format(i)
        img = pygame.image.load(path.join(img_dir, file_name)).convert()
        img.set_colorkey((0, 0, 0))
        img = pygame.transform.scale(img, (75, 75))
        explosion_anim.append(img)

    explosions = Group()

    #create the fleet of aliens
    gf.create_fleet(ai_settings, screen, ship, aliens)

    #create an instance to store game stats and a scoreboard.
    stats = GameStats(ai_settings)

    sb = Scoreboard(ai_settings, screen, stats)

    #game over button
    over_button = Button(screen, screen_rect.centerx, screen_rect.centery, 'Game Over', 200, 50, 48)

    #make a quit button
    q_button = Button(screen, screen_rect.centerx - 150, screen_rect.centery + 50, 'Quit', 100, 80, 40)

    #make a small play button
    p_button = Button(screen, screen_rect.centerx + 180, screen_rect.centery + 50, 'Play Again', 200, 180, 40)

    pygame.mixer.music.play(loops=-1)

    #start the main loop for the game
    while True:
        # time.sleep(1)
        #watch for keyboard and mouse events.
        screen.blit(ai_settings.image, (0, 0))
        # pygame.mixer.init() # for sound
        gf.check_events(ai_settings, screen, stats, sb, ship, aliens, bullets, COUNT, bonus, meteors, meteor_images, shoot_sound)
        if stats.game_active:
            if stats.timer == 0:
                stats.game_active = False
            else:
                stats.timer -= 1
            sb.prep_clock()
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets, explosions, explosion_anim, exp_sounds)
            gf.update_bonus(ai_settings, bonus, stats, sb, ship, star_sound)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets, meteors, lose_sound)
            gf.update_meteor(ai_settings, meteors, stats, sb, ship, screen, aliens, bullets, lose_sound)
        #redraw the screen
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, meteors, explosions, bonus, q_button, p_button, over_button)

run_game()
