##############################
# IMPORTS
##############################

import pygame
from defaults import window, running, clock, fps, dir_path
import keys

##############################
# SPRITES
##############################

class sprite:
    def __init__(self,file,name="sprite",w=100,h=100):
        self.name = name
        self.sprite = pygame.transform.scale(pygame.image.load(f"{dir_path}/{file}"),(w,h))
    def render(self,x,y):
        window.blit(self.sprite,(x,y))

class sprite_sheet:
    def __init__(self,name):

        ##### IDLE #####

        self.idle_left_1 = sprite(f"{name}/idle 1")
        self.idle_left_2 = sprite(f"{name}/idle 2")
        self.idle_left_3 = sprite(f"{name}/idle 3")
        self.idle_left_4 = sprite(f"{name}/idle 4")

        self.idle_left = [
            self.idle_left_1,
            self.idle_left_2,
            self.idle_left_3,
            self.idle_left_4,
        ]

        self.idle_right_1 = pygame.transform.flip(self.idle_left_1, True, False)
        self.idle_right_2 = pygame.transform.flip(self.idle_left_2, True, False)
        self.idle_right_3 = pygame.transform.flip(self.idle_left_3, True, False)
        self.idle_right_4 = pygame.transform.flip(self.idle_left_4, True, False)

        self.idle_right = [
            self.idle_right_1,
            self.idle_right_2,
            self.idle_right_3,
            self.idle_right_4,
        ]

        ##### RUNNING #####

        self.run_left_1 = sprite(f"{name}/run 1")
        self.run_left_2 = sprite(f"{name}/run 2")
        self.run_left_3 = sprite(f"{name}/run 3")
        self.run_left_4 = sprite(f"{name}/run 4")

        self.run_left = [
            self.run_left_1,
            self.run_left_2,
            self.run_left_3,
            self.run_left_4,
        ]

        self.run_right_1 = pygame.transform.flip(self.run_left_1, True, False)
        self.run_right_2 = pygame.transform.flip(self.run_left_2, True, False)
        self.run_right_3 = pygame.transform.flip(self.run_left_3, True, False)
        self.run_right_4 = pygame.transform.flip(self.run_left_4, True, False)

        self.run_right = [
            self.run_right_1,
            self.run_right_2,
            self.run_right_3,
            self.run_right_4,
        ]

        ##### ATTACKING #####

        self.run_left_1 = sprite()
        self.run_left_2 = sprite()
        self.run_left_3 = sprite()
        self.run_left_4 = sprite()

        self.run_left = [
            self.run_left_1,
            self.run_left_2,
            self.run_left_3,
            self.run_left_4,
        ]

        self.run_right_1 = pygame.transform.flip(sprite(), True, False)
        self.run_right_2 = pygame.transform.flip(sprite(), True, False)
        self.run_right_3 = pygame.transform.flip(sprite(), True, False)
        self.run_right_4 = pygame.transform.flip(sprite(), True, False)

        self.run_right = [
            self.run_right_1,
            self.run_right_2,
            self.run_right_3,
            self.run_right_4,
        ]

##############################
# CHARACTER CLASSES
##############################

class character:
    def __init__(self,name):
        self.name = name
        self.sprites = sprite_sheet(
            [
                f"{name}/run"
            ]
        )
        self.sprite =