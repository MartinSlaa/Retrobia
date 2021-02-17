import pygame
import os
import time
import random
from abc import abstractmethod
pygame.font.init()

os.environ['SDL_VIDEO_CENTERED'] = '1'
# define window size
WIDTH, HEIGHT = 750, 850
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

# player ship
FIGHTER_SHIP = pygame.image.load(os.path.join("assets", "fighter_ship.png"))

# Loading background
BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join("assets", "blueNebula_1.png")), (WIDTH, HEIGHT))

# Load lasers
BOLT_LASER_BLUE = pygame.image.load(os.path.join("assets", "blasterbolt.png"))


class Ship:
    def __init__(self, pos_x, pos_y, health=100):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.health = health
        self.ship_image = None
        self.bolt_image = None
        self.bolts = []
        self.cooldown = 0

    def draw(self, window):
        window.blit(self.ship_image, (self.pos_x, self.pos_y))


class PlayerShip(Ship):
    def __init__(self, pos_x, pos_y, health=100):
        super().__init__(pos_x, pos_y, health)
        self.ship_image = FIGHTER_SHIP
        self.bolt_image = BOLT_LASER_BLUE
        self.mask = pygame.mask.from_surface(self.ship_image)
        self.max_health = health
        


# main program
def main():
    run = True
    fps = 60
    level = 1
    score = 0
    clock = pygame.time.Clock()
    main_font = pygame.font.SysFont("comicsans", 60)
    player_velocity = 5
    player = PlayerShip(300, 650)

    def redraw_window():
        WIN.blit(BACKGROUND, (0, 0))
        level_label = main_font.render(f"Level: {level}", 1, (255, 255, 255))
        score_label = main_font.render(f"Score: {score}", 1, (255, 255, 255))

        WIN.blit(level_label, (10, 10))
        WIN.blit(score_label, (WIDTH - level_label.get_width() - 10, 10))
        player.draw(WIN)

        pygame.display.update()

    while run:
        clock.tick(fps)
        redraw_window()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and player.pos_x - player_velocity > 0:  # move left
            player.pos_x -= player_velocity
        if keys[pygame.K_d] and player.pos_x + player_velocity + 50 < WIDTH:  # move right
            player.pos_x += player_velocity
        if keys[pygame.K_w] and player.pos_y - player_velocity > 0:  # move up
            player.pos_y -= player_velocity
        if keys[pygame.K_s] and player.pos_y + player_velocity + 50 < HEIGHT:  # move down
            player.pos_y += player_velocity



main()