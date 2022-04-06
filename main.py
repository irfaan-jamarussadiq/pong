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
displacement = 5

while True:   
    for event in pygame.event.get():             
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        my_game.player.move_up(displacement, screen)
    elif keys[pygame.K_d]:
        my_game.player.move_down(displacement, screen)  
    elif keys[pygame.K_p]:
        my_game.opponent.move_up(displacement, screen)
    elif keys[pygame.K_l]:
        my_game.opponent.move_down(displacement, screen) 
    
    my_game.draw(screen)
    pygame.display.update()
    clock.tick(frame_rate)