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

    def move_up(self, change):
        self.paddle.move_ip(0, -change)

    def move_down(self, change):
        self.paddle.move_ip(0, change)
        
    def draw_paddle(self, screen):
        pygame.draw.rect(screen, pygame.Color('white'), self.paddle)

    def update_score(self):
        self.score += 1

    def reset_score(self):
        self.score = 0

    def update_score_text(self, screen, x):
        font = pygame.font.Font('freesansbold.ttf', 32)
        player_text = font.render(f'{self.score}', False, (255, 255, 255))
        screen.blit(player_text, (int (screen.get_width() * x), 20))

    def display_winner_text(self, screen, x):
        font = pygame.font.Font('freesansbold.ttf', 32)
        player_text = font.render(f'{self.name} wins!', False, (255, 255, 255))
        screen.blit(player_text, (int (screen.get_width() * x), 80))