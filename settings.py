import pygame


class Settings:
    ''' Stores all the game's settings '''

    def __init__(self):
        # Screen settings
        self.screen_width = 1600
        self.screen_height = 900
        self.bg_color = (0, 0, 0)
        self.bg_image = pygame.image.load('images/starfield.png')

        # Ship settings
        self.ship_speed = 30
        self.ship_limit = 3

        # Bullet settings
        self.bullet_speed = 40
        self.bullet_width = 25
        self.bullet_height = 3
        self.bullet_color = (0, 0, 255)

        # Enemy settings
        self.enemy_speed = 18

        # Game speedup multiplier
        self.speedup_scale = 1.1

        # How quickly alien point values increase
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        ''' Initialize settings that change throughout the levels '''
        self.enemy_speed_factor = 1

        # Scoring
        self.enemy_points = 20

    def increase_speed(self):
        ''' Increase enemy speed and point value '''
        self.enemy_speed_factor *= self.speedup_scale
        self.enemy_points = int(self.enemy_points * self.score_scale)
