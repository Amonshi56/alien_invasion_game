import pygame
import random

# Инициализация Pygame
pygame.init()

# Создание окна
screen = pygame.display.set_mode((800, 600))

# Координаты и скорость врага
enemy_x = 400
enemy_y = 300
enemy_speed = 0.1

# Маршрут движения врага
route = [(100, 200), (400, 100), (700, 300), (400, 500)]

# Индекс текущей цели в маршруте
target_index = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Проверка достижения текущей цели
    target_x, target_y = route[target_index]
    if enemy_x == target_x and enemy_y == target_y:
        target_index = (target_index + 1) % len(route)
    
    # Вычисление новых координат врага с помощью векторов
    dx = target_x - enemy_x
    dy = target_y - enemy_y
    distance = abs(dx) + abs(dy)
    speed_x = dx / distance * enemy_speed
    speed_y = dy / distance * enemy_speed
    enemy_x += speed_x
    enemy_y += speed_y

    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (255, 0, 0), (int(enemy_x), int(enemy_y)), 20)
    pygame.display.flip()

pygame.quit()
