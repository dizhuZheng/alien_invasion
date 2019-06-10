import sys
import pygame
from bullet import Bullet
from alien_bullet import AlienBullet
from alien import Alien
from random import randint
from time import sleep

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """respond to keypresses"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()

def fire_bullet(ai_settings, screen, ship, bullets):
    """fire a bullet if limit not reached yet"""
    if len(bullets) < ai_settings.bullets_allowed:
            new_bullet = Bullet(ai_settings, screen, ship)
            bullets.add(new_bullet)

def check_keyup_events(event, ship):
    """respond to key releases"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ai_settings, screen, ship, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(ai_settings, screen, ship, aliens, bullets, alien_bullets):
    """update images on the screen each pass through the loop"""
    screen.fill(ai_settings.bg_color)

    #redraw all bulltes behind ship and aliens
    for bullet in bullets.sprites():
            bullet.draw_bullet()

    for alien_bullet in alien_bullets.sprites():
        alien_bullet.draw_alien_bullet()

    ship.blitme()
    aliens.draw(screen)
    #make the most recently drawn screen visible.
    pygame.display.flip()


def update_alien_bullets(alien_bullets):
    """update position of bullets and get rid of old bullets"""
    #update bullet position
    alien_bullets.update()


def update_bullets(ai_settings, screen, ship, aliens, bullets):
    """update position of bullets and get rid of old bullets"""
    #update bullet position
    bullets.update()
    #check any collision, if so, get rid of the alien and ufo
    check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets)

    if len(aliens) == 0:
        bullets.empty()
        create_fleet(ai_settings, screen, ship, aliens)

    #get rid of bullets that have disappeared
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


def check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets):
      collisions = pygame.sprite.groupcollide(bullets, aliens, False, True)


def create_fleet(ai_settings, screen, ship, aliens):
    """create a full fleet of aliens"""
    #create an alien and find the number of aliens in a row.
    alien = Alien(ai_settings, screen, 1)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.y)
    #create the first row of aliens
    for j in range(number_rows):
        for i in range(number_aliens_x):
                create_alien(ai_settings, screen, aliens, i, j)


def get_number_aliens_x(ai_settings, alien_width):
    """determine the number of aliens taht fit in a row"""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """create an alien and place it in the row"""
    alien = Alien(ai_settings, screen, 1)
    alien_width = alien.rect.width
    alien_height = alien.rect.height
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.y = alien_height + 2 * alien_height * row_number
    alien.rect.x = alien.x
    alien.rect.y = alien.y
    aliens.add(alien)


def get_number_rows(ai_settings, ship_height, alien_height):
    """determine the number of rows of aliens that fit on the screen"""
    available_space_y = (ai_settings.screen_height - (2 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def check_fleet_edges(ai_settings, aliens):
    """respond appropriately if any aliens have reached an edge"""
    for alien in aliens.sprites():
        if alien.check_edges():
            alien.rect.y += ai_settings.single_drop_speed
            alien.direction *= -1


def update_aliens(ai_settings, stats, screen, ship, aliens, bullets):
    """check if the fleet is at an edge, and then update the position of all aliens"""
    check_fleet_edges(ai_settings, aliens)
    aliens.update()
    #look for alien-ship collisions, ship is a sprite, aliens is a group, this method looks for any member of the
    #group that collided with the ship and stops looping through the group
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, ship, aliens, bullets)

    check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets)


def ship_hit(ai_settings, stats, screen, ship, aliens, bullets):
    """respond to ship being hit by alien"""
    if stats.ships_left > 0:
        stats.ships_left -= 1
        sleep(1)

        #empty the aliens ans bullets
        aliens.empty()
        bullets.empty()

        #create a new fleet and ship
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

        #pause
        sleep(0.5)
    else:
        stats.game_active = False


def check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets):
    """check if any alien hit the bottm"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien in aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
                break
