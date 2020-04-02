""" Main console for the game """
from pygame.locals import (
    K_DOWN,
    K_UP,
    K_RIGHT,
    K_LEFT,
    KEYDOWN
)
import pygame
pygame.init()


screen = pygame.display.set_mode([500, 500])
pygame.display.set_caption("Catch The Pearls")
status = True

""" The main loop of the game starts here """
while status:

    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            status = False
    screen.fill((235, 225, 52))

    snake = pygame.Surface((20, 10))
    snake.fill((30, 130, 10))

    screen.blit(snake, (0, 0))
    # a main command which if not written nothing is seen on the screen
    pygame.display.flip()
pygame.quit()
