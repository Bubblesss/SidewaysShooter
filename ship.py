import pygame

from pygame.sprite import Sprite


class Ship(Sprite):
    ''' Class for managing our ship '''

    def __init__(self, sws_settings, screen):
        ''' Initialize the ship and set its starting position '''
        super().__init__()
        self.screen = screen

        # Load the ship image and get its rect
        self.image = pygame.image.load('images/spaceship2.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.sws_settings = sws_settings
        self.screen_rect = screen.get_rect()

        # Set the location for ship at the center left of the screen
        self.rect.midleft = self.screen_rect.midleft

        # Store's decimal value for the ship's horizontal and vertical position
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Movement flag
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        ''' Update the ship's position '''
        # Update the ship's x and y value, not the rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.sws_settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.sws_settings.ship_speed
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.y -= self.sws_settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.sws_settings.ship_speed

        # Update rect object from self.x and self.y
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        ''' Draw the ship at the location specified above '''
        self.screen.blit(self.image.convert_alpha(), self.rect)

    def center_ship(self):
        ''' Center the ship on the left side of the screen '''
        self.rect.midleft = self.screen_rect.midleft

        # self.x = float(self.rect.x)
        # self.y = float(self.rect.y)
