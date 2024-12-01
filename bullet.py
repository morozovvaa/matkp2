import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """
    Класс для управления пулями, выпущенными кораблём.

    Этот класс управляет пулями, которые корабль выпустил для уничтожения пришельцев.
    Пули движутся вверх по экрану и исчезают, когда выходят за пределы экрана.
    """

    def __init__(self, ai_settings, screen, ship):
        """
        Инициализирует пулю в текущей позиции корабля.

        :param ai_settings: Объект настроек игры, содержащий параметры пуль (цвет, скорость и т. д.)
        :param screen: Экран, на котором будет отображаться пуля.
        :param ship: Объект корабля, который выпустил пулю. Позиция пули зависит от положения корабля.
        """
        super().__init__()  # Вызов конструктора родительского класса Sprite
        self.screen = screen

        # Создание пули в позиции (0,0) и назначение правильной позиции
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
                                ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx  # Центр пули по горизонтали совпадает с центром корабля
        self.rect.top = ship.rect.top  # Пуля появляется на верхней границе корабля

        # Позиция пули хранится в вещественном формате для более точных вычислений
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color  # Цвет пули
        self.speed_factor = ai_settings.bullet_speed_factor  # Скорость движения пули

    def update(self):
        """
        Перемещает пулю вверх по экрану.

        Позиция пули обновляется каждый кадр в зависимости от её скорости. Пуля двигается
        вверх экрана, и её прямоугольник (rect) также обновляется.
        """
        self.y -= self.speed_factor  # Обновление позиции пули в вещественном формате (движется вверх)
        self.rect.y = self.y  # Обновление прямоугольника для отображения пули на экране

    def draw_bullet(self):
        """
        Отображает пулю на экране.

        Рисует пулю с заданным цветом на экране в текущей позиции, используя её прямоугольник.
        """
        pygame.draw.rect(self.screen, self.color, self.rect)  # Рисует прямоугольник пули