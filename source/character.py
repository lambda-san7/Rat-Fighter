##############################
# IMPORTS
##############################

import pygame
import math
from defaults import window, running, clock, fps, dir_path, camera

##############################
# COLLISIONS
##############################

class collisions:
    def __init__(self):
        self.grounded = False
        self.air = False
        self.climbing = False
    def get(self,object,map,collidables=[]):
        if self.y < map.y - object.h: # on ground
            self.grounded = True
            

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

        ##############################
        # IDLE
        ##############################

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

        ##############################
        # RUN
        ##############################

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

        ##############################
        # FALLING
        ##############################

        self.falling_left = [
            sprite(f"{name}/run_3.gif").sprite,
            sprite(f"{name}/run_3.gif").sprite,
            sprite(f"{name}/run_3.gif").sprite,
            sprite(f"{name}/run_3.gif").sprite,
        ]
        
        self.falling_right = [
            pygame.transform.flip(self.falling_left[0], True, False),
            pygame.transform.flip(self.falling_left[1], True, False),
            pygame.transform.flip(self.falling_left[2], True, False),
            pygame.transform.flip(self.falling_left[3], True, False),
        ]


        ##############################
        # SPRITE ASSETS
        ##############################
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

shadow = sprite("shadow.gif",w=100,h=24).sprite

##############################
# CHARACTER CLASSES
##############################

class character_shadow:
    def __init__(self):
        self.sprite = shadow
        self.x = 0
        self.y = 0
    def render(self,x,y):
        window.blit(self.sprite,(x - camera.x,y - camera.y))
        #window.blit(self.sprite,(self.x - camera.x,self.y - camera.y))

class character:
    def __init__(self,name,w=100,h=100,speed=18,jump=18,jump_count=1):
        self.name = name
        self.w = w
        self.h = h
        self.sprite_sheet = sprite_sheet(name)
        self.sprite_list = self.sprite_sheet.idle_left
        self.sprite = 0
        self.facing = "left"
        self.curr_speed = 0
        self.speed = speed
        self.air_speed = speed + 5
        self.jump = jump
        self.jumps = jump_count
        self.curr_jumps = jump_count
        self.x = 100
        self.y = 100
        self.horizontal_velocity = 0
        self.vertical_velocity = 0
        self.terminal_velocity = 50
        self.shadow = character_shadow()
        self.control = False
        self.stun = 0
        self.collisions = collisions()

    ##############################
    # CHARACTER >> HANDLE
    ##############################

    def handle(self,key_held,key_down,key_up,map):
        #self.collisions.get()
        self.sprite_list = eval(f"self.sprite_sheet.idle_{self.facing}")
        self.controller(key_held,key_down,key_up)
        self.physics(map)
        self.animate(0.2)
        self.render(self.x,self.y)

    ##############################
    # CHARACTER >> RENDER
    ##############################

    def render(self,x,y):
        self.shadow.render(
            self.x,
            500 + 5
        )
        window.blit(self.sprite_list[math.floor(self.sprite)],(x - camera.x,(y + 15) - camera.y))
        
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

    def physics(self,map):

        ##############################
        # CHARACTER >> PHYSICS >> HORIZONTAL
        ##############################

        if self.x <= 0:
            self.horizontal_velocity = self.horizontal_velocity
            self.stun = 5
            self.x = self.w + 1

        if (self.x + self.w) >= pygame.display.Info().current_w:
            self.horizontal_velocity = -self.horizontal_velocity
            self.stun = 5
            self.x = pygame.display.Info().current_w - self.w
            #self.x -= (pygame.display.Info().current_w - self.w ) + 1

        if self.horizontal_velocity < 0:
            self.horizontal_velocity += 1
            self.x -= self.horizontal_velocity
        if self.horizontal_velocity > 0:
            self.horizontal_velocity -= 1
            self.x -= self.horizontal_velocity
        if self.horizontal_velocity == 0:
            self.horizontal_velocity = 0
        
        
        ##############################
        # CHARACTER >> PHYSICS >> VERTICAL
        ##############################

        self.y -= self.vertical_velocity
        if self.y == 500 - self.h: # On Ground
            self.control = True
            self.curr_speed = self.speed
            self.vertical_velocity = 0
            self.curr_jumps = self.jumps
            return
        if self.y > 500 - self.h: # Below the ground
            self.vertical_velocity = 0
            self.y = 500 - self.h
            return
        if self.y < 500 - self.h: # In the Air
            self.sprite_list = eval(f"self.sprite_sheet.falling_{self.facing}")
            self.curr_speed = self.air_speed
        if self.vertical_velocity >= self.terminal_velocity: # check to see if velocity is max
            self.vertical_velocity = self.terminal_velocity
        self.vertical_velocity -= 1

    ##############################
    # CHARACTER >> CONTROLLER
    ##############################

    def controller(self,key_held,key_down,key_up):

        if self.stun != 0:
            self.control = False
            self.stun -= 0.5
        
        if not self.control:
            return

        ##############################
        # CHARACTER >> CONTROLLER >> W
        ##############################

        if key_down == "w":
            if self.curr_jumps <= 0:
                return
            self.curr_jumps -= 1
            self.vertical_velocity = self.jump

        ##############################
        # CHARACTER >> CONTROLLER >> A
        ##############################

        if key_held[pygame.K_a]:
            self.horizontal_velocity = self.curr_speed
            self.facing = "left"
            self.sprite_list = self.sprite_sheet.run_left

        ##############################
        # CHARACTER >> CONTROLLER >> S
        ##############################

        if key_held[pygame.K_s]:
            self.vertical_velocity -= 5

        ##############################
        # CHARACTER >> CONTROLLER >> D
        ##############################

        if key_held[pygame.K_d]:
            self.horizontal_velocity = -self.curr_speed
            self.facing = "right"
            self.sprite_list = self.sprite_sheet.run_right
    
michael = character("michael",speed=18,jump=20,jump_count=1)
bell = character("bell",speed=18,jump=20,jump_count=1)
lazarus = character("lazarus",speed=20,jump=20,jump_count=2)