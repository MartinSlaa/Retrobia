import sys, random
import pygame

pygame.init()

# Window size
WIDTH = 750
HEIGHT = 850
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption('Ssssnake')

# Main Function
def main():
    clock = pygame.time.Clock()
    snake_pos = [200,70]
    snake_body = [[200,70], [200-10,70], [200-(2*10),70]]
    direction = 'right'
    score = 0
    fruit_pos = [0,0]
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
        WIN.fill((0,0,0))

        for square in snake_body:
            pygame.draw.rect(WIN, (255,255,0), (square[0], square[1],10,10))

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

        if pygame.Rect(snake_pos[0], snake_pos[1], 10, 10).colliderect(pygame.Rect(fruit_pos[0], fruit_pos[1], 10, 10)):
            fruit_spawn = True
            score += 5
        else:
            snake_body.pop(0)

        for square in snake_body[:-1]:
            if pygame.Rect(square[0], square[1], 10, 10).colliderect(pygame.Rect(snake_pos[0], snake_pos[1], 10, 10)):
                sys.exit()

        # Add random fruit spawn
        if fruit_spawn:
            fruit_pos = [random.randrange(40, WIDTH-40), random.randrange(40, HEIGHT-40)]
            fruit_spawn = False
        pygame.draw.rect(WIN,(138,43,226), (fruit_pos[0], fruit_pos[1], 10, 10))

        # Let snake eat fruit
        if pygame.Rect(snake_pos[0], snake_pos[1],10,10). colliderect(pygame.Rect(fruit_pos[0],fruit_pos[1],10,10)):
            fruit_spawn = True
            score += 5
        pygame.display.update()
        clock.tick(25)

        # Exit game if snake hits window edge
        if snake_pos[0]+10 <=0 or snake_pos[0] >= WIDTH:
            sys.exit()
        if snake_pos[1]+10 <=0 or snake_pos[1] >= HEIGHT:
            sys.exit()
main()