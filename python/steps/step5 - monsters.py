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
fireball = Fireball(hero.rect.left + hero.rect.width - 35, hero.rect.top + 5)
monsters = pygame.sprite.Group()

# Game metrics setup
hero_speed = 5.0
fired = False
fireball_speed = 15.0

monster_speed = 1.0
monsters_per_second = 1.5
monster_frequency = 1000.0 / monsters_per_second
last_monster_time = 0

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
        
        # Look for FIRE button (spacebar)
        btn_space = keystates[K_SPACE]
    
    # Create new monsters if needed
    if (pygame.time.get_ticks() - last_monster_time > monster_frequency):
        amplitude = 20
        monsters.add(Monster( (640, random.randint(0, 300)), [0], create_sinewave_diff(math.trunc(640.0 / 8), amplitude)))
        last_monster_time = pygame.time.get_ticks()
        

    # Move objects around
    if btn_uparrow:
        # Move player up
        if hero.rect.top > 0 + hero_speed:
            hero.move(0, -hero_speed)

    if btn_downarrow:
        # Move player down
        if (hero.rect.bottom + hero_speed) < 479:
            hero.move(0, hero_speed)

    if btn_space and (not fired):
        # Launch a fireball.
        fireball.position = (hero.rect.left + hero.rect.width - 35.0, hero.rect.top + 5.0)
        # TODO: Play a sound
        fired = True

    if fired:
        # Move the fireball
        fireball.move(fireball_speed, 0)
        if fireball.rect.left > 640:
            # Fireball missed.  End it.
            fired = False

    # Move each monster
    for m in monsters:
        m.move(-monster_speed, 0)
    for m in monsters:
        if m.rect.left < -200:
            monsters.remove(m)

    # Draw the background
    screen.blit(bg, [0,0])

    # Draw the hero
    hero.animate()
    screen.blit(hero.image, hero.rect)

    # Draw the fireball
    if fired:
        fireball.animate()
        screen.blit(fireball.image, fireball.rect)

    # Draw the monsters
    for m in monsters:
        screen.blit(m.image, m.rect)    

    # Draw the scene onto the monitor.
    pygame.display.update()