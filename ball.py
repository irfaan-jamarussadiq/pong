import pygame
from random import choice

ball_size = 20

# Object
    # data -> fields

class Ball():
    def __init__(self, x, y):
        adj_x = x - ball_size/2
        adj_y = y - ball_size/2
        self.ball = pygame.Rect(adj_x, adj_y, ball_size, ball_size)
        self.speed_x = 2
        self.speed_y = 2

    def move(self, screen, player, opponent):
        if self.collided_with_paddle(player) or self.collided_with_paddle(opponent):
            self.speed_x *= -1
        if self.ball.top <= 0 or self.ball.bottom >= screen.get_height():
            self.speed_y *= -1

        self.ball.move_ip(self.speed_x, self.speed_y)

    def collided_with_paddle(self, player):
        return self.ball.colliderect(player.paddle)

    def draw(self, screen):
        pygame.draw.ellipse(screen, pygame.Color('white'), self.ball)