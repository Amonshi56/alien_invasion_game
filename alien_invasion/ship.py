import pygame

class Ship():
    '''Класс для управления кораблем.'''
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        # Загружает изображение коробля и получает прямоугольник
        self.image = pygame.image.load('images/spaceship.png')
        self.rect = self.image.get_rect()
        
        # Каждый новый корабль появляется у нижнего края экрана.
        self.rect.midbottom = self.screen_rect.midbottom

        # Сохранение вещественной координаты центра коробля.
        self.x = float(self.rect.x)

        # Флаг перемещения 
        self.moving_right = False
        self.moving_left = False

    def update(self):
        '''обновляет позицию коробля учитывая флаг'''
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.image = pygame.image.load('images/spaceship_right.png')
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.image = pygame.image.load('images/spaceship_left.png')
            self.x -= self.settings.ship_speed 
        if not self.moving_right and not self.moving_left:
            self.image = pygame.image.load('images/spaceship.png')
        # Обновление атрибута rect на основании self.x
        self.rect.x = self.x           

    def blitme(self):
        '''Рисует корабль  в текущей позиции.'''
        self.screen.blit(self.image, self.rect)    

    def center_ship(self):
        '''Размещает корабль в центре'''
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)    