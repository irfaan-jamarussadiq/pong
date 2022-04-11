import pygame
from random import choice

ball_size = 20

class Ball():
    def __init__(self, x, y):
        adj_x = x - ball_size/2
        adj_y = y - ball_size/2
        self.hitbox = pygame.Rect(adj_x, adj_y, ball_size, ball_size)
        self.speed_x = 5
        self.speed_y = 7

    def move(self, screen, player, opponent):
        if self.collided_with_paddle(player) or self.collided_with_paddle(opponent):
            self.speed_x *= -1
        if self.hitbox.top <= 0 or self.hitbox.bottom >= screen.get_height():
            self.speed_y *= -1

        self.hitbox.move_ip(self.speed_x, self.speed_y)

    def collided_with_paddle(self, player):
        return self.hitbox.colliderect(player.paddle)

    def stop(self):
        self.speed_x = 0
        self.speed_y = 0
        