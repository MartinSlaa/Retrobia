import random
import sys
import time
import os
import pygame


pygame.init()
pygame.font.init()
pygame.mixer.init()

# Fonts
font = pygame.font.SysFont('comicsansms', 30)
font2 = pygame.font.SysFont(None, 40)

# Open window in the middle of the screen
os.environ['SDL_VIDEO_CENTERED'] = '1'

# Window size
WIDTH = 720
HEIGHT = 480

# Game screen
pygame.display.set_caption("Retrobia Ssssnake")
gameScreen = pygame.display.set_mode((WIDTH, HEIGHT))

# Draw loading screen
def drawLoading():
    # Fill background
    gameScreen.fill((32, 32, 32))

    # Display logo
    gameScreen.blit(LOGO, (260, 100))

    # Display text
    textString = "Loading..."
    text = font2.render(textString, True, (192, 192, 192))
    gameScreen.blit(text, (300, 350))

    # Update game screen
    pygame.display.update()

# Load and resize assets
WATERMELON = pygame.image.load("snake/assets/Watermelon.png")
#WATERMELON = pygame.image.load(os.path.join("assets", "Watermelon.png"))
WATERMELON = pygame.transform.smoothscale(WATERMELON, (25, 25))
LOGO = pygame.image.load("snake/assets/logo.png")
#LOGO = pygame.image.load(os.path.join("snake/assets", "logo.png"))
RATTLESNAKE = pygame.image.load("snake/assets/Rattlesnake.png")
#RATTLESNAKE = pygame.image.load(os.path.join("assets", "Rattlesnake.png"))
RATTLESNAKE = pygame.transform.smoothscale(RATTLESNAKE, (205, 300))
WATERMELON_SLICE = pygame.image.load("snake/assets/watermelon-slice.png")
#WATERMELON_SLICE = pygame.image.load(os.path.join("assets", "watermelon-slice.png"))
WATERMELON_SLICE = pygame.transform.smoothscale(WATERMELON_SLICE, (100, 100))

# Sounds and sound effects
fruit_sound = pygame.mixer.Sound("snake/assets/watermelon-seed.wav")
#fruit_sound = pygame.mixer.Sound(os.path.join('assets', 'watermelon-seed.wav'))
game_over_sound= pygame.mixer.Sound("snake/assets/game-over.wav")
#game_over_sound = pygame.mixer.Sound(os.path.join('assets', 'game-over.wav'))
click_sound= pygame.mixer.Sound("snake/assets/retro-click.wav")
#click_sound = pygame.mixer.Sound(os.path.join('assets', 'retro-click.wav'))


# Menu Function
def main_menu():
    while 1:
        for event in pygame.event.get():
            # If user presses ESC
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # If user presses ENTER
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    # Sound effect to confirm ENTER
                    pygame.mixer.Sound.play(click_sound)
                    # Call main() function to start game
                    main()
        gameScreen.fill((0, 0, 0))
        # Message and artwork on the main menu
        main_menu_message = font.render('Press ENTER to start a new game', True, (75, 139, 59))
        font_pos = main_menu_message.get_rect(center=(WIDTH//2, HEIGHT//10))
        gameScreen.blit(main_menu_message, font_pos)
        # Snake artwork
        gameScreen.blit(RATTLESNAKE, (260, 100))
        # Watermelon artwork
        gameScreen.blit(WATERMELON_SLICE, (480, 300))
        gameScreen.blit(WATERMELON_SLICE, (140, 300))
        pygame.display.update()


# Game Over Screen
def game_over(score, highscore):
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        gameScreen.fill((0, 0, 0))
        # You Lost message
        game_over_message = font.render('You Lost', True, (255, 0, 0))
        font_pos_message = game_over_message.get_rect(center=(WIDTH//2, HEIGHT//2))
        # Your score message
        game_over_score = font.render(f'Your score was {score}', True, (255, 255, 255))
        font_pos_score = game_over_score.get_rect(center=(WIDTH//2, HEIGHT//2+40))
        # Message displaying current highscore
        high_score = font.render(f"Current Highscore is: {highscore}", 1, (255, 165, 0))
        font_pos_highscore = high_score.get_rect(center=(WIDTH//2, HEIGHT//2+80))
        # Message displayed when highscore is beaten
        beat_high_score = font.render(f"New Highscore!", 1, (255, 215, 0))
        font_pos_new_highscore = beat_high_score.get_rect(center=(WIDTH//2, HEIGHT//2+80))
        # Message displayed when highscore is tied
        tie_score = font.render(f"You tied with the Highscore!", 1, (255, 255, 255))
        font_pos_tie_score = tie_score.get_rect(center=(WIDTH//2, HEIGHT//2+80))
        gameScreen.blit(game_over_message, font_pos_message)
        gameScreen.blit(game_over_score, font_pos_score)
        # Sound played on game over screen
        pygame.mixer.Sound.play(game_over_sound)
        # When current score is higher than the high score
        if score > highscore:
            gameScreen.blit(beat_high_score, font_pos_new_highscore)
            with open("snake/score.txt", "w") as f:
                f.write(f"Current highscore is: {score}\n")
                f.close()
        # When current score is the same as the high score
        if score == highscore:
            gameScreen.blit(tie_score, font_pos_tie_score)
            with open("snake/score.txt", "w") as f:
                f.write(f"Your shared highscore is: {score}\n")
                f.close()
        # When current score is lower than the high score
        if score < highscore:
            gameScreen.blit(high_score, font_pos_highscore)
            pass
        pygame.display.update()

        time.sleep(5)
        main_menu()


# Main Function
def main():
    clock = pygame.time.Clock()
    snake_pos = [200, 70]
    snake_body = [[200, 70], [200 - 10, 70], [200 - (2 * 10), 70]]
    direction = 'right'
    score = 0
    fruit_pos = [0, 0]
    fruit_spawn = True

    highscore = 0
    file = open("snake/score.txt", "r")
    content = file.read()

    x = content.split()
    for i in x:
        if i.isdigit():
            highscore = int(i)
    
    # Game loop
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            keys = pygame.key.get_pressed()

            if (keys[pygame.K_w] or keys[pygame.K_UP]) and direction != 'down':
                direction = 'up'
            if (keys[pygame.K_s] or keys[pygame.K_DOWN]) and direction != 'up':
                direction = 'down'
            if (keys[pygame.K_a] or keys[pygame.K_LEFT]) and direction != 'right':
                direction = 'left'
            if (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and direction != 'left':
                direction = 'right'
        gameScreen.fill((0, 0, 0))

        for square in snake_body:
            pygame.draw.rect(gameScreen, (75, 139, 59), (square[0], square[1], 20, 20))

        # Direction control for the snake
        if direction == 'right':
            snake_pos[0] += 10
        elif direction == 'left':
            snake_pos[0] -= 10
        elif direction == 'up':
            snake_pos[1] -= 10
        elif direction == 'down':
            snake_pos[1] += 10

        snake_body.append(list(snake_pos))

        for square in snake_body[:-1]:
            if pygame.Rect(square[0], square[1], 10, 10).colliderect(pygame.Rect(snake_pos[0], snake_pos[1], 10, 10)):
                game_over(score, highscore)

        # Add random fruit spawn
        if fruit_spawn:
            fruit_pos = [random.randrange(40, WIDTH - 40), random.randrange(40, HEIGHT - 40)]
            fruit_spawn = False
        gameScreen.blit(WATERMELON, (fruit_pos[0], fruit_pos[1], 20, 20))

        # Let snake eat fruit
        if pygame.Rect(snake_pos[0], snake_pos[1], 20, 20).colliderect(pygame.Rect(fruit_pos[0], fruit_pos[1], 25, 25)):
            fruit_spawn = True
            # Number added to score
            score += 10
            # Sound effect when fruit is eaten
            pygame.mixer.Sound.play(fruit_sound)
        else:
            snake_body.pop(0)

        # Score display
        score_font = font.render(f'Score: {score}', True, (75, 139, 59))
        font_pos = score_font.get_rect(center=(WIDTH//2-40, 30))
        gameScreen.blit(score_font, font_pos)

        pygame.display.update()
        
        # Frames per second, increasing/decreasing this number changes the movement speed of the snake
        clock.tick(25)

        # Game over if snake hits window edge
        if snake_pos[0] + 10 <= 0 or snake_pos[0] >= WIDTH:
            game_over(score, highscore)
        if snake_pos[1] + 10 <= 0 or snake_pos[1] >= HEIGHT:
            game_over(score, highscore)


drawLoading()
time.sleep(2)
main_menu()
