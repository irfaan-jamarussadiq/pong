import pygame

paddle_width = 10
paddle_height = 80

class Player():
    def __init__(self, x, y, name):     
        adj_x = max(0, x - paddle_width)
        adj_y = y - paddle_height/2

        self.paddle = pygame.Rect(adj_x, adj_y, paddle_width, paddle_height)
        self.speed = 10
        self.score = 0
        self.name = name

    def move_up(self, change, screen):
        _ = screen.get_size()        
        if self.paddle.top + change >= 0:
            self.paddle.move_ip(0, -change)

    def move_down(self, change, screen):
        _, height = screen.get_size()
        if self.paddle.bottom + change <= height:
            self.paddle.move_ip(0, change)

    def __eq__(self, other):
        return isinstance(other, Player) and self.name == other.name
