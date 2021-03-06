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
hero = Hero()

# Game metrics setup
hero_speed = 5.0

# Sound setup


# Main game loop
while True:
    clock.tick(100)
    # Look for messages that the game sends to us
    for event in pygame.event.get():
        # User clicked the [X] to quit.  
        if event.type == pygame.QUIT:
            sys.exit()

    if pygame.key.get_focused():
        keystates = pygame.key.get_pressed()

        # Look for arrow keys
        btn_uparrow = (keystates[K_KP8] or keystates[K_UP])
        btn_downarrow = (keystates[K_KP2] or keystates[K_DOWN])
    
    # Move objects around
    if btn_uparrow:
        # Move player up
        if hero.rect.top > 0 + hero_speed:
            hero.move(0, -hero_speed)

    if btn_downarrow:
        # Move player down
        if (hero.rect.bottom + hero_speed) < 479:
            hero.move(0, hero_speed)

    # Draw the background
    screen.blit(bg, [0,0])

    # Draw the hero
    hero.animate()
    screen.blit(hero.image, hero.rect)

    
    # Draw the scene onto the monitor.
    pygame.display.update()