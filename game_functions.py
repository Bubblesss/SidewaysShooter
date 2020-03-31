import sys
from time import sleep

import pygame
from bullet import Bullet
from enemy import Enemy


def check_play_button(sws_settings, screen, stats, sb, play_button, ship,
                      enemies, bullets, mouse_x, mouse_y):
    ''' Start a new game when player clicks Play '''
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        # Reset the game settings
        sws_settings.initialize_dynamic_settings()

        start_game(sws_settings, screen, stats, sb, ship, enemies, bullets)


def check_events(sws_settings, screen, stats, sb, play_button, ship, enemies,
                 bullets):
    ''' Respond to keypresses and mouse events '''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, sws_settings, screen, stats, sb, ship,
                                 enemies, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(sws_settings, screen, stats, sb, play_button,
                              ship, enemies, bullets, mouse_x, mouse_y)


def check_keydown_events(event, sws_settings, screen, stats, sb, ship, enemies,
                         bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    elif event.key == pygame.K_q:
        sys.exit()
    elif event.key == pygame.K_SPACE:
        fire_bullet(sws_settings, bullets, screen, ship)
    elif event.key == pygame.K_p:
        start_game(sws_settings, screen, stats, sb, ship, enemies, bullets)


def check_keyup_events(event, ship):
    ''' Respond to key releases '''
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False


def fire_bullet(sws_settings, bullets, screen, ship):
    ''' Fires a bullet '''
    new_bullet = Bullet(sws_settings, screen, ship)
    bullets.add(new_bullet)


def update_screen(sws_settings, screen, stats, sb, ship, enemies,
                  bullets, play_button):
    ''' Update images on the screen and flip to the new screen '''
    # Redraw the screen during each pass through the loop
    screen.fill(sws_settings.bg_color)
    screen.blit(sws_settings.bg_image.convert(), (0, 0))
    ship.image.convert_alpha()

    # Redraw all bullets behind ship and enemies
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    enemies.draw(screen)

    # Draw the score information
    sb.show_score()

    # Draw the play button if the game is inactive
    if not stats.game_active:
        play_button.draw_button()

    # Make most recently drawn screen visible
    pygame.display.flip()


def update_bullets(sws_settings, screen, stats, sb, ship, enemies, bullets):
    ''' Update position of bullets and get rid of old ones '''
    # Update bullet positions
    bullets.update()

    # Get rid of old bullets
    for bullet in bullets.copy():
        if bullet.rect.right >= 1600:
            bullets.remove(bullet)
            # print(len(bullets))

    check_bullet_alien_collisions(
        sws_settings, screen, stats, sb, ship, enemies, bullets)


def check_bullet_alien_collisions(sws_settings, screen, stats, sb, ship, enemis, bullets):
    ''' Respond to bullet-enemy collisions '''
    # Remove any bullets and aliens that have collided
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    if collisions:
        for enemies in collisions.values():
            stats.score += sws_settings.enemy_points * len(enemies)
            sb.prep_score()

        check_high_score(stats, sb)

    if len(enemies) == 0:
        start_new_level(sws_settings, enemies, bullets,
                        sb, screen, ship, stats)


# def start_new_level(sws_settings, enemies, bullets, sb, screen, ship, stats):
#     # If the entire fleet is destroyed, start a new level
#     sws_settings.increase_speed()
#     # Increase level
#     stats.level += 1
#     sb.prep_level()
#     create_fleet(sws_settings, screen, ship, enemies)


def create_enemy(sws_settings, screen, ship, enemies):
    # Create an enemy
    enemy = Enemy(sws_settings, screen)
    enemies.add(enemy)


def update_enemies(sws_settings, stats, screen, sb, ship, enemies, bullets):
    enemies.update()

    # Look for enemy-ship collisions
    if pygame.sprite.spritecollideany(ship, enemies):
        ship_hit(sws_settings, stats, screen, sb, ship, enemies, bullets)


def ship_hit(sws_settings, stats, screen, sb, ship, enemies, bullets):
    ''' Respond to ship being hit by alien '''

    # Decrement ships left
    stats.ships_left -= 1

    if stats.ships_left > 0:

        # Update scoreboards
        sb.prep_ships()

        # Empty the list of enemies
        enemies.empty()

        # Create a new enemy and center the ship on the left side
        create_enemy(sws_settings, screen, ship, enemies)
        ship.center_ship()

        # Pause
        sleep(0.75)

    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)


def start_game(sws_settings, screen, stats, sb, ship, enemies, bullets):
    # Hide the mouse cursor
    pygame.mouse.set_visible(False)

    # Reset the game statistics
    stats.reset_stats()
    stats.game_active = True

    # Reset the scoreboard images
    sb.prep_images()

    # Empty the list of enemies
    enemies.empty()

    # Create a new enemy and center the ship on the left side of screen
    create_enemy(sws_settings, screen, ship, enemies)
    ship.center_ship()


def check_high_score(stats, sb):
    ''' Check to see if there is a new high score '''
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()
