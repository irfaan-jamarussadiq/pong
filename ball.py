import pygame

class Ball():
    def __init__(self, x, y, speed, size):
        self.hitbox = pygame.Rect(x - size/2, y - size/2, size, size)
        self.speed = speed

    def move(self, screen, player, opponent):
        if self.collided_with_paddle(player) or self.collided_with_paddle(opponent):
            self.speed = (self.speed[0] * -1, self.speed[1])
        if self.hitbox.top <= 0 or self.hitbox.bottom >= screen.get_height():
            self.speed = (self.speed[0], self.speed[1] * -1)

        self.hitbox.move_ip(self.speed[0], self.speed[1])

    def collided_with_paddle(self, player):
        return self.hitbox.colliderect(player.paddle)

    def stop(self):
        self.speed = (0, 0)
