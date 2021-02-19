import pygame, mixer, os, random, sys
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

def drawText(text, font, surface, x, y):
    textobj = font.render(text, 1, TEXTCOLOR)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
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
gameOverSound = pygame.mixer.Sound('gameover.wav')
pygame.mixer.music.load('gameover.wav')


#IMAGES
playerImage = pygame.image.load ('player.png')
PlayerRect = playerImage.get_rect()
villainImage = pygame.image.load ('villain.png')

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
    #pygame.mixer.music.play(-1, 0.0)

while True: # game loop runs while the game part is playing
    score += 1 # Score increase

    for event in pygame.event.get():
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
                moveLeft = False
                moveRight = True
            if event.key == K_UP or event.key == K_w:
                moveDown =False
                moveUp = True
            if event.key == K_DOWN or event.key == K_S:
                moveUp = False
                moveDown = True

            if event.type == KEYUP:
                if event.key == K_z:
                    reverseCheat = False
                    score = 0
                if event.key == K_x:
                    slowCheat = False
                    score = 0
                if event.key ==K_ESCAPE:
                    terminate()

                if event.key == K_LEFT or event.key == K_a:
                    moveLeft = False
                if event.key == K_RIGHT or event.key == K_d:
                    moveRight = False
                if event.key == K_UP or event.key == K_w:
                    moveUp = False
                if event.key == K_DOWN or event.key == K_s:
                    moveDown = False

            if event.type == MOUSEMOTION:
                #If the mouse moves, player is placed on the cursor
                playerRect.centerx = event.pos[0]
                playerRect.century = event.pos[1]
        #New villains at the top of the screen
        if not reverseCheat and not slowCheat:
            villainAddCounter += 1
        if villainAddCounter == ADDNEWVILLAINRATE:
            villainAddCounter =0
            villainSize = random.randint(VILLAINMINSIZE, VILLAINMAXSIZE)
            newVillain = {'rect': pygame.Rect(random.randint(0,
                            WINDOWWIDTH - villainSize), 0 - villainSize,
                            villainSize, villainSize),
                          'speed': random.randint(VILLAINMINSPEED,
                            VILLAINMAXSPEED),
                          'surface':pygame.transform.scale(villainImage,
                            (villainSize, villainSize)),
                          }

            villains.append(newVillain)

        #Player movement
        if moveLeft and playerRect.left > 0:
            playerRect.move_ip(-1 * PLAYERMOVERATE, 0)
        if moveRight and playerRect.right < WINDOWWIDTH:
            playerRect.move_ip(PLAYERMOVERATE, 0)
        if moveUp and playerRect.top > 0:
            playerRect.move_ip(0, -1 * PLAYERMOVERATE)
        if moveDown and playerRect.bottom < WINDOWHEIGHT:
            playerRect.move_ip(0, PLAYERMOVERATE)

        #Move the villains down
        for v in villains:
            if not reverseCheat and not slowCheat:
                v['rect'].move_ip(0, v['speed'])
            elif reverseCheat:
                v['rect'].move_ip(0, -5)
            elif slowCheat:
                v['rect'].move_ip(0,1)

        #Remove villains at the bottom of screen
            for v in villains[:]:
                if v['rect'].top > WINDOWWEIGHT:
                    villains.remove(b)

        #Game world on the window
        windowSurface.fill(BACKGROUNDCOLOR)

        #Score and top score
        drawText('Score: %s' % (score), font, windowSurface, 10, 0)
        drawText('Top Score: %s' % (topScore), font, windowSurface,
            10, 40)

        #Players surface
        windowsurface.blit(playerImage, playerRect)

        #Draw willains
        for v in villains:
            windowsurface.blit(v['surface'], v['rect'])

        pygame.display.update()

        #Check if the villains have touched the player
        if playerHasHitVillain(playerRect, villains):
            if score > topScore:
                topScore = score #Set new top score
            break

        mainCLock.tick(FPS)

    #Game stop and show 'Game Over' screen
    pygame.mixer.music.stop()
    gameOverSound.play()

    drawText('GAME OVER', font, windowSurface, (WINDOWWIDTH / 3),
        (WINDOWWEIGHT / 3))
    drawText('Press any key to play again!', font, windowSurface,
             (WINDOWWIDTH / 3) - 80, (WINDOWWEIGHT / 3) + 50)
    pygame.display.update()
    StandByForPlayerToPressKey()

    gameOverSound.stop()








