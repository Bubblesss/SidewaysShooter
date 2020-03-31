# import sys

import pygame

from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from scoreboard import ScoreBoard
from button import Button
from ship import Ship
import game_functions as gf


def run_game():
    # Initialize pygame, settings and create a screen object
    pygame.init()

    sws_settings = Settings()

    screen = pygame.display.set_mode(
        (sws_settings.screen_width, sws_settings.screen_height))
    pygame.display.set_caption('Sideways Shooter')

    # Make the Play button
    play_button = Button(sws_settings, screen, "Play")

    # Create an instance to store game statistics and create a scoreboard
    stats = GameStats(sws_settings)
    sb = ScoreBoard(sws_settings, screen, stats)

    # Make a ship, bullets and an enemy
    ship = Ship(sws_settings, screen)
    bullets = Group()
    enemies = Group()
    gf.create_enemy(sws_settings, screen, ship, enemies)

    # Start the main loop for the game
    while True:
        # Watch for keyboard and mouse events
        gf.check_events(sws_settings, screen, stats, sb,
                        play_button, ship, enemies, bullets)

        if stats.game_active:
            ship.update()
            gf.update_enemies(sws_settings, stats, screen,
                              sb, ship, enemies, bullets)

        gf.update_screen(sws_settings, screen, stats, sb,
                         ship, enemies, bullets, play_button)


run_game()

#     def run_game(self):
#         ''' Start main loop of the game '''
#         while True:
#             self._check_events()

#             if self.stats.game_active:
#                 self.ship.update()
#                 self._update_bullets()
#                 self._update_enemies()

#             self._update_screen()

#     def _update_bullets(self):
#         ''' Update bullet positions and remove old ones '''
#         self.bullets.update()

#         # Get rid of bullets not on the screen
#         for bullet in self.bullets.copy():
#             if bullet.rect.right >= 1600:
#                 self.bullets.remove(bullet)

#         self._check_bullet_enemy_collisions()

#     def _check_bullet_enemy_collisions(self):
#         ''' Respond to bullet-enemy collisions '''
#         # Remove any bullets and enemies that have collided
#         collisions = pygame.sprite.groupcollide(
#             self.bullets, self.enemies, True, True)

#         if not self.enemies:
#             # If no enemies on screen, create a new enemy
#             # self.bullets.empty()
#             self._create_enemy()

#     def _check_enemy_edge(self):
#         ''' Create a new enemy if previous one has left the screen '''
#         if enemy.check_edges():
#             self._create_enemy()

#     def _create_enemy(self):
#         ''' Create the enemies '''
#         # Make an enemy
#         enemy = Enemy(self)
#         self.enemies.add(enemy)

#     def _update_enemies(self):
#         ''' Update the positions of enemies '''
#         self.enemies.update()

#         # Look for enemy-ship collisions
#         if pygame.sprite.spritecollideany(self.ship, self.enemies):
#             self._ship_hit()

#     def _ship_hit(self):
#         ''' Respond to the ship being hit by the enemy '''
#         if self.stats.ships_left > 0:
#             # Decrement ships left
#             self.stats.ships_left -= 1

#             # Get rid of any remaining enemies and bullets
#             self.enemies.empty()
#             self.bullets.empty()

#             # Create a new fleet and center the ship
#             self._create_enemy()
#             self.ship.center_ship()

#             # Pause
#             sleep(0.75)
#         else:
#             self.stats.game_active = False
#             pygame.mouse.set_visible(True)

#     def _check_events(self):
#         ''' Respond to keypresses and mouse events '''
#         mouse_pos = pygame.mouse.get_pos()
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 sys.exit()
#             elif event.type == pygame.MOUSEBUTTONDOWN:
#                 self._check_play_button(mouse_pos)
#             elif event.type == pygame.KEYDOWN:
#                 self._check_keydown_events(event)
#             elif event.type == pygame.KEYUP:
#                 self._check_keyup_events(event)

#     def _check_play_button(self, mouse_pos):
#         ''' Start a new game when the player clicks Play '''
#         button_clicked = self.play_button.rect.collidepoint(mouse_pos)
#         if button_clicked and not self.stats.game_active:
#             # Reset the game statistics
#             self.stats.reset_stats()
#             self.stats.game_active = True
#             # Hide the mouse cursor
#             pygame.mouse.set_visible(False)

#             # Get rid of any remaining enemies and bullets
#             self.enemies.empty()
#             self.bullets.empty()

#             # Create a new enemy and center the ship
#             self._create_enemy()
#             self.ship.center_ship()

#     def _check_keydown_events(self, event):
#         ''' Respond to keypress '''
#         if event.key == pygame.K_RIGHT:
#             self.ship.moving_right = True
#         elif event.key == pygame.K_LEFT:
#             self.ship.moving_left = True
#         elif event.key == pygame.K_UP:
#             self.ship.moving_up = True
#         elif event.key == pygame.K_DOWN:
#             self.ship.moving_down = True
#         elif event.key == pygame.K_q:
#             sys.exit()
#         elif event.key == pygame.K_SPACE or pygame.K_f:
#             self._fire_bullet()
#         elif event.key == pygame.K_p:
#             self._check_play_button()

#     def _check_keyup_events(self, event):
#         ''' Respond to key releases '''
#         if event.key == pygame.K_RIGHT:
#             self.ship.moving_right = False
#         elif event.key == pygame.K_LEFT:
#             self.ship.moving_left = False
#         elif event.key == pygame.K_UP:
#             self.ship.moving_up = False
#         elif event.key == pygame.K_DOWN:
#             self.ship.moving_down = False

#     def _fire_bullet(self):

#         new_bullet = Bullet(self)
#         self.bullets.add(new_bullet)

#     def _update_screen(self):
#         self.screen.fill(self.settings.bg_color)
#         self.screen.blit(self.settings.bg_image.convert(), (0, 0))
#         self.ship.image.convert_alpha()
#         self.ship.blitme()

#         for bullet in self.bullets.sprites():
#             bullet.draw_bullet()
#         self.enemies.draw(self.screen)

#         # Draw the play button if the game is inactive
#         if not self.stats.game_active:
#             self.play_button.draw_button()
#         # pygame.display.update()
#         pygame.display.flip()


# if __name__ == '__main__':
#     ''' Make a game instance and run it '''
#     sws = SideWaysShooter()
#     sws.run_game()
