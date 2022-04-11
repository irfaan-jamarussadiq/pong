import pygame
from random import choice
from player import Player
from ball import Ball

pygame.font.init()

BACKGROUND_COLOR = pygame.Color((20, 20, 20))
FOREGROUND_COLOR = pygame.Color('white')
BALL_COLOR = pygame.Color('white')
PADDLE_COLOR = pygame.Color('white')
FONT = pygame.font.Font('freesansbold.ttf', 16)
SCORE_FONT = pygame.font.Font('freesansbold.ttf', 24)

class Game():
    BALL_SIZE = 16
    BALL_SPEED = (5, 7)

    def __init__(self, width, height, player_name='Player', opponent_name='Opponent'):
        self.player = Player(0, height/2, player_name)
        self.opponent = Player(width, height/2, opponent_name)
        self.ball = Ball(width/2, height/2, Game.BALL_SPEED, Game.BALL_SIZE)

    def update(self, screen):
        self.ball.move(screen, self.player, self.opponent)
        if self.get_winner():
            self.end_game(screen)
        elif self.ball.hitbox.left <= 0:
            self.opponent.score += 1
            self.restart_round(screen)
        elif self.ball.hitbox.right >= screen.get_width():
            self.player.score += 1
            self.restart_round(screen)

    def update_score(self, screen, player):
        player_text = SCORE_FONT.render(f'{player.score}', False, (255, 255, 255))
        x_pos = screen.get_width() * (0.25 if self.player == player else 0.75)
        screen.blit(player_text, (int(x_pos), 20))

    def get_winner(self):
        if self.player.score >= 1:
            return self.player
        elif self.opponent.score >= 1:
            return self.opponent

    def end_game(self, screen):
        winner = self.get_winner()
        self.ball.stop()
        player_text = FONT.render(f'{winner.name} wins!', False, (255, 255, 255))
        x_pos = screen.get_width() * (0.20 if winner == self.player else 0.60)
        location = (int(x_pos), 80)
        screen.blit(player_text, location)

    def restart_round(self, screen):
        self.ball.hitbox.center = (screen.get_width()/2, screen.get_height()/2)
        self.ball.speed = (self.ball.speed[0] * choice((-1, 1)), self.ball.speed[1] * choice((-1, 1)))

    def draw(self, screen):
        screen.fill(BACKGROUND_COLOR)
        width = screen.get_width()
        pygame.draw.line(screen, FOREGROUND_COLOR, [width/2, 0], [width/2, width], 1)
        self.update_score(screen, self.player)
        self.update_score(screen, self.opponent)
        self.update(screen)

        pygame.draw.rect(screen, PADDLE_COLOR, self.player.paddle.hitbox)
        pygame.draw.rect(screen, PADDLE_COLOR, self.opponent.paddle.hitbox)
        pygame.draw.ellipse(screen, BALL_COLOR, self.ball.hitbox)