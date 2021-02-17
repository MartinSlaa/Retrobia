# importing necessary packages
import pygame
import os
import time
import random
from abc import abstractmethod

# initializes the font module in pygame
pygame.font.init()

# Make sure the game starts at the center of screen
os.environ['SDL_VIDEO_CENTERED'] = '1'

# define window size
WIDTH, HEIGHT = 750, 1050
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

# Load images of enemy ships
BOSS_SHIP = pygame.image.load(os.path.join("assets", "boss_ship.png"))
ENEMY_SHIP_1 = pygame.image.load(os.path.join("assets", "enemy_ship1.png"))
ENEMY_SHIP_2 = pygame.image.load(os.path.join("assets", "enemy_ship2.png"))

# load image of player ship
FIGHTER_SHIP = pygame.image.load(os.path.join("assets", "fighter_ship.png"))

# Loading background image
BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join("assets", "blueNebula_1.png")), (WIDTH, HEIGHT))

# Load lasers image
BOLT_LASER_BLUE = pygame.image.load(os.path.join("assets", "blasterbolt.png"))


# class ship abstract method which other ships inherits from
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

    def get_width(self):
        return self.ship_image.get_width()

    def get_height(self):
        return self.ship_image.get_height()


# PLayer class that inherits from the ship class
class PlayerShip(Ship):
    def __init__(self, pos_x, pos_y, health=100):
        super().__init__(pos_x, pos_y, health)
        self.ship_image = FIGHTER_SHIP
        self.bolt_image = BOLT_LASER_BLUE
        self.mask = pygame.mask.from_surface(self.ship_image)
        self.max_health = health


# Enemy class that inherits from the ship class
class Enemy(Ship):
    SHIP_COLOR = {
                  "blue": (ENEMY_SHIP_1, BOLT_LASER_BLUE),
                  "red" : (ENEMY_SHIP_2, BOLT_LASER_BLUE),
                  "green": (BOSS_SHIP, BOLT_LASER_BLUE)
                 }

    def __init__(self, pos_x, pos_y, color, health = 100):
        super().__init__(pos_x, pos_y, health)
        self.ship_image, self.bolt_image = self.SHIP_COLOR[color]
        self.mask = pygame.mask.from_surface(self.ship_image)

    def move(self, velocity):
        self.pos_y += velocity

# main program
def main():
    """"The main method with primary functionality of the application."""

    # declaring variables
    run = True
    fps = 60
    level = 0
    lives = 5
    score = 0
    clock = pygame.time.Clock()

    # declaring the fonts used in the game
    main_font = pygame.font.SysFont("lucidasans", 40)
    lost_font = pygame.font.SysFont("impact", 80)

    # Player variables
    player_velocity = 5
    player = PlayerShip(325, 750)

    # enemy variables
    enemies = []
    wave_length = 0
    enemy_velocity = 2

    # setting lost to false
    lost = False

    # Redraw function to draw UI and lost text
    def redraw_window():
        WIN.blit(BACKGROUND, (0, 0))
        level_label = main_font.render(f"Level: {level}", 1, (255, 255, 255))
        score_label = main_font.render(f"Score: {score}", 1, (255, 255, 255))
        lives_label = main_font.render(f"Lives: {lives}", 1, (255, 255, 255))

        # Placement of lives, level and score on the screen
        WIN.blit(level_label, (5, 1))
        WIN.blit(lives_label, (5, 40))
        WIN.blit(score_label, (WIDTH - level_label.get_width() - 15, 1))

        # draw the player ship on the window
        player.draw(WIN)

        # draw enemies contained in the enemies list
        for enemy in enemies:
            enemy.draw(WIN)

        # Display lost message
        if lost:
            lost_label = lost_font.render("Game Over!", 1, (255, 255, 255))
            WIN.blit(lost_label, (WIDTH/2 - lost_label.get_width()/2, 350))

        # update window
        pygame.display.update()

    # While loop while game is running
    while run:
        clock.tick(fps)

        # Player looses if health is zero or lost all lives
        if lives <= 0 or player.health <= 0:
            lost = True

        # create random waves of enemies and move to next level if player kills all enemies
        if len(enemies) == 0:
            level += 1
            wave_length += 5
            for i in range(wave_length):
                enemy = Enemy(random.randrange(50, WIDTH - 100), random.randrange(- 1500, - 300),
                              random.choice(["red", "blue"]))
                enemies.append(enemy)

        # if player exit game, terminate program by setting run to false
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # defining player movement and that player ship cannot move off screen
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and player.pos_x - player_velocity > 0:  # move left
            player.pos_x -= player_velocity
        if keys[pygame.K_d] and player.pos_x + player_velocity + player.get_width() < WIDTH:  # move right
            player.pos_x += player_velocity
        if keys[pygame.K_w] and player.pos_y - player_velocity > 0:  # move up
            player.pos_y -= player_velocity
        if keys[pygame.K_s] and player.pos_y + player_velocity + player.get_height() < HEIGHT:  # move down
            player.pos_y += player_velocity

        # defining enemy movement
        for enemy in enemies:
            enemy.move(enemy_velocity)
            if enemy.pos_y + enemy.get_height() > HEIGHT:
                lives -= 1
                enemies.remove(enemy)

        redraw_window()

# run program
main()