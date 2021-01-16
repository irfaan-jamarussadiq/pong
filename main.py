import pygame, sys
from game import Game

width = 750
height = 500
frame_rate = 60

pygame.init()

game = Game(width, height, 'Player', 'Opponent')

screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():        
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                game.player.move_up(20)
            elif event.key == pygame.K_DOWN:
                game.player.move_down(20)
            elif event.key == pygame.K_a:
                game.opponent.move_up(20)
            elif event.key == pygame.K_b:
                game.opponent.move_down(20)
    
    game.draw(screen)
    pygame.display.update()
    clock.tick(frame_rate)