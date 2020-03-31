import pygame

from pygame.sprite import Sprite


class Bullet(Sprite):
    ''' Class to manage ship's bullets '''

    def __init__(self, sws_settings, screen, ship):
        super().__init__()
        self.screen = screen

        #self.bullet_speed = sws_settings.bullet_speed
        self.color = sws_settings.bullet_color

        # Create a bullet rect at 0,0 and then set the correct position
        self.rect = pygame.Rect(
            0, 0, sws_settings.bullet_width, sws_settings.bullet_height)
        self.rect.midright = ship.rect.midright

        # Store the bullets position
        self.x = float(self.rect.x)

    def update(self):
        # Update the decimal position of the bullet
        self.x += sws_settings.bullet_speed
        self.rect.x = self.x

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
