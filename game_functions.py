import random
import sys
import pygame
from bullet import Bullet
from alien import Alien
from pygame.sprite import Group
from time import sleep
import math
from bonus import Bonus
from meteor import Meteor
from explosion import Explosion


def check_keydown_events(event, ai_settings, stats, screen, ship, bullets, shoot_sound):
    """respond to keypresses"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets, shoot_sound)
    elif event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    elif event.key == pygame.K_q:
        sys.exit()
    elif event.key == pygame.K_p:
        stats.game_active = False
        stats.paused = True


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


def fire_bullet(ai_settings, screen, ship, bullets, shoot_sound):
    """fire a bullet if limit not reached yet"""
    now = pygame.time.get_ticks()
    if now - ship.last_shoot > ship.shoot_delay:
        ship.last_shoot = now
        if len(bullets) < ai_settings.bullets_allowed:
            new_bullet = Bullet(ai_settings, screen, ship)
            bullets.add(new_bullet)
            shoot_sound.play()


def check_events(ai_settings, screen, stats, ship, aliens, bullets, COUNT, bonus, meteors, meteor_images, shoot_sound, p_button, quit_button):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, stats, screen, ship, bullets, shoot_sound)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_button(stats, p_button, quit_button, mouse_x, mouse_y)
        elif event.type == COUNT and stats.game_active:
            new_bonus = Bonus(screen, ai_settings)
            bonus.add(new_bonus)
            for i in range(6):
                new_meteor = Meteor(screen, ai_settings, meteor_images)
                meteors.add(new_meteor)


def check_button(stats, p_button, quit_button, mouse_x, mouse_y):
    p_button.draw_button()
    quit_button.draw_button()
    if p_button.rect.collidepoint(mouse_x, mouse_y):
        stats.game_active = True
    elif quit_button.rect.collidepoint(mouse_x, mouse_y):
        sys.exit()


start_ticks = pygame.time.get_ticks()
def update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, meteors, explosions, bonus, quit_button, p_button, over_button, pause_button, li, mouse_x, mouse_y):
    """update images on the screen each pass through the loop"""
    #make the most recently drawn screen visible.
    screen.blit(ai_settings.image, (0, 0))

    screen_rect = screen.get_rect()

    #redraw all bulltes behind ship and aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    for b in bonus.sprites():
        b.blitme()

    for alien in aliens.sprites():
        alien.blitme()

    for meteor in meteors.sprites():
        meteor.blitme()

    for explosion in explosions.sprites():
        explosion.blitme()

    ship.blitme()
    aliens.draw(screen)
    sb.show_score()
    sb.prep_energy()

    if not stats.game_active:
        if stats.ships_left == 0 or stats.timer == 0:
            over_button.draw_button()
        elif stats.paused:
            pause_button.draw_button()
            check_button(stats, p_button, quit_button, mouse_x, mouse_y)
        else:
            seconds = (pygame.time.get_ticks()-start_ticks)/1000
            if seconds <= 1:
                image = li[3]
            elif seconds <= 2:
                image = li[2]
            elif seconds <= 3:
                image = li[1]
            elif seconds <= 4:
                image = li[0]
            elif seconds <= 5:
                image = li[0]
                stats.game_active = True
            screen.blit(image, (screen_rect.centerx - 63, screen_rect.centery-40))
    pygame.display.flip()


def update_bullets(ai_settings, screen, stats, sb, ship, aliens, meteors, bullets, explosions, explosion_anim, exp_sounds):
    """update position of bullets and get rid of old bullets"""
    bullets.update()
    explosions.update()
    check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets, explosions, explosion_anim, exp_sounds)
    check_bullet_meteor_collisions(screen, bullets, meteors, explosions, explosion_anim, exp_sounds)


def update_meteor(ai_settings, meteors, stats, sb, ship, screen, aliens, bullets, lose_sound):
    meteors.update()
    check_meteor_ship_collisions(ai_settings, stats, sb, ship, meteors, screen, aliens, bullets, lose_sound)



def check_meteor_ship_collisions(ai_settings, stats, sb, ship, meteors, screen, aliens, bullets, lose_sound):
    hits = pygame.sprite.spritecollide(ship, meteors, True, pygame.sprite.collide_circle)
    for hit in hits:
        stats.pct -= hit.radius * 2
        if stats.pct <= 0:
            ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets, meteors, lose_sound)


def update_bonus(ai_settings, bonus, stats, sb, ship, star_sound):
    bonus.update()
    check_bonus_ship_collisions(ai_settings, stats, sb, ship, bonus, star_sound)

    for b in bonus.copy():
        if b.rect.bottom >= ai_settings.screen_height + 20 or b.rect.left <= -20 or b.rect.right >= ai_settings.screen_width + 20:
            bonus.remove(b)


def check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets, explosions, explosion_anim, exp_sounds):
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    stats.score += ai_settings.alien_points * len(collisions)
    sb.prep_score()
    for collision in collisions:
        ex = Explosion(screen, collision.rect.center, 'lg', explosion_anim)
        explosions.add(ex)
        ex.blitme()
        for e in exp_sounds:
            e.play()

    if len(aliens) == 0:
        bullets.empty()
        ai_settings.increase_level(stats)
        stats.level += 1
        sb.prep_level()
        ship.center_ship()
        create_fleet(ai_settings, screen, ship, aliens)


def check_bullet_meteor_collisions(screen, bullets, meteors, explosions, explosion_anim, exp_sounds):
    collisions = pygame.sprite.groupcollide(bullets, meteors, True, True)
    for collision in collisions:
        ex = Explosion(screen, collision.rect.center, 'sm', explosion_anim)
        explosions.add(ex)
        ex.blitme()
        for e in exp_sounds:
            e.play()


def check_bonus_ship_collisions(ai_settings, stats, sb, ship, bonus, star_sound):
    hits = pygame.sprite.spritecollide(ship, bonus, True, pygame.sprite.collide_circle)
    if hits:
        stats.score += ai_settings.bonus_points * len(hits)
        stats.pct += len(hits) * 10
        sb.prep_score()
        star_sound.play()


def create_fleet(ai_settings, screen, ship, aliens):
    """create a full fleet of aliens"""
    for j in range(2):
        for i in range(ai_settings.alien_number):
            create_alien(ai_settings, screen, ship, aliens, i, j)


def create_alien(ai_settings, screen, ship, aliens, alien_number, row_number):
    """create an alien and place it in the row"""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien_height = alien.rect.height
    alien.x = ship.rect.width * 2 + alien_width + 2 * alien_width * alien_number
    alien.y = ship.rect.height + alien_height + 3 * alien_height * row_number
    alien.rect.x = alien.x
    alien.rect.y = alien.y
    aliens.add(alien)


def check_fleet_edges(ai_settings, screen, aliens):
    """respond appropriately if any aliens have reached an edge"""
    for alien in aliens.sprites():
        if alien.check_edges():
            alien = Alien(ai_settings, screen)
            aliens.add(alien)


def update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets, meteors, lose_sound):
    """check if the fleet is at an edge, and then update the position of all aliens"""
    check_fleet_edges(ai_settings, screen, aliens)
    aliens.update()
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets, meteors, lose_sound)


def ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets, meteors, lose_sound):
    """respond to ship being hit by alien"""
    lose_sound.play()
    if stats.ships_left > 0:
        stats.ships_left -= 1
        sb.prep_ships()
        #empty the aliens ans bullets
        aliens.empty()
        bullets.empty()
        meteors.empty()
        #create a new fleet and ship
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

        #pause
        sleep(0.5)

    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)
