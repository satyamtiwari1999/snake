""" Main console for the game """
import pygame
pygame.init()

# difining our snake unit
snake = pygame.Surface((10, 10))
snake.fill((30, 130, 10))

# designing the pearls


# defining our main screen
screen = pygame.display.set_mode([500, 500])


def head(x, y):
    """ will control the head of the snake """
    screen.blit(snake, (x, y))


# position of head of the snake and how much to move
x, y, change_x, change_y = 0, 0, 5, 0
current = pygame.K_RIGHT  # stores the current direction of the snake


# working with the length of the snake
length = [(0, 0), (5, 0)]
# writing the name of the game
pygame.display.set_caption("Catch The Pearls")

# current status of the game
status = True

""" The main loop of the game starts here """
while status:

    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            status = False  # if false then loop breaks

        # defining the controls
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                status = False
            elif event.key == pygame.K_LEFT and current != pygame.K_RIGHT:
                change_x = -5
                change_y = 0
                current = pygame.K_LEFT
            elif event.key == pygame.K_RIGHT and current != pygame.K_LEFT:
                change_x = 5
                change_y = 0
                current = pygame.K_RIGHT
            elif event.key == pygame.K_UP and current != pygame.K_DOWN:
                change_y = -5
                change_x = 0
                current = pygame.K_UP
            elif event.key == pygame.K_DOWN and current != pygame.K_UP:
                change_y = 5
                change_x = 0
                current = pygame.K_DOWN

    x, y = x + change_x, y + change_y
    # maintaining the length and position of the snake
    length.append((x, y))
    length.pop(0)
    screen.fill((235, 225, 52))
    for i in length:
        head(i[0], i[1])

    # a main command which if not written nothing is seen on the screen
    pygame.display.update()
    pygame.time.Clock().tick(30)
pygame.quit()
