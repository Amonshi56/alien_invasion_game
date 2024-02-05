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
        self.ships_limit = 3

        # Параметры снаряда
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 0, 0)

        # Настройки пришельцев
        self.fleet_drop_speed = 10
        
        # Темп ускорения игры
        self.speedup_scale = 1.1
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        '''Инициализация настроек изменяющихся по ходу игры'''
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alian_speed = 1.0
        self.fleet_direction = 1
        self.alian_points = 50

    def increase_speed(self):
        '''Увеличение настройки скорости.'''
        self.ship_speed *= self.speedup_scale        
        self.bullet_speed *= self.speedup_scale
        self.alian_speed *= self.speedup_scale
        
        self.alian_points = int(self.alian_points * self.score_scale)
