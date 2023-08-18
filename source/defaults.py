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

def create_window(w=0,h=0,title="Blank",favicon="favicon.png"):
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

##############################
# EVENT C.R.A.P (Call, Responds (with), Action, Parameters)
##############################

def handle_event():
    key_down = None
    key_up = None
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
        if i.type == pygame.KEYDOWN:
            try:
                key_down = i.unicode
            except:
                key_down = i.key
        if i.type == pygame.KEYUP:
            try:
                key_up = i.unicode
            except:
                key_up = i.key
    return [pygame.key.get_pressed(),key_down,key_up]
    
##############################
# DISTANCE
##############################

def distance(x1,y1,x2,y2):
    #return (x2 - x1)**2 + (y2 - y1)**2
    return [
        (x2 + x1)/2,
        (y2 + y1)/2
    ]
