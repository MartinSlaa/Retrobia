# Import the pygame library and start game
import pygame
from pygame.locals import *
import os
import time
import sys

# import paddle class and ball class
from paddle import Paddle
from ball import Ball
from brick import Brick
from levelbuilder import *

# INITIALIZE PYGAME
pygame.init()
pygame.font.init()
# pygame.mixer.init()

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
BGCOLOR = (32, 32, 32)


def init_lives():
    score = 0
    lives = 100
    return score, lives


# Setting highscore
highscore = 0
file = open("Bricks/assets/score.txt", "r")
content = file.read()

# open a new window
screen_width = 800
screen_height = 600
size = (screen_width, screen_height)
FPS = 60

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Bricks")

# List of sprites to be used in game
all_bricks = pygame.sprite.Group()

# This will be a list that will contain all the sprites we intend to use in game
all_sprites_list = pygame.sprite.Group()

font = pygame.font.SysFont('chalkduster', 120)
font1 = pygame.font.SysFont(None, 40)
font2 = pygame.font.SysFont(None, 30)
font3 = pygame.font.SysFont('comicsansms', 30)


# Sounds
main_menu_theme = pygame.mixer.Sound('Bricks/assets/background.mp3')  ##Credit to DonimikBraun @ freesound.org
game_over_sound = pygame.mixer.Sound('Bricks/assets/game_over.mp3')  ##Credit to Baltiyar13 @ freesound.org
level_complete_sound = pygame.mixer.Sound('Bricks/assets/level_complete.mp3')  ##Credit to ProjectsU012 @ freesound.org


def draw_loading(screen):
    # Fill background
    screen.fill(BGCOLOR)

    # Display logo
    LOGO = pygame.image.load('Bricks/assets/logo.png')
    screen.blit(LOGO, (300, 100))

    font1 = pygame.font.Font(None, 74)
    text = font1.render("Loading...", 1, WHITE)
    screen.blit(text, (290, 450))

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


def main_menu_menu(screen, font, selected):
    screen.fill(BRICK)

    title = font.render("BRICKS!", 1, YELLOW)
    if selected == 'start':
        text_start = text_format('START', font1, 1, WHITE)
    else:
        text_start = text_format('START', font1, 1, BLACK)
    if selected == 'quit':
        text_quit = text_format('QUIT', font1, 1, WHITE)
    else:
        text_quit = text_format('QUIT', font1, 1, BLACK)
    if selected == 'howto':
        text_howto = text_format('HOW TO PLAY BRICKS', font1, 1, WHITE)
    else:
        text_howto = text_format('HOW TO PLAY BRICKS', font1, 1, BLACK)
    return title, text_start, text_quit, text_howto


def display_howto(screen, font):
    screen.fill(LIGHTBLUE)
    title = text_format('HOW TO PLAY BRICKS', font1, 1, YELLOW)
    howto = text_format('Move using left and right arrow, start game with SPACEBAR', font2, 75, BLACK)
    back1 = text_format('GO', font1, 75, BLACK)
    back2 = text_format('BACK', font1, 75, BLACK)
    title_rect = title.get_rect()
    howto_rect = howto.get_rect()
    back1_rect = back1.get_rect()
    back2_rect = back2.get_rect()
    go_back = False
    while True:
        for event in pygame.event.get():  # user has done something
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    back1 = text_format('GO', font1, 75, WHITE)
                    back2 = text_format('BACK', font1, 75, WHITE)
                    back1_rect = back1.get_rect()
                    back2_rect = back2.get_rect()
                    go_back = True
                if go_back and event.key == pygame.K_UP:
                    back1 = text_format('GO', font1, 75, BLACK)
                    back2 = text_format('BACK', font1, 75, BLACK)
                    back1_rect = back1.get_rect()
                    back2_rect = back2.get_rect()
                    go_back = False
                if go_back and event.key == pygame.K_RETURN:
                    return

        screen.blit(title, (screen_width / 2 - (title_rect[2] / 2), 80))
        screen.blit(howto, (screen_width / 2 - (howto_rect[2] / 2), 240))
        screen.blit(back1, (screen_width / 2 - (back1_rect[2] / 2), 400))
        screen.blit(back2, (screen_width / 2 - (back2_rect[2] / 2), 440))
        pygame.display.update()
        clock.tick(FPS)



def main_menu():
    # Sound played on game menu
    pygame.mixer.Sound.play(main_menu_theme)

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
                        # print('start')
                        menu = False
                        main_menu_theme.fadeout(1000)
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


# Game Over Screen
def game_over():
    # if lives == 0:
    screen.fill(DARKBLUE)
    # Display game over message
    game_over_message = font3.render('Game Over! Press Enter to play again!', 1, WHITE)
    font_pos_message = game_over_message.get_rect(center=(screen_width // 2, screen_height // 2))
    # Your score message
    game_over_score = font3.render(f'Your score was {score}', 1, WHITE)
    font_pos_score = game_over_score.get_rect(center=(screen_width // 2, screen_height // 2 + 40))
    # Message displaying current highscore
    high_score = font3.render(f"Current Highscore is: {highscore}", 1, WHITE)
    font_pos_highscore = high_score.get_rect(center=(screen_width // 2, screen_height // 2 + 80))
    # Message displayed when highscore is beaten
    beat_high_score = font3.render(f"New Highscore!", 1, WHITE)
    font_pos_new_highscore = beat_high_score.get_rect(center=(screen_width // 2, screen_height // 2 + 80))
    # Message displayed when highscore is tied
    tie_score = font3.render(f"You tied with the Highscore!", 1, WHITE)
    font_pos_tie_score = tie_score.get_rect(center=(screen_width // 2, screen_height // 2 + 80))
    screen.blit(game_over_message, font_pos_message)
    screen.blit(game_over_score, font_pos_score)
    pygame.display.flip()
    pygame.display.update()
    # Sound played on game over screen
    pygame.mixer.Sound.play(game_over_sound)
    # When current score is higher than the high score
    if score > highscore:
        screen.blit(beat_high_score, font_pos_new_highscore)
        with open("Bricks/assets/score.txt", "w") as f:
            f.write(f"Current highscore is: {score}\n")
            f.close()
    # When current score is the same as the high score
    if score == highscore:
        screen.blit(tie_score, font_pos_tie_score)
        with open("Bricks/assets/score.txt", "w") as f:
            f.write(f"Your shared highscore is: {score}\n")
            f.close()
    # When current score is lower than the high score
    if score < highscore:
        screen.blit(high_score, font_pos_highscore)
        pass
    pygame.display.update()
    pygame.time.wait(2000)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            elif event.type == KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return
        pygame.display.update()


def level_complete():
    # if len(all_bricks) == 0:
    screen.fill(DARKBLUE)

    # Sound played for level complete:
    pygame.mixer.Sound.play(level_complete_sound)

    # Display level complete message
    level_complete_message = font2.render('LEVEL COMPLETE! PRESS ENTER TO PLAY THE NEXT LEVEL', 1, WHITE)
    font_pos_message = level_complete_message.get_rect(center=(screen_width // 2, screen_height // 2))
    screen.blit(level_complete_message, font_pos_message)
    pygame.display.flip()
    pygame.display.update()
    pygame.time.wait(2000)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            elif event.type == KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return
        pygame.display.update()


# List of sprites to be used in game
all_sprites_list = pygame.sprite.Group()

# Create the paddle
paddle = Paddle(LIGHTBLUE, 100, 10)
paddle.rect.x = 350
paddle.rect.y = 560

# Create the ball sprite
ball = Ball(WHITE, 10, 10)
ball.rect.x = 345
ball.rect.y = 195
ball.moveToPaddle(paddle)

# Add paddle to the list of sprites
all_sprites_list.add(paddle)
all_sprites_list.add(ball)
build_bricks(all_bricks)

# Game clock will be used to control how quickly the screen updates
clock = pygame.time.Clock()
level = 1
level_up = False
# Main PROGRAM LOOP

while True:

    if not level_up:
        draw_loading(screen)
        main_menu()
        score, lives = init_lives()
    else:
        level_up = False
    carryOn = True
    build_bricks(all_bricks, level)

    while carryOn:

        # MAIN EVENT LOOP
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
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
            game_over()
            level_up = False
            level = 1
            break

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
            score += 10
            brick.kill()

            highscore = 0
            file = open('Bricks/assets/score.txt', 'r')
            content = file.read()

            x = content.split()
            for i in x:
                if i.isdigit():
                    highscore = int(i)

            if len(all_bricks) == 0:
                # Display level complete message for 3 seconds
                level_complete()
                level += 1
                level_up = True
                carryOn = False
                ball.moveToPaddle(paddle)

            pygame.display.update()

        # clear screen to dark blue
        screen.fill(DARKBLUE)
        pygame.draw.line(screen, WHITE, [0, 38], [800, 38], 2)

        # Display score and lives at the top of the game screen
        text = font1.render("Score: " + str(score), 1, WHITE)
        screen.blit(text, (20, 10))
        text = font1.render("Lives: " + str(lives), 1, WHITE)
        screen.blit(text, (650, 10))
        # text = font1.render("High Score: " + str(), 1, WHITE)
        # screen.blit(text, (300, 10))

        # place spirites
        all_sprites_list.draw(screen)
        all_bricks.draw(screen)

        pygame.display.flip()
        clock.tick(FPS)