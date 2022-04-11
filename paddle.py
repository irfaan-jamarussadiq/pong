import pygame

class Paddle():
    LENGTH = 80
    WIDTH = 10

    def __init__(self, x, y):     
        x_pos, y_pos = max(0, x - Paddle.LENGTH), y - Paddle.LENGTH/2
        self.paddle = pygame.Rect(x_pos, y_pos, Paddle.WIDTH, Paddle.LENGTH)

    def move_up(self, change, screen):     
        if self.paddle.top + change >= 0:
            self.paddle.move_ip(0, -change)

    def move_down(self, change, screen):
        _, height = screen.get_size()
        if self.paddle.bottom + change <= height:
            self.paddle.move_ip(0, change)
