##############################
# IMPORTS
##############################

import pygame
from defaults import window, running, clock, fps, dir_path, camera

##############################
# SPRITE
##############################

class sprite:
    def __init__(self,file,name="sprite",w=50,h=50):
        self.name = name
        self.sprite = pygame.transform.scale(pygame.image.load(f"{dir_path}/assets/map/{file}"),(w,h))
    def render(self,x,y):
        window.blit(self.sprite,(x,y))

##############################
# MAPS AND STAGES
##############################

class map:
    def __init__(self,folder):
        #self.prop_w = prop_w
        #self.prop_h = prop_h
        self.floor = sprite(
            f"{folder}/floor.gif",
            w=(400 + (pygame.display.Info().current_w - 400)),
            h=(100 + (pygame.display.Info().current_h - 600))
        ).sprite
        #self.prop = sprite(f"{folder}/prop.gif",w=self.w,h=self.h).sprite
        self.back = sprite(
            f"{folder}/back.gif",
            w=(400 + (pygame.display.Info().current_w - 400)),
            h=(250 + (pygame.display.Info().current_h - 250))
        ).sprite
    def render(self):
        window.blit(self.back,(0,0))
        window.blit(self.floor,(0,500))

testing = map("testing")
blank = map("blank")
old_ratt_town = map("Old Ratt Town")