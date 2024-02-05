
class GameStats():
    '''Отслеживание статистики для игры AI'''

    def __init__(self, ai_game):
        '''Инициализация статистики'''
        self.settings = ai_game.settings
        self.reset_stats()
        self.game_active = False
        self.high_score = 0
        self.level = 1

    def reset_stats(self):
        '''Инициализирует статистику, изменяющуюся в ходе игры'''
        self.ships_left = self.settings.ships_limit
        self.score = 0