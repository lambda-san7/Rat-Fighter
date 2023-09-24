##############################
# IMPORTS
##############################

import pygame
import math
from defaults import window, running, clock, fps, dir_path, camera, distance

##############################
# COLLISIONS
##############################

class collisions:
    def __init__(self):
        self.grounded = False
        self.air = False
        self.above_ground = False
        self.underground = False
        self.climbing = False

    def get(self,object,map,collidables=[]):

        self.grounded = False
        self.air = False
        self.above_ground = False
        self.underground = False
        self.climbing = False

        if ((object.y == map.y - object.h) and
            (object.x + object.w >= map.x) and
            (object.x <= map.x + map.w)
            ): # on ground
            self.grounded = True

        if ((object.y + object.h < map.y)): # above the ground
            self.air = True

        if ((object.y + object.h > map.y) and
            (object.x + object.w >= map.x) and
            (object.x <= map.x + map.w) and
            (object.y < map.y + map.h)
            ): # in the ground
            self.underground = True
            

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

        self.walk_left = [
            sprite(f"{name}/walk_1.gif").sprite,
            sprite(f"{name}/walk_2.gif").sprite,
            sprite(f"{name}/walk_3.gif").sprite,
            sprite(f"{name}/walk_4.gif").sprite,
        ]
        
        self.walk_right = [
            pygame.transform.flip(self.walk_left[0], True, False),
            pygame.transform.flip(self.walk_left[1], True, False),
            pygame.transform.flip(self.walk_left[2], True, False),
            pygame.transform.flip(self.walk_left[3], True, False),
        ]


##############################
# CHARACTER CLASSES
##############################

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
        self.walk_speed = speed - 5
        self.run_speed = speed
        self.ground_speed = self.walk_speed
        self.air_speed = speed + 5
        self.jump = jump
        self.jumps = jump_count
        self.curr_jumps = jump_count
        self.walking = 0
        self.walked = False
        self.x = 600
        self.y = 100
        self.horizontal_velocity = 0
        self.vertical_velocity = 0
        self.terminal_velocity = 50
        self.shadow = sprite("shadow.gif",w=100,h=24).sprite
        self.control = False
        self.stun = 0
        self.collisions = collisions()

    ##############################
    # CHARACTER >> HANDLE
    ##############################

    def handle(self,key_held,key_down,key_up,map):
        camera.follow(self,10,5)
        if self.is_off_screen(self,1000):
            print(self.x, self.y)
            self.x = 600
            self.y = 100
    #    camera.x = distance(
     #       self.x + (self.w / 2),
      #      self.y,
       #     map.x + (map.w / 2),
        #    map.y
        #)[0] - (pygame.display.Info().current_w / 2)
        self.sprite_list = eval(f"self.sprite_sheet.idle_{self.facing}")
        self.controller(key_held,key_down,key_up)
        self.physics(map)
        self.animate(0.2)
        self.render(self.x,self.y)

    ##############################
    # CHARACTER >> RENDER
    ##############################

    def render(self,x,y):
    #    self.shadow.render(
     #       self.x,
      #      (pygame.display.Info().current_h / 2) + 2
       # )
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
        self.y -= self.vertical_velocity
        self.collisions.get(self,map)
        
        ##############################
        # CHARACTER >> PHYSICS >> HORIZONTAL
        ##############################

#        if self.x <= 0:
 #           self.horizontal_velocity = self.horizontal_velocity
  #          self.stun = 5
   #         self.x = self.w + 1

    #    if (self.x + self.w) >= pygame.display.Info().current_w:
     #       self.horizontal_velocity = -self.horizontal_velocity
      #      self.stun = 5
       #     self.x = pygame.display.Info().current_w - self.w
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

        if self.collisions.grounded: # On Ground
            self.control = True
            self.curr_speed = self.ground_speed
            self.vertical_velocity = 0
            self.curr_jumps = self.jumps
            return
        if self.collisions.underground: # Below the ground
            self.vertical_velocity = 0
            self.y = map.y - self.h
            return
        if self.collisions.air: # In the Air
            self.sprite_list = eval(f"self.sprite_sheet.falling_{self.facing}")
            self.curr_speed = self.air_speed
        self.vertical_velocity -= 1

    ##############################
    # CHARACTER >> CONTROLLER
    ##############################

    def controller(self,key_held,key_down,key_up):
        self.walked = False

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
            #self.sprite_list = self.sprite_sheet.run_left
            self.sprite_list = self.sprite_sheet.walk_left
            self.ground_speed = self.walk_speed
            self.walked = True
            self.walking += 1
            if self.walking >= 25:
                self.sprite_list = self.sprite_sheet.run_left
                self.ground_speed = self.run_speed

        ##############################
        # CHARACTER >> CONTROLLER >> D
        ##############################

        if key_held[pygame.K_d]:
            self.horizontal_velocity = -self.curr_speed
            self.facing = "right"
            #self.sprite_list = self.sprite_sheet.run_right
            self.sprite_list = self.sprite_sheet.walk_right
            self.ground_speed = self.walk_speed
            self.walked = True
            self.walking += 1
            if self.walking >= 25:
                self.sprite_list = self.sprite_sheet.run_right
                self.ground_speed = self.run_speed

        ##############################
        # CHARACTER >> CONTROLLER >> S
        ##############################

        if key_held[pygame.K_s]:
            self.vertical_velocity -= 5
            #self.sprite_list = eval(f"self.sprite_sheet.crouch_{self.facing}")

        if not self.walked:
            self.walking = 0

    def is_off_screen(self,subject,buffer=0):
        if ((subject.x < (0 - buffer)) or 
            (subject.x > (pygame.display.Info().current_w + buffer)) or 
            (subject.y < (0 - buffer)) or 
            (subject.y > (pygame.display.Info().current_h + buffer))):
            return True
        return False
    
michael = character("michael",speed=15,jump=20,jump_count=2)
bell = character("bell",speed=15,jump=20,jump_count=2)
lazarus = character("lazarus",speed=20,jump=20,jump_count=2)
#testing_character = character("testing",speed=15,jump=20,jump_count=999)