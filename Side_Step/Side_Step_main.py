import pygame, random, sys
from pygame.locals import *

WINDOWWIDTH = 600
WINDOWHEIGHT = 600
TEXTCOLOR = (0, 0, 0)
BACKGROUNDCOLOR = (255, 125, 51)
FPS = 60
VILLAINMINSIZE = 10
VILLAINMAXSIZE = 40
VILLAINMINSPEED = 1
VILLAINMAXSPEED = 8
ADDNEWVILLAINRATE = 6
PLAYERMOVERATE = 5

def terminate():
    pygame.quit()
    sys.exit()

def StandByForPlayerToPressKey():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE: #ESC quits the game
