##############################
# IMPORTS
##############################

import pygame
import math
from defaults import window, running, clock, fps, dir_path, camera

##############################
# SPRITES
##############################

class sprite:
    def __init__(self,file,name="sprite",w=100,h=100):
        self.name = name
        self.sprite = pygame.transform.scale(pygame.image.load(f"{dir_path}/assets/character/{file}"),(w,h))
    def render(self,x,y):
        window.blit(self.sprite,(x,y))

class sprite_sheet:
    def __init__(self,name):

        ##### IDLE #####

        self.idle_left = [
            sprite(f"{name}/idle_1.gif").sprite,
            sprite(f"{name}/idle_2.gif").sprite,
            sprite(f"{name}/idle_3.gif").sprite,
            sprite(f"{name}/idle_4.gif").sprite,
        ]

        self.idle_right = [
            pygame.transform.flip(self.idle_left[0], True, False),
            pygame.transform.flip(self.idle_left[1], True, False),
            pygame.transform.flip(self.idle_left[2], True, False),
            pygame.transform.flip(self.idle_left[3], True, False),
        ]

        ##### RUNNING #####

        self.run_left = [
            sprite(f"{name}/run_1.gif").sprite,
            sprite(f"{name}/run_2.gif").sprite,
            sprite(f"{name}/run_3.gif").sprite,
            sprite(f"{name}/run_4.gif").sprite,
        ]
        
        self.run_right = [
            pygame.transform.flip(self.run_left[0], True, False),
            pygame.transform.flip(self.run_left[1], True, False),
            pygame.transform.flip(self.run_left[2], True, False),
            pygame.transform.flip(self.run_left[3], True, False),
        ]

        ##### ATTACKING #####
'''
        self.attack_left = [
            sprite(f"{name}/attack_1.gif").sprite,
            sprite(f"{name}/attack_2.gif").sprite,
            sprite(f"{name}/attack_3.gif").sprite,
            sprite(f"{name}/attack_4.gif").sprite,
        ]
        
        self.attack_right = [
            pygame.transform.flip(self.attack_left[0], True, False),
            pygame.transform.flip(self.attack_left[1], True, False),
            pygame.transform.flip(self.attack_left[2], True, False),
            pygame.transform.flip(self.attack_left[3], True, False),
        ]
'''
##############################
# CHARACTER CLASSES
##############################

class character:
    def __init__(self,name):
        self.name = name
        self.sprite_sheet = sprite_sheet(name)
        self.sprite_list = self.sprite_sheet.run_left
        self.sprite = 0
        self.facing = "left"
        self.x = 100
        self.y = 100
    def handle(self):
        self.animate(0.1)
        self.render(self.x,self.y)
    def render(self,x,y):
        window.blit(self.sprite_list[math.floor(self.sprite)],(x - camera.x,y - camera.y))
    def animate(self,animation_rate):
        self.sprite += animation_rate
        if(self.sprite > len(self.sprite_list)):
            self.sprite = 0
    def move(self,amount,direction):
        match direction:
            case "left":
                self.x -= amount
            case "right":
                self.x += amount

michael = character("michael")
bell = character("bell")