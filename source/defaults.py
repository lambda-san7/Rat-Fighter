##############################
# IMPORTS
##############################

import pygame
import os 

##############################
# DEFAULT STUFF
##############################

pygame.init()

pygame.mouse.set_visible(False)

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

class new_camera:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.scale = 1
        self.horizontal_velocity = 0
        self.vertical_velocity = 0
        self.target_x = None
        self.target_y = None
    def follow(self,subject,speed_x,speed_y):
        center_x = (pygame.display.Info().current_w) / 2
        center_y = (pygame.display.Info().current_h) / 2

        self.x = midpoint(self.x,self.y,subject.x,subject.y)[0] - (pygame.display.Info().current_h) / 2
    
    def is_off_screen(self,subject):
        if ((subject.x <= camera.x) or 
            (subject.x >= camera.x + pygame.display.Info().current_w) or 
            (subject.y <= camera.y) or 
            (subject.y >= camera.y + pygame.display.Info().current_h)):
            return True
        return False


camera = new_camera()

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
# MATH
##############################

def distance(x1,y1,x2,y2):
    return [
        (x2 + x1)/2,
        (y2 + y1)/2
    ]

def midpoint(x1, y1, x2, y2):
    return [(x1 + x2) / 2,(y1 + y2) / 2]

def quarterpoint(x1, y1, x2, y2):
    return [(x1 + x2) / 4,(y1 + y2) / 4]

##############################
# CURSOR
##############################

class sprite:
    def __init__(self,file,name="sprite",w=20,h=20):
        self.name = name
        self.sprite = pygame.transform.scale(pygame.image.load(f"{dir_path}/assets/{file}"),(w,h))
    def render(self,x,y):
        window.blit(self.sprite,(x,y))

cursor = sprite(file="cursor.gif").sprite