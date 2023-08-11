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
    def __init__(self,file,name="sprite",w=50,h=50):
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
# SPRITE ASSETS
##############################

shadow = sprite("shadow.gif",w=50,h=12).sprite

##############################
# CHARACTER CLASSES
##############################

class character_shadow:
    def __init__(self):
        self.sprite = shadow
        self.x = 0
        self.y = 0
    def render(self,):
        window.blit(self.sprite,(self.x - camera.x,self.y - camera.y))

class character:
    def __init__(self,name,w=50,h=50):
        self.name = name
        self.w = w
        self.h = h
        self.sprite_sheet = sprite_sheet(name)
        self.sprite_list = self.sprite_sheet.idle_left
        self.sprite = 0
        self.facing = "left"
        self.speed = 10
        self.x = 100
        self.y = 100
        self.horizontal_velocity = 0
        self.vertical_velocity = 0
        self.terminal_velocity = 5
        self.shadow = character_shadow()

    # Well hello there future me! it's Past You please work on gravity and the collision method today,
    # also make michael's flipped sprites (right now his arm is wrong) thanks!

    ##############################
    # CHARACTER >> HANDLE
    ##############################

    def handle(self,key_held,key_down,key_up):
        self.sprite_list = eval(f"self.sprite_sheet.idle_{self.facing}")
        self.controller(key_held,key_down,key_up)
        self.physics()
        self.animate(0.2)
        self.render(self.x,self.y)

    ##############################
    # CHARACTER >> RENDER
    ##############################

    def render(self,x,y):
        #self.shadow.render()
        window.blit(self.sprite_list[math.floor(self.sprite)],(x - camera.x,y - camera.y))
        
    ##############################
    # CHARACTER >> ANIMATE
    ##############################

    def animate(self,animation_rate):
        self.sprite += animation_rate
        if(self.sprite > len(self.sprite_list)):
            self.sprite = 0

    ##############################
    # CHARACTER >> PHYSICS
    ##############################

    def physics(self):
        ##############################
        # CHARACTER >> PHYSICS >> HORIZONTAL
        ##############################

        if self.horizontal_velocity < 0:
            self.horizontal_velocity += 1
        if self.horizontal_velocity > 0:
            self.horizontal_velocity -= 1
        self.x -= self.horizontal_velocity
        
        ##############################
        # CHARACTER >> PHYSICS >> VERTICAL
        ##############################

        self.y -= self.vertical_velocity
        if self.y >= 500:
            self.vertical_velocity = 0
            return
        if self.vertical_velocity >= self.terminal_velocity: # check to see if velocity is max
            self.vertical_velocity = self.terminal_velocity
        self.vertical_velocity -= 1


                
    ##############################
    # CHARACTER >> CONTROLLER
    ##############################

    def controller(self,key_held,key_down,key_up):

        ##############################
        # CHARACTER >> CONTROLLER >> W
        ##############################

        if key_held[pygame.K_w]:
            print(f"w {self.vertical_velocity}")
            self.vertical_velocity += 5

        ##############################
        # CHARACTER >> CONTROLLER >> A
        ##############################

        if key_held[pygame.K_a]:
            self.horizontal_velocity = self.speed
            self.facing = "left"
            self.sprite_list = self.sprite_sheet.run_left

        ##############################
        # CHARACTER >> CONTROLLER >> S
        ##############################

        if key_held[pygame.K_s]:
            pass

        ##############################
        # CHARACTER >> CONTROLLER >> D
        ##############################

        if key_held[pygame.K_d]:
            self.horizontal_velocity = -self.speed
            self.facing = "right"
            self.sprite_list = self.sprite_sheet.run_right

michael = character("michael")
bell = character("bell")