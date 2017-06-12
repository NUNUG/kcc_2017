import pygame
from pygame.locals import *
import sys
import random
import math
from sfsprites import *



# Pygame Setup
pygame.init()

# SkyFire setup
screen = pygame.display.set_mode([640, 480])
clock = pygame.time.Clock()

# Graphics setup
bg = pygame.transform.scale(pygame.image.load('assets\\slc-night.jpg'), (640, 480))

# Game metrics setup


# Sound setup


# Main game loop
while True:
    clock.tick(100)
    # Look for messages that the game sends to us
    for event in pygame.event.get():
        # User clicked the [X] to quit.  
        if event.type == pygame.QUIT:
            sys.exit()

            
    # Draw the background
    screen.blit(bg, [0,0])

    
    # Draw the scene onto the monitor.
    pygame.display.update()