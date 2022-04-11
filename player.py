import pygame

class Player():
    def __init__(self, x, y, width, height, name):     
        self.paddle = pygame.Rect(max(0, x - width), y - height/2, width, height)
        self.name = name

    def move_up(self, change, screen):     
        if self.paddle.top + change >= 0:
            self.paddle.move_ip(0, -change)

    def move_down(self, change, screen):
        _, height = screen.get_size()
        if self.paddle.bottom + change <= height:
            self.paddle.move_ip(0, change)

    def __eq__(self, other):
        return isinstance(other, Player) and self.name == other.name
