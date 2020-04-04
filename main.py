""" Main console for the game """
import pygame
import random
import time
pygame.init()

name = input("Enter Your Name: ").upper()

# difining our snake unit
snake = pygame.Surface((10, 10))
snake.fill((30, 130, 10))

# defining our main screen
screen = pygame.display.set_mode([500, 500])

# keeping the scores
scores = 0


def print_score():
    """ will print the scores """
    font = pygame.font.SysFont("comicsansms", 30)
    n = font.render(name, True, (0, 0, 0))
    screen.blit(n, (5, 0))
    score = font.render(str(scores), True, (0, 0, 0))
    screen.blit(score, (460, 0))


def head(x, y):
    """controls the head of the snake and print the unit element of snake"""
    screen.blit(snake, (x, y))


# designing the pearl
pearl = pygame.Surface((10, 10))
pearl.fill((51, 68, 245))
a = [0, 0]


def position_pearl(a):
    '''prints the pearl at the random coordinates'''
    if a[0] == 0 and a[1] == 0:
        a[0] = random.choice([x for x in range(10, 480, 10)])
        a[1] = random.choice([x for x in range(10, 480, 10)])
    screen.blit(pearl, (a[0], a[1]))


# obstacles
obs = []


def print_obstacle(obs):
    """ prints the obstacles """
    obst = pygame.Surface((10, 10))
    obst.fill((207, 10, 10))
    for j in obs:
        screen.blit(obst, (j[0], j[1]))


def make_obstacle(obs):
    """ makes obstacles """
    t = random.randint(0, 5)
    for i in range(t):
        x = random.choice([x for x in range(10, 480, 10)])
        y = random.choice([x for x in range(30, 480, 10)])
        if [x, y] != a:
            obs.append((x, y))


# position of head of the snake and how much to move
x, y, change_x, change_y = 0, 0, 10, 0
current = pygame.K_RIGHT  # stores the current direction of the snake


# collision condition
def collision(head, pearl_coordinate, current):
    """ checks if collision has taken place or not """
    if current == pygame.K_LEFT:
        if (head[0] == pearl_coordinate[0] + 10 or head[0] == pearl_coordinate[0]) and head[1] == pearl_coordinate[1]:
            return True
        else:
            return False
    elif current == pygame.K_RIGHT:
        if (head[0] == pearl_coordinate[0] - 10 or head[0] == pearl_coordinate[0]) and head[1] == pearl_coordinate[1]:
            return True
        else:
            return False
    elif current == pygame.K_UP:
        if head[0] == pearl_coordinate[0] and (head[1] == pearl_coordinate[1] + 10 or head[1] == pearl_coordinate[1]):
            return True
        else:
            return False
    elif current == pygame.K_DOWN:
        if head[0] == pearl_coordinate[0] and (head[1] == pearl_coordinate[1] - 10 or head[1] == pearl_coordinate[1]):
            return True
        else:
            return False
    else:
        return False


# working with the length of the snake
length = [(0, 0), (10, 0)]
# writing the name of the game
pygame.display.set_caption("Catch The Pearls")


def highscore():

    pass  # making the start screen of the game


def start():
    s = pygame.image.load('images/mainscreen.png')
    screen.blit(s, (0, 0))
    pygame.display.update()
    time.sleep(2)


# current status of the game
start()


def menu():
    """ main menu of the game """
    while True:
        m = pygame.image.load("images/menu.png")
        screen.blit(m, (0, 0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                position = event.pos
                print(position)
                if position[0] in [x for x in range(20, 488)] and position[1] in [y for y in range(114, 191)]:
                    return True
                elif position[0] in [x for x in range(20, 488)] and position[1] in [y for y in range(282, 360)]:
                    screen.fill((235, 225, 255))
                    font = pygame.font.SysFont("comicsansms", 50)
                    n = font.render(highscore(), True, (0, 0, 0))
                    screen.blit(n, (90, 180))
                    pygame.display.update()
                    time.sleep(1)
            elif event.type == pygame.QUIT:
                pygame.quit()


status = menu()
""" The main loop of the game starts here """
while status:

    screen.fill((235, 225, 255))  # background color
    position_pearl(a)
    print_obstacle(obs)
    print_score()

    # event loop starts
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            status = False  # if false then loop breaks

        # defining the controls
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                status = False
            elif event.key == pygame.K_LEFT and current != pygame.K_RIGHT:
                change_x = -10
                change_y = 0
                current = pygame.K_LEFT
            elif event.key == pygame.K_RIGHT and current != pygame.K_LEFT:
                change_x = 10
                change_y = 0
                current = pygame.K_RIGHT
            elif event.key == pygame.K_UP and current != pygame.K_DOWN:
                change_y = -10
                change_x = 0
                current = pygame.K_UP
            elif event.key == pygame.K_DOWN and current != pygame.K_UP:
                change_y = 10
                change_x = 0
                current = pygame.K_DOWN

    x, y = x + change_x, y + change_y
    # maintaining the length and position of the snake
    length.append((x, y))
    if not collision((x, y), a, current):
        length.pop(0)
        for i in obs:
            if i == (x, y):
                status = False
    else:
        make_obstacle(obs)
        a = [0, 0]
        scores += 1
    # PRINTING THE SNAKE
    for i in length:
        head(i[0], i[1])
    if (x < 10 and current == pygame.K_LEFT) or (x > 480 and current == pygame.K_RIGHT):
        status = False
    elif (y < 10 and current == pygame.K_UP) or (y > 480 and current == pygame.K_DOWN):
        status = False

    # a main command which if not written nothing is seen on the screen
    pygame.display.update()
    pygame.time.Clock().tick(10)
    if not status:
        screen.fill((235, 225, 52))  # background color
        font = pygame.font.SysFont("comicsansms", 60)
        n = font.render(name + ' : ' + str(scores), True, (0, 0, 0))
        screen.blit(n, (70, 130))
        pygame.display.update()
        time.sleep(2)
pygame.quit()
