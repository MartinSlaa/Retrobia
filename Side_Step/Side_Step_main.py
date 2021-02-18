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
                    terminate()
                return

def playerHasHitVillain(playerRect, villains):
    for v in villains:
        if playerRect.colliderect(v['rect']):
            return True
        return False

def provideText(text, font, surface, x, y):
    textobj = font.render(text, 1, TEXTCOLOR)
    textrect = textobj.get_rect()
    textrect.topleft = (x, Y)
    surface.blit(textobj, textrect)

#Set up pygame, window and the mouse cursor
pygame.init()
mainClock = pygame.time.Clock()
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('SIDE-STEP')
pygame.mouse.set_visible(False)

#FONTS
font = pygame.font.SysFont(None, 48)

#SOUNDS
#gameOverSound = pygame.mixer.Sound('gameover.wav')
#pygame.mixer.music.load('background.mp3')

#IMAGES
playerImage = pygame.image.load('player.png')
PlayerRect = playerImage.get_rect()
villainImage = pygame.image.load('villain.png')

#Start Screen
windowSurface.fill(BACKGROUNDCOLOR)
drawText('SIDE-STEP', font, windowSurface, (WINDOWWIDTH / 3),
         (WINDOWHEIGHT / 3))
drawText ('Press any key to start!', font, windowSurface,
    (WINDOWWIDTH / 3) - 30, (WINDOWHEIGHT / 3) + 50)
pygame.display.update()
StandByForPlayerToPressKey()

topScore = 0
while True:
    # Setup menu before game start
    villains = []
    score = 0
    playerRect.topleft = (WINDOWWIDTH / 2, WINDOWHEIGHT - 50)
    moveLeft = moveRight = moveUp = moveDown = False
    reverseCheat = slowCheat = False
    villainAddCounter = 0
    pygame.mixer.music.play(-1, 0.0)

while True: # game loop runs while the game part is playing
    score += 1 # Score increase

    for event in pygame.event.get()
        if event.type == QUIT:
            terminate()

        if even.type == KEYDOWN:
            if event.key == K_z:
                reverseCheat = True
            if event.key == K_x:
                slowCheat = True
            if event.key == K_LEFT or event.key == K_a:
                moveRight = False
                moveLeft = True
            if event.key == K_RIGHT or event.key ==K_d:
                moveLEFT = False
                moveRIGHT = True
            if event.key == K_UP or event.key == K_w:
                moveDOWN =False
                moveUP = True
            if event.key == K_DOWN or event.key == K_S:
                moveUP = False
                moveDown = True

            if event.type == KEYUP:
                if event.key == K_z:
                    reverseCheat = False
                    score = 0
                if event.key == K_x:
                    slowCheat = False
                    score = 0
                if event.key ==K_ESCAPE
                    terminate()

                if event.key == K_LEFT or event.key == K_a:
                    moveLEFT = False
                if event.key == K_RIGHT or event.key == K_d:
                    moveRIGHT = False
                if event.key == K_UP or event.key == K_w:
                    moveUP = False
                if event.key == K_DOWN or event.key == K_s:
                    moveDOWN = False







