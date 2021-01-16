import pygame
from random import choice
from player import Player
from ball import Ball

background = pygame.Color((20, 20, 20))
line_color = pygame.Color('white')

class Game():
    def __init__(self, width, height, player_name, opp_name):
        self.player = Player(0, height/2, player_name)
        self.opponent = Player(width, height/2, opp_name)
        self.ball = Ball(width/2, height/2)

    def update(self, screen):
        self.ball.move(screen, self.player, self.opponent)

        if self.get_winner() is None:
            if self.ball.ball.left <= 0:
                self.restart_round(screen)
                self.opponent.update_score()
            elif self.ball.ball.right >= screen.get_width():
                self.restart_round(screen)
                self.player.update_score()
        else:
            self.stop()
            self.display_winner(screen)

    def get_winner(self):
        if self.player.score >= 11:
            return self.player.name
        elif self.opponent.score >= 11:
            return self.opponent.name
        else:
            return None

    def display_winner(self, screen):
        if self.get_winner() == self.player.name:
            self.player.display_winner_text(screen, 0.2)
        elif self.get_winner() == self.player.name:
            self.player.display_winner_text(screen, 0.8)

    def stop(self):
        self.ball.speed_x = 0
        self.ball.speed_y = 0

    def restart_round(self, screen):
        self.ball.ball.center = (screen.get_width()/2, screen.get_height()/2)
        self.ball.speed_x *= choice((-1, 1))
        self.ball.speed_y *= choice((-1, 1))

    def draw(self, screen):
        screen.fill(background)
        width = screen.get_width()
        pygame.draw.line(screen, line_color, [width/2, 0], [width/2, width], 1)
        self.player.update_score_text(screen, 0.2)
        self.opponent.update_score_text(screen, 0.8)
        self.update(screen)

        self.ball.draw(screen)
        self.player.draw_paddle(screen)
        self.opponent.draw_paddle(screen)