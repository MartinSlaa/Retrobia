import pygame
import os
import time
import random
pygame.font.init()

# define window size
WIDTH, HEIGHT = 750, 750
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

# player ship
FIGHTER_SHIP = pygame.image.load(os.path.join("assets", "fighter_ship.png"))

# Loading background
BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join("assets", "blueNebula_1.png")), (WIDTH, HEIGHT))

# Load lasers
BOLT_LASER_BLUE = pygame.image.load(os.path.join("assets", "blasterbolt.png"))


# main program
def main():
    run = True
    fps = 60
    level = 1
    score = 0
    clock = pygame.time.Clock()
    main_font = pygame.font.SysFont("comicsans", 60)

    def redraw_window():
        WIN.blit(BACKGROUND, (0, 0))
        level_label = main_font.render(f"Level: {level}", 1, (255, 255, 255))
        score_label = main_font.render(f"Score: {score}", 1, (255, 255, 255))

        WIN.blit(level_label, (10, 10))
        WIN.blit(score_label, (WIDTH - level_label.get_width() - 10, 10))

        pygame.display.update()

    while run:
        clock.tick(fps)
        redraw_window()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


main()