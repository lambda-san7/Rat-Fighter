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
    def __init__(self,folder,w=800,h=400):
        self.x = (pygame.display.Info().current_w / 2) - (w / 2)
        self.y = (pygame.display.Info().current_h / 2) + 100
        self.w = w
        self.h = h
        self.platform = sprite(
            f"{folder}/floor.gif",
            w=(w),
            h=(h)
        ).sprite
        #self.prop = sprite(f"{folder}/prop.gif",w=self.w,h=self.h).sprite
        self.back = sprite(
            f"{folder}/back.gif",
            w=(pygame.display.Info().current_w),
            h=(pygame.display.Info().current_h)
        ).sprite
    def render(self):
        window.blit(self.back,(0,0))
        window.blit(self.platform,(self.x - camera.x,self.y - camera.y))

testing = map("testing")
blank = map("blank")
sky_islands = map("Sky Islands")
old_ratt_town = map("Old Ratt Town",h=800)