import random
import sys
import time
import os
import pygame


pygame.init()

font = pygame.font.SysFont('comicsansms', 30)

# Window size
WIDTH = 500
HEIGHT = 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption('Ssssnake')

# Load and resize assets
WATERMELON = pygame.image.load("snake/assets/Watermelon.png")
#WATERMELON = pygame.image.load(os.path.join("assets", "Watermelon.png"))
WATERMELON = pygame.transform.smoothscale(WATERMELON, (25, 25))


# Menu Function
def main_menu():
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                main()
        WIN.fill((0, 0, 0))

        main_menu_message = font.render('Press anywhere to start the game', True, (75, 139, 59))
        font_pos = main_menu_message.get_rect(center=(WIDTH//2, HEIGHT//2))
        WIN.blit(main_menu_message, font_pos)
        pygame.display.update()


# Game Over Screen
def game_over(score):
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        WIN.fill((0, 0, 0))

        game_over_message = font.render('You Lost', True, (255, 0, 0))
        game_over_score = font.render(f'Your score was {score}', True, (255, 255, 255))
        font_pos_message = game_over_message.get_rect(center=(WIDTH//2, HEIGHT//2))
        font_pos_score = game_over_score.get_rect(center=(WIDTH//2, HEIGHT//2+40))
        WIN.blit(game_over_message, font_pos_message)
        WIN.blit(game_over_score, font_pos_score)
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
        WIN.fill((0, 0, 0))

        for square in snake_body:
            pygame.draw.rect(WIN, (75, 139, 59), (square[0], square[1], 20, 20))

        # Snake direction control
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
                game_over(score)

        # Add random fruit spawn
        if fruit_spawn:
            fruit_pos = [random.randrange(40, WIDTH - 40), random.randrange(40, HEIGHT - 40)]
            fruit_spawn = False
        WIN.blit(WATERMELON, (fruit_pos[0], fruit_pos[1], 20, 20))

        # Let snake eat fruit
        if pygame.Rect(snake_pos[0], snake_pos[1], 20, 20).colliderect(pygame.Rect(fruit_pos[0], fruit_pos[1], 25, 25)):
            fruit_spawn = True
            score += 5
        else:
            snake_body.pop(0)

        # Score display
        score_font = font.render(f'Score: {score}', True, (75, 139, 59))
        font_pos = score_font.get_rect(center=(WIDTH//2-40, 30))
        WIN.blit(score_font, font_pos)

        pygame.display.update()

        clock.tick(25)

        # Exit game if snake hits window edge
        if snake_pos[0] + 10 <= 0 or snake_pos[0] >= WIDTH:
            game_over(score)
        if snake_pos[1] + 10 <= 0 or snake_pos[1] >= HEIGHT:
            game_over(score)


main_menu()
