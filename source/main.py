##############################
# IMPORTS
##############################

import pygame
from defaults import window, running, clock, fps, handle_event
from character import michael, bell

##############################
# PLAYER SHIT
##############################

class player:
    character = None

player.character = bell

##############################
# SCENES
##############################

class game:
    def handle():
        keys = handle_event()
        window.fill((50,50,50))
        player.character.handle(keys[0],keys[1],keys[2])

scene = game

##############################
# GAME LOOP
##############################

while running:
    clock.tick(fps)
    scene.handle()
    pygame.display.update()

pygame.quit