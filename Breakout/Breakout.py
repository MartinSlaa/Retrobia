# Import the pygame library and start game
import pygame
import pygame.locals
import os
import time
import sys

# import paddle class and ball class
from paddle import Paddle
from ball import Ball
from brick import Brick

# INITIALIZE PYGAME
pygame.init()

# Center the Game Application
os.environ['SDL_VIDEO_CENTERED'] = '1'

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
DARKBLUE = (36, 90, 190)
LIGHTBLUE = (0, 176, 240)
RED = (255, 0, 0)
ORANGE = (255, 100, 0)
YELLOW = (255, 255, 0)
BRICK = (80, 25, 33)

score = 0
lives = 3

# open a new window
screen_width = 800
screen_height = 600
size = (screen_width, screen_height)
FPS = 80

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Bricks")

# This will be a list that will contain all the sprites we intend to use in game
all_sprites_list = pygame.sprite.Group()
font = pygame.font.Font(None, 34)

# Draw loading screen
def drawLoading(screen):
    # Fill background
    screen.fill(BLACK)

    # Display logo
    LOGO = pygame.image.load('./assets/logo.png').convert()
    screen.blit(LOGO, (300, 100))

    font1 = pygame.font.Font(None, 74)
    text = font1.render("Loading...", 1, WHITE)
    screen.blit(text, (300, 450))

    # Update screen
    pygame.display.update()

    # Update game screen
    pygame.display.update()
    tic = time.time()
    wait = True
    while wait:
        if time.time() - tic > 2:
            wait = False
            break
        events = [e.type for e in pygame.event.get()]
        if pygame.locals.QUIT in events:
            pygame.quit()
            sys.exit(0)

# TEXT RENDER
def text_format(message, textFont, size, textColor):
    newText = textFont.render(message, size, textColor)
    return newText

##GAME FONTS
# font = 'Retro.ttf'
def main_menu_menu(screen, font, selected):
    screen.fill(DARKBLUE)
    title = text_format('BRICKS!', font, 90, YELLOW)
    if selected == 'start':
        text_start = text_format('START', font, 75, WHITE)
    else:
        text_start = text_format('START', font, 75, BLACK)
    if selected == 'quit':
        text_quit = text_format('QUIT', font, 75, WHITE)
    else:
        text_quit = text_format('QUIT', font, 75, BLACK)
    if selected == 'howto':
        text_howto = text_format('HOW TO PLAY BRICKS', font, 75, WHITE)
    else:
        text_howto = text_format('HOW TO PLAY BRICKS', font, 75, BLACK)
    return title, text_start, text_quit, text_howto


def display_howto(screen, font):
    screen.fill(LIGHTBLUE)
    title = text_format('HOW TO PLAY BRICKS', font, 90, YELLOW)
    howto = text_format('Move using left and right arrow, start game with SPACEBAR', font, 75, BLACK)
    back = text_format('GO BACK', font, 75, BLACK)
    title_rect = title.get_rect()
    howto_rect = howto.get_rect()
    back_rect = back.get_rect()
    go_back = False
    while True:
        for event in pygame.event.get():  # user has done something
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    back = text_format('GO BACK', font, 75, WHITE)
                    back_rect = back.get_rect()
                    go_back = True
                if go_back and event.key == pygame.K_UP:
                    back = text_format('GO BACK', font, 75, BLACK)
                    back_rect = back.get_rect()
                    go_back = False
                if go_back and event.key == pygame.K_RETURN:
                    return

        screen.blit(title, (screen_width / 2 - (title_rect[2] / 2), 80))
        screen.blit(howto, (screen_width / 2 - (howto_rect[2] / 2), 340))
        screen.blit(back, (screen_width / 2 - (back_rect[2] / 2), 500))
        pygame.display.update()
        clock.tick(FPS)


def main_menu():
    menu = True
    selection = ['start', 'howto', 'quit']
    idx = 0
    selected = selection[idx]

    while menu:
        # Main event loop
        for event in pygame.event.get():  # user has done something
            if event.type == pygame.QUIT:  # player closed game window
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    idx = (idx + 1) % 3
                elif event.key == pygame.K_UP:
                    idx = (idx - 1) % 3
                selected = selection[idx]
                if event.key == pygame.K_RETURN:
                    if selected == 'start':
                        print('start')
                        menu = False
                    elif selected == 'quit':
                        pygame.quit()
                        quit()
                    else:
                        display_howto(screen, font)
        # Update selection
        title, text_start, text_quit, text_howto = main_menu_menu(screen, font, selected)
        title_rect = title.get_rect()
        start_rect = text_start.get_rect()
        quit_rect = text_quit.get_rect()
        howto_rect = text_howto.get_rect()
        screen.blit(title, (screen_width / 2 - (title_rect[2] / 2), 80))
        screen.blit(text_start, (screen_width / 2 - (start_rect[2] / 2), 280))
        screen.blit(text_howto, (screen_width / 2 - (howto_rect[2] / 2), 340))
        screen.blit(text_quit, (screen_width / 2 - (quit_rect[2] / 2), 400))
        pygame.display.update()
        clock.tick(FPS)



# List of sprites to be used in game
all_sprites_list = pygame.sprite.Group()

# Create the paddle
paddle = Paddle(LIGHTBLUE, 100, 10)
paddle.rect.x = 350
paddle.rect.y = 560

# create the ball sprite
ball = Ball(WHITE, 10, 10)
ball.rect.x = 345
ball.rect.y = 195
ball.moveToPaddle(paddle)

all_bricks = pygame.sprite.Group()
for i in range(7):
    brick = Brick(RED, 80, 30)
    brick.rect.x = 60 + i * 100
    brick.rect.y = 60
    all_sprites_list.add(brick)
    all_bricks.add(brick)
for i in range(7):
    brick = Brick(ORANGE, 80, 30)
    brick.rect.x = 60 + i * 100
    brick.rect.y = 100
    all_sprites_list.add(brick)
    all_bricks.add(brick)
for i in range(7):
    brick = Brick(YELLOW, 80, 30)
    brick.rect.x = 60 + i * 100
    brick.rect.y = 140
    all_sprites_list.add(brick)
    all_bricks.add(brick)

# Add paddle to the list of sprites
all_sprites_list.add(paddle)
all_sprites_list.add(ball)

# Loading screen
drawLoading(screen)

# Game loop will run until player/user exits game
carryOn = True

# Game clock will be used to control how quickly the screen updates
clock = pygame.time.Clock()

main_menu()

# MAIN PROGRAM LOOP

while carryOn:

    # MAIN EVENT LOOP
    for event in pygame.event.get():
        if event.type == pygame.locals.QUIT:
            carryOn = False
    # Moving the paddle
    # def moving_paddle():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        paddle.moveLeft(5)
        if not ball.moving:
            ball.moveToPaddle(paddle)
    if keys[pygame.K_RIGHT]:
        paddle.moveRight(5)
        if not ball.moving:
            ball.moveToPaddle(paddle)
    if not ball.moving and keys[pygame.K_SPACE]:
        ball.move()

    # game logic
    all_sprites_list.update()

    # Check if the ball is bouncing against any of the 4 walls:
    if ball.rect.x >= 790:
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.x <= 0:
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.y > 590:
        ball.stop()
        ball.moveToPaddle(paddle)
        lives -= 1
        if lives == 0:
            # Display Game Over Message for 3 seconds
            font1 = pygame.font.Font(None, 50)
            text = font1.render("GAME OVER! PLAY AGAIN?", 1, WHITE)
            screen.blit(text, (175, 300))
            pygame.display.flip()
            pygame.time.wait(5000)

    if ball.rect.y < 40:
        ball.velocity[1] = -ball.velocity[1]

    # Detect collisions between the ball and the paddle
    if pygame.sprite.collide_mask(ball, paddle):
        ball.rect.x -= ball.velocity[0]
        ball.rect.y -= ball.velocity[1]
        ball.bounce()

        # Check if there is the ball collides with any bricks
    brick_collision_list = pygame.sprite.spritecollide(ball, all_bricks, False)
    for brick in brick_collision_list:
        ball.bounce()
        score += 1
        brick.kill()
        if len(all_bricks) == 0:
            # Display level complete message for 3 seconds
            font1 = pygame.font.Font(None, 50)
            text = font1.render('LEVEL COMPLETE', 1, YELLOW)
            screen.blit(text, (275, 300))
            pygame.display.flip()
            pygame.time.wait(3000)
            title = text_format('LEVEL COMPLETE', font, 90, YELLOW)

            # stop the game
            carryOn = True

    # clear screen to dark blue
    screen.fill(DARKBLUE)
    pygame.draw.line(screen, WHITE, [0, 38], [800, 38], 2)

    # Display score and lives at the top of the game screen
    text = font.render("Score: " + str(score), 1, WHITE)
    screen.blit(text, (20, 10))
    text = font.render("Lives: " + str(lives), 1, WHITE)
    screen.blit(text, (650, 10))

    # place spirites
    all_sprites_list.draw(screen)


    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()

