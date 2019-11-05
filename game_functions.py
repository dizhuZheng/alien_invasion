import sys
import pygame
from bullet import Bullet
from alien_bullet import AlienBullet
from alien import Alien
from random import randint
from pygame.sprite import Group
from time import sleep
import math
from bonus import Bonus

def check_keydown_events(event, ai_settings, stats, screen, aliens, sb, ship, bullets):
    """respond to keypresses"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    elif event.key == pygame.K_q:
        sys.exit()
    elif event.key == pygame.K_p:
        stats.reset_stats()
        stats.game_active = True
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()
        sb.prep_clock()
        aliens.empty()
        bullets.empty()
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()


def check_keyup_events(event, ship):
    """respond to key releases"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False


def fire_bullet(ai_settings, screen, ship, bullets):
    """fire a bullet if limit not reached yet"""
    if len(bullets) < ai_settings.bullets_allowed:
            new_bullet = Bullet(ai_settings, screen, ship)
            bullets.add(new_bullet)


def check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, COUNT, bonus):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, stats, screen, aliens, sb, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, bonus, mouse_x, mouse_y)
        elif event.type == COUNT and stats.game_active:
            new_bonus = Bonus(screen, ai_settings)
            bonus.add(new_bonus)


def check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, bonus, mouse_x, mouse_y):
    """start a new game when the player clicks play"""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        pygame.mouse.set_visible(False)
        if play_button.rect.collidepoint(mouse_x, mouse_y):
            ai_settings.initialize_dynamic_settings()
            stats.reset_stats()
            stats.game_active = True
            #reset the scoreboard images.
            sb.prep_score()
            sb.prep_clock()
            sb.prep_high_score()
            sb.prep_level()
            sb.prep_ships()
            #empy the list of aliens and bullets
            aliens.empty()
            bullets.empty()
            bonus.empty()
            #create new fleet and center the ship
            create_fleet(ai_settings, screen, ship, aliens)
            ship.center_ship()


def update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, bonus, play_button, quit_button, p_button, over_button):
    """update images on the screen each pass through the loop"""
    #make the most recently drawn screen visible.
    screen.blit(ai_settings.image, (0,0))

    #redraw all bulltes behind ship and aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    for b in bonus.sprites():
        b.blitme()

    ship.blitme()
    aliens.draw(screen)
    sb.show_score()

    if not stats.game_active:
        if stats.ships_left == 0 or stats.timer == 0:
            over_button.draw_button()
            p_button.draw_button()
            quit_button.draw_button()
        else:
            play_button.draw_button()

    pygame.display.flip()


def check_high_score(stats, sb):
    """check to see if there's a new high score."""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()


def update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """update position of bullets and get rid of old bullets"""
    #update bullet position
    bullets.update()
    #check any collision, if so, get rid of the alien and ufo
    check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets)

    #get rid of bullets that have disappeared
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


def update_bonus(ai_settings, bonus, stats, sb, ship):
    bonus.update(ai_settings)
    check_bonus_ship_collisions(ai_settings, stats, sb, ship, bonus)

    for b in bonus.copy():
        if b.rect.bottom >= ai_settings.screen_height + 20 or b.rect.left <= -20 or b.rect.right >= ai_settings.screen_width + 20:
            bonus.remove(b)


def check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets):
    collisions = pygame.sprite.groupcollide(bullets, aliens, False, True)
    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points * len(aliens)
            sb.prep_score()
        check_high_score(stats, sb)

    if len(aliens) == 0:
        #destroy exisitng bullets, speed up game, create new fleet
        bullets.empty()
        ai_settings.increase_speed()
        #increse level.
        stats.level += 1
        sb.prep_level()
        ship.center_ship()
        create_fleet(ai_settings, screen, ship, aliens)


def check_bonus_ship_collisions(ai_settings, stats, sb, ship, bonus):
    col = pygame.sprite.spritecollide(ship, bonus, True)
    if col:
        for b in col:
            stats.score += ai_settings.bonus_points
            sb.prep_score()
        check_high_score(stats, sb)


def create_fleet(ai_settings, screen, ship, aliens):
    """create a full fleet of aliens"""
    #create an alien and find the number of aliens in a row.
    alien = Alien(ai_settings, screen, 1)
    for j in range(2):
        for i in range(6):
                create_alien(ai_settings, screen, ship, aliens, i, j)


def create_alien(ai_settings, screen, ship, aliens, alien_number, row_number):
    """create an alien and place it in the row"""
    alien = Alien(ai_settings, screen, 1)
    alien_width = alien.rect.width
    alien_height = alien.rect.height
    alien.x = ship.rect.width * 2 + alien_width + 2 * alien_width * alien_number
    alien.y = ship.rect.height + alien_height + 3 * alien_height * row_number
    alien.rect.x = alien.x
    alien.rect.y = alien.y
    aliens.add(alien)


def check_fleet_edges(ai_settings, aliens):
    """respond appropriately if any aliens have reached an edge"""
    for alien in aliens.sprites():
        if alien.check_edges():
            alien.rect.y += ai_settings.single_drop_speed
            alien.direction *= -1


def update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """check if the fleet is at an edge, and then update the position of all aliens"""
    check_fleet_edges(ai_settings, aliens)
    aliens.update()
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets)

    check_aliens_bottom(ai_settings, screen, stats, sb, ship, aliens, bullets)


def ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """respond to ship being hit by alien"""
    if stats.ships_left > 0:
        stats.ships_left -= 1

        #update scoreboard
        sb.prep_ships()

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
        pygame.mouse.set_visible(True)


def check_aliens_bottom(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """check if any alien hit the bottm"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien in aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets)
                break
