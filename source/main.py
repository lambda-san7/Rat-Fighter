##############################
# IMPORTS
##############################

import pygame
from defaults import window, running, clock, fps, handle_event
from character import michael, bell,lazarus
from map import testing, blank, old_ratt_town

##############################
# MATCH
##############################

class match:
    character = None
    stage = None

match.character = bell
match.stage = blank

##############################
# SCENES
##############################

michael.x = 500

class game:
    def handle():
        keys = handle_event()
        window.fill((50,50,50))
        match.stage.render()
        match.character.handle(keys[0],keys[1],keys[2],old_ratt_town)

scene = game

##############################
# GAME LOOP
############################## 

while running:
    clock.tick(fps)
    scene.handle()
    pygame.display.update()

pygame.quit