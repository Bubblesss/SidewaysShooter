import pygame
from pygame.sprite import Sprite
import random
import settings


class Enemy(Sprite):
    ''' A class to represent enemy ships '''

    def __init__(self, sws_settings, screen):
        ''' Initiliaze enemies and set their starting positions '''
        super().__init__()
        self.screen = screen
        self.sws_settings = sws_settings

        # Load the enemy images and set their rect attributes
        self.image = pygame.image.load('images/ufo1.png').convert_alpha()
        self.rect = self.image.get_rect()

        # Start each enemy randomly near the far right of the screen
        self.rect.x = random.randint(1550, 1600)
        self.rect.y = random.randint(0, 800)

        # Store the enemy's exact horizontal and vertical position
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def blitme(self):
        """Draw the enemy at its current location."""
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        ''' Return True if enemy is at the edge of screen '''
        screen.rect = self.screen.get_rect()
        if self.rect.left <= 10:
            return True

    def update(self):
        ''' Move the enemy to the left '''
        self.x -= self.sws_settings.enemy_speed
        self.rect.x = self.x
