import pygame

class Paddle():
    LENGTH = 80
    WIDTH = 10

    def __init__(self, x, y):     
        x_pos, y_pos = max(0, x - Paddle.WIDTH), y - Paddle.LENGTH/2
        self.hitbox = pygame.Rect(x_pos, y_pos, Paddle.WIDTH, Paddle.LENGTH)

    def move_up(self, change, screen):     
        if self.hitbox.top + change >= 0:
            self.hitbox.move_ip(0, -change)

    def move_down(self, change, screen):
        _, height = screen.get_size()
        if self.hitbox.bottom + change <= height:
            self.hitbox.move_ip(0, change)
