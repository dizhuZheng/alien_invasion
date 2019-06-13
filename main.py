import sys
from alien import Alien
from settings import Settings

import pygame

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption('narue game')
    bg_color = (30, 30, 30)
    alien = Alien(ai_settings, screen, 1)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(bg_color)
        alien.blitme()
        pygame.display.flip()

run_game()
