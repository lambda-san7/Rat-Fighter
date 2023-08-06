##############################
# IMPORTS
##############################

import pygame
import os 

##############################
# DEFAULT STUFF
##############################

pygame.init()

running = True

##############################
# WINDOW
##############################

def create_window(w=900,h=600,title="Blank",favicon="favicon.png"):
    window = pygame.display.set_mode((w,h),pygame.RESIZABLE)
    pygame.display.set_caption(title)
    #pygame.display.set_icon(favicon)
    return window

window = create_window(title="Rat Rumble")

##############################
# TIME
##############################

clock = pygame.time.Clock()

fps = 60

deltaTime = clock.tick(fps)/1000

##############################
# CAMERA                   
##############################

class camera:
    x = 0
    y = 0
    scale = 1

##############################
# FILES
##############################

dir_path = os.path.dirname(os.path.realpath(__file__))