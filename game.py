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
                self.opponent.update_score()
                self.restart_round(screen)
            elif self.ball.ball.right >= screen.get_width():
                self.player.update_score()
                self.restart_round(screen)
        else:
            self.stop()
            self.display_winner(screen)

    def get_winner(self):
        if self.player.score >= 11:
            return self.player
        elif self.opponent.score >= 11:
            return self.opponent
        else:
            return None

    def display_play_again(self, screen, x):
        font = pygame.font.Font('freesansbold.ttf', 20)
        loc = (int (screen.get_width() * x), 80)
        rect = pygame.draw.rect(screen, (0, 0, 0), (loc[0] + 30, loc[1] + 50, 100, 50))
        playagain = font.render('Play Again?', False, (255, 255, 255))
        screen.blit(playagain, (int (screen.get_width() * x), 120))

        mouse = pygame.mouse.get_pos()
        mouse_x_in_rect = mouse[0] >= rect.left and mouse[0] <= rect.right
        mouse_y_in_rect = mouse[1] >= rect.top and mouse[1] <= rect.bottom
        if mouse_x_in_rect and mouse_y_in_rect:
            self.restart_game(screen)

    def display_winner(self, screen):
        if self.get_winner().name == self.player.name:
            self.player.display_winner_text(screen, 0.15)
            self.display_play_again(screen, 0.20)
        elif self.get_winner().name == self.opponent.name:
            self.opponent.display_winner_text(screen, 0.6)
            self.display_play_again(screen, 0.75)

    def stop(self):
        self.ball.speed_x = 0
        self.ball.speed_y = 0

    def restart_round(self, screen):
        self.ball.ball.center = (screen.get_width()/2, screen.get_height()/2)
        self.ball.speed_x *= choice((-1, 1))
        self.ball.speed_y *= choice((-1, 1))

    def restart_game(self, screen):
        width = screen.get_width()
        height = screen.get_height();
        pname = self.player.name
        oname = self.opponent.name
        self.__init__(width, height, pname, oname)
        self.restart_round(screen)

    def draw(self, screen):
        screen.fill(background)
        width = screen.get_width()
        pygame.draw.line(screen, line_color, [width/2, 0], [width/2, width], 1)
        self.player.update_score_text(screen, 0.25)
        self.opponent.update_score_text(screen, 0.75)
        self.update(screen)

        self.player.draw_paddle(screen)
        self.opponent.draw_paddle(screen)
        self.ball.draw(screen)