##############################
# IMPORTS
##############################

import pygame
from defaults import window, running, clock, fps
import keys

##############################
# SCENES
##############################

class main_menu:
    def handle():
        window.fill((255,255,255))



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
        if i.type == pygame.KEYDOWN:
            keys.down = i.key
        if i.type == pygame.KEYUP:
            keys.up = i.key
    keys.held = pygame.key.get_pressed()
    pygame.display.update()

pygame.quit