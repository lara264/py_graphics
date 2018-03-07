# Imports
import pygame
import math
import random

# Initialize game engine
pygame.init()

# Window
WIDTH = 800
HEIGHT = 600
TITLE = "My Awesome Picture"
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption(TITLE)

# Timer
clock = pygame.time.Clock()
refresh_rate = 1

# Colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ORANGE = (255, 125, 0)

# Game loop
done = False

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    a_color = (r, g, b)
    return a_color

while not done:
    # Event processing (React to key presses, mouse clicks, etc.)
    ''' for now, we'll just check to see if the X is clicked '''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Game logic (Check for collisions, update points, etc.)
    ''' leave this section alone for now '''

    # Drawing code (Describe the picture. It isn't actually drawn yet.)
    LIGHT_BLUE = (68, 227, 255)
    for i in range(0, 200):
        screen.fill(random_color())
    #screen.fill(LIGHT_BLUE)

    #for i in range(200, 400):
        #pygame.draw.line(screen, random_color(), [i, i], [i, i+800], 5)

    start_x1 = 0
    start_y1 = 0
    end_x1 = 1
    end_y1 = 1

    start_x2 = 800
    start_y2 = 0
    end_x2 = 799
    end_y2 = 1

    start_x3 = 400
    start_y3 = 600
    end_x3 = 399
    end_y3 = 599

    start_x4 = 0
    start_y4 = 0
    end_x4 = 1
    end_y4 = 1

    pygame.draw.line(screen, random_color(), [start_x1, start_y1], [end_x1, end_y1], 1)

    pygame.draw.line(screen, random_color(), [start_x2, start_y2], [end_x2, end_y2], 1)

    pygame.draw.line(screen, random_color(), [start_x3, start_y3], [end_x3, end_y3], 1)


    for i in range(0, 100000):

        k = random.randint(1, 3)

        if(k == 1):
            start_x1 = (start_x1+start_x4)/2
            start_y1 = (start_y1+start_y4)/2
            end_x1 = (end_x1+end_x4)/2
            end_y1 = (end_y1+end_y4)/2
            start_x4 = start_x1
            start_y4 = start_y1
            end_x4 = end_x1
            end_y4 = end_y1
        if(k == 2):
            start_x2 = (start_x2 + start_x4) / 2
            start_y2 = (start_y2 + start_y4) / 2
            end_x2 = (end_x2 + end_x4) / 2
            end_y2 = (end_y2 + end_y4) / 2
            start_x4 = start_x2
            start_y4 = start_y2
            end_x4 = end_x2
            end_y4 = end_y2
        if(k == 3):
            start_x3 = (start_x3 + start_x4) / 2
            start_y3 = (start_y3 + start_y4) / 2
            end_x3 = (end_x3 + end_x4) / 2
            end_y3 = (end_y3 + end_y4) / 2
            start_x4 = start_x3
            start_y4 = start_y3
            end_x4 = end_x3
            end_y4 = end_y3

        #pygame.draw.line(screen, random_color(), [start_x1, start_y1], [end_x1, end_y1], 1)
        #pygame.draw.line(screen, random_color(), [start_x2, start_y2], [end_x2, end_y2], 1)
        #pygame.draw.line(screen, random_color(), [start_x3, start_y3], [end_x3, end_y3], 1)
        pygame.draw.line(screen, random_color(), [start_x4, start_y4], [end_x4, end_y4], 1)

    #pygame.draw.rect(screen, RED, [50, 50, 400, 300])
    #pygame.draw.line(screen, GREEN, [300, 40], [100, 500], 5)
    #pygame.draw.ellipse(screen, BLUE, [100, 100, 600, 300])
    #pygame.draw.polygon(screen, BLACK, [[200, 200], [50, 400], [600, 500]], 10)

    ''' angles for arcs are measured in radians (a pre-cal topic) '''
    #pygame.draw.arc(screen, ORANGE, [100, 100, 100, 100], 0, math.pi / 2, 1)
    #pygame.draw.arc(screen, BLACK, [100, 100, 100, 100], 0, math.pi / 2, 50)

    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()

    # Limit refresh rate of game loop
    clock.tick(refresh_rate)

# Close window and quit
pygame.quit()
