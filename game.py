import pygame
from random import choice
from player import Player
from ball import Ball

BACKGROUND_COLOR = pygame.Color((20, 20, 20))
FOREGROUND_COLOR = pygame.Color('white')
BALL_COLOR = pygame.Color('white')
PADDLE_COLOR = pygame.Color('white')
FONT = 'freesansbold.ttf'

class Game():
    BALL_SIZE = 20
    BALL_SPEED = (5, 7)

    def __init__(self, width, height, player_name='Player', opponent_name='Opponent'):
        self.player = Player(0, height/2, player_name)
        self.opponent = Player(width, height/2, opponent_name)
        self.ball = Ball(width/2, height/2, Game.BALL_SPEED, Game.BALL_SIZE)

    def update(self, screen):
        self.ball.move(screen, self.player, self.opponent)
        if self.get_winner():
            self.ball.stop()
            self.display_winner(screen)
        elif self.ball.hitbox.left <= 0:
            self.opponent.score += 1
            self.restart_round(screen)
        elif self.ball.hitbox.right >= screen.get_width():
            self.player.score += 1
            self.restart_round(screen)

    def update_score(self, screen, player):
        font = pygame.font.Font(FONT, 32)
        player_text = font.render(f'{player.score}', False, (255, 255, 255))
        x_pos = screen.get_width() * (0.25 if self.player == player else 0.75)
        screen.blit(player_text, (int(x_pos), 20))

    def get_winner(self):
        if self.player.score >= 11:
            return self.player
        elif self.opponent.score >= 11:
            return self.opponent
        else:
            return None

    def display_winner(self, screen):
        # Display winner name
        winner = self.get_winner()
        font = pygame.font.Font(FONT, 24)
        player_text = font.render(f'{winner.name} wins!', False, (255, 255, 255))
        x_pos = screen.get_width() * (0.15 if winner == self.player else 0.60)
        screen.blit(player_text, (int(x_pos), 80))

        # Display "Play again?" text
        x_pos = screen.get_width() * (0.20 if winner == self.player else 0.75)
        location = (int(x_pos), 80)
        play_again_text = font.render('Play Again?', False, (255, 255, 255))
        screen.blit(play_again_text, (location[0], 120))

        # TODO: Replace this with button press.
        # mouse = pygame.mouse.get_pos()
        # mouse_x_in_rect = mouse[0] >= rect.left and mouse[0] <= rect.right
        # mouse_y_in_rect = mouse[1] >= rect.top and mouse[1] <= rect.bottom
        # if mouse_x_in_rect and mouse_y_in_rect:
        #     self.restart_game(screen)

    def restart_round(self, screen):
        self.ball.hitbox.center = (screen.get_width()/2, screen.get_height()/2)
        self.ball.speed = (self.ball.speed[0] * choice((-1, 1)), self.ball.speed[1] * choice((-1, 1)))

    def restart_game(self, screen):
        width = screen.get_width()
        height = screen.get_height()
        self.__init__(width, height, self.player.name, self.opponent.name)
        self.restart_round(screen)

    def draw(self, screen):
        screen.fill(BACKGROUND_COLOR)
        width = screen.get_width()
        pygame.draw.line(screen, FOREGROUND_COLOR, [width/2, 0], [width/2, width], 1)
        self.update_score(screen, self.player)
        self.update_score(screen, self.opponent)
        self.update(screen)

        pygame.draw.rect(screen, PADDLE_COLOR, self.player.paddle)
        pygame.draw.rect(screen, PADDLE_COLOR, self.opponent.paddle)
        pygame.draw.ellipse(screen, BALL_COLOR, self.ball.hitbox)