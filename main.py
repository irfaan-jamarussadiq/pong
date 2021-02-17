import pygame, sys
from game import Game

width = 750
height = 500
frame_rate = 60

pygame.init()

my_game = Game(width, height, 'Player', 'Opponent')

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Pong')
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():        
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                my_game.player.move_up(20)
            elif event.key == pygame.K_DOWN:
                my_game.player.move_down(20)
            elif event.key == pygame.K_a:
                my_game.opponent.move_up(20)
            elif event.key == pygame.K_b:
                my_game.opponent.move_down(20)
    
    my_game.draw(screen)
    pygame.display.update()
    clock.tick(frame_rate)