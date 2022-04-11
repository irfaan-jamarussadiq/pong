import pygame, sys
from game import Game

WIDTH = 750
HEIGHT = 500
FRAME_RATE = 60
PADDLE_DISPLACEMENT = 5

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Pong')
clock = pygame.time.Clock()
pong_game = Game(WIDTH, HEIGHT)

while True:   
    for event in pygame.event.get():             
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        pong_game.player.paddle.move_up(PADDLE_DISPLACEMENT, screen)
    elif keys[pygame.K_d]:
        pong_game.player.paddle.move_down(PADDLE_DISPLACEMENT, screen)  
    elif keys[pygame.K_p]:
        pong_game.opponent.paddle.move_up(PADDLE_DISPLACEMENT, screen)
    elif keys[pygame.K_l]:
        pong_game.opponent.paddle.move_down(PADDLE_DISPLACEMENT, screen) 
    
    pong_game.draw(screen)
    pygame.display.update()
    clock.tick(FRAME_RATE)