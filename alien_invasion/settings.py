import pygame

class Settings():
    '''Класс для хранения настроек игры Alien Invasion.'''

    def __init__(self):
        '''Инициализирует настройки игры.'''
        # Параметры экрана
        self.screen_width = 800
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.bg_image = pygame.image.load('images/background.png')
        self.fullscreen = True
        self.bullet_limit = False
        self.bullets_allowed = 3

        # Настройки корабля
        self.ship_speed = 1.5

        # Параметры снаряда
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 0, 0)

        # Настройки пришельцев
        self.alian_speed = 1.0
        self.fleet_drop_speed = 10
        self.fleet_direction = 1

