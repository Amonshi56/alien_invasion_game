import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    '''Класс для управление снарядами, выпущенными кораблем.'''

    def __init__(self, ai_game):
        '''Создаёт объект снарядов в текущей позиции коробля.'''
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color
        self.bullet_sound = pygame.mixer.Sound('sound/bullet.mp3')
        # Создание снаряда в позиции (0, 0) и назначение правильной позиции.
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, 
            self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop
        self.bullet_sound.play()
        # Позиция снаряда хранится в вещественном формате.
        self.y = float(self.rect.y)


    def update(self):
        '''Перемещает снаряд по экрану.'''
        # Обновление позиции снаряда в вещественном формате.
        self.y -= self.settings.bullet_speed
        # Обновление позиции прямоугольника.
        self.rect.y = self.y

    def draw_bullet(self):
        '''Вывод снаряда на экран.''' 
        pygame.draw.rect(self.screen, self.color, self.rect)   
