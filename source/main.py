##############################
# IMPORTS
##############################

import pygame
from defaults import window, running, clock, fps, handle_event,cursor
from character import michael, bell, lazarus#, testing_character
from map import testing, blank, sky_islands, old_ratt_town

##############################
# MATCH
##############################

class match:
    character = None
    stage = None

match.character = lazarus

match.stage = old_ratt_town

##############################
# SCENES
##############################

michael.x = 500

class game:
    def handle():
        keys = handle_event()
        window.fill((50,50,50))
        match.stage.render()
        match.character.handle(keys[0],keys[1],keys[2],match.stage)
        #window.blit(cursor,pygame.mouse.get_pos())

scene = game

##############################
# GAME LOOP
############################## 

while running:
    clock.tick(fps)
    scene.handle()
    pygame.display.update()

pygame.quit