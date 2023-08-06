##############################
# IMPORTS
##############################

import pygame
from defaults import window, running, clock, fps
from character import michael, bell

##############################
# SCENES
##############################

class main_menu:
    def handle():
        window.fill((255,255,255))
        michael.handle()
        bell.x = 200
        bell.handle()

scene = main_menu

##############################
# GAME LOOP
##############################

while running:
    clock.tick(fps)
    scene.handle()
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            running = False
    pygame.display.update()

pygame.quit