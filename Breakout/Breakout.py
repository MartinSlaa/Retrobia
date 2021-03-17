#Import the pygame library and start game
import pygame

#import paddle class and ball class
from paddle import Paddle
from ball import Ball
from brick import Brick

pygame.init()

#Define colors
WHITE = (255,255,255)
DARKBLUE = (36,90,190)
LIGHTBLUE = (0,176,240)
RED = (255,0,0)
ORANGE = (255,100,0)
YELLOW = (255,255,0)

score = 0
lives = 3

#Open game window
size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Breakout Game")

#List of sprites to be used in game
all_sprites_list = pygame.sprite.Group()

#Create the paddle
paddle = Paddle(LIGHTBLUE, 100, 10)
paddle.rect.x = 350
paddle.rect.y = 560

#create the ball sprite
ball = Ball(WHITE,10,10)
ball.rect.x = 345
ball.rect.y = 195

all_bricks = pygame.sprite.Group()
for i in range(7):
    brick = Brick(RED,80,30)
    brick.rect.x = 60 + i* 100
    brick.rect.y = 60
    all_sprites_list.add(brick)
    all_bricks.add(brick)
for i in range(7):
    brick = Brick(ORANGE,80,30)
    brick.rect.x = 60 + i* 100
    brick.rect.y = 100
    all_sprites_list.add(brick)
    all_bricks.add(brick)
for i in range(7):
    brick = Brick(YELLOW,80,30)
    brick.rect.x = 60 + i* 100
    brick.rect.y = 140
    all_sprites_list.add(brick)
    all_bricks.add(brick)

#Add paddle to the list of sprites
all_sprites_list.add(paddle)
all_sprites_list.add(ball)

#Game loop will run until player/user exits game
carryOn = True

#Game clock will be used to control how quickly the screen updates
clock = pygame.time.Clock()

# MAIN PROGRAM LOOP
while carryOn:
    #Main event loop
    for event in pygame.event.get(): #user has done something
        if event.type == pygame.QUIT: #player closed game window
            carryOn = False #flag the we are done so we can exit the loop


    #Moving the paddle
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        paddle.moveLeft(5)
    if keys[pygame.K_RIGHT]:
        paddle.moveRight(5)

    #game logic
    all_sprites_list.update()

    #Check if the ball is bouncing against any of the 4 walls:
    if ball.rect.x>=790:
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.x<=0:
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.y>590:
        ball.velocity[1] = -ball.velocity[1]
        lives -= 1
        if lives == 0:
            #Display Game Over Message for 3 seconds
            font = pygame.font.Font(None, 74)
            text = font.render("GAME OVER", 1, WHITE)
            screen.blit(text, (250,300))
            pygame.display.flip()
            pygame.time.wait(3000)

            #STOP GAME
            carryOn=False

    if ball.rect.y<40:
        ball.velocity[1] = -ball.velocity[1]

    #Detect collisions between the ball and the paddle
    if pygame.sprite.collide_mask(ball, paddle):
        ball.rect.x -= ball.velocity[0]
        ball.rect.y -= ball.velocity[1]
        ball.bounce()

        #Check if there is the ball collides with any bricks
        brick_collision_list = pygame.sprite.spritecollide(ball,all_bricks,False)
        for brick in brick_collision_list:
            ball.bounce()
            score += 1
            brick.kill()
            if len(all_bricks)==0:
                #Display level complete message for 3 seconds
                font = pygame.font.Font(None, 74)
                text = font.render("LEVEL COMPLETE", 1, WHITE)
                screen.blit(text, (200,300))
                pygame.display.flip()
                pygame.time.wait(3000)

                #stop the game
                carryOn=False


    #clear screen to dark blue
    screen.fill(DARKBLUE)
    pygame.draw.line(screen, WHITE, [0, 38], [800, 38], 2)

    #Display score and lives at the top of the game screen
    font = pygame.font.Font(None, 34)
    text = font.render("Score: " + str(score), 1, WHITE)
    screen.blit(text, (20,10))
    text = font.render("Lives: " + str(lives), 1, WHITE)
    screen.blit(text, (650,10))

    #place spirites
    all_sprites_list.draw(screen)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()

