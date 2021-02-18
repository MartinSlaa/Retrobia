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


class Ship:
    """abstract class which other ships inherits from"""

    COOLDOWN = 15

    def __init__(self, pos_x, pos_y, health=100):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.health = health
        self.ship_image = None
        self.bolt_image = None
        self.bolts = []
        self.cooldown = 0

    def draw(self, window):
        window.blit(self.ship_image, (self.pos_x , self.pos_y))
        for bolt in self.bolts:
            bolt.draw(window)

    def get_width(self):
        return self.ship_image.get_width()

    def get_height(self):
        return self.ship_image.get_height()

    def shoot(self):
        if self.cooldown == 0:
            bolt = Bolt(self.pos_x + 39, self.pos_y, self.bolt_image)
            self.bolts.append(bolt)
            self.cooldown = 1

    def cooldowns(self):
        if self.cooldown >= self.COOLDOWN:
            self.cooldown = 0
        elif self.cooldown > 0:
            self.cooldown += 1

    def move_bolts(self, velocity, obj):
        self.cooldowns()
        for bolt in self.bolts:
            bolt.move(velocity)
            if bolt.off_screen(HEIGHT):
                self.bolts.remove(bolt)
            elif bolt.collision(obj):
                obj.health -= 10
                self.bolts.remove(bolt)


# PLayer class that inherits from the ship class
class PlayerShip(Ship):
    def __init__(self, pos_x, pos_y, health=100):
        super().__init__(pos_x, pos_y, health)
        self.ship_image = FIGHTER_SHIP
        self.bolt_image = BOLT_LASER_BLUE
        self.mask = pygame.mask.from_surface(self.ship_image)
        self.max_health = health

    def move_bolts(self, velocity, objs):
        self.cooldowns()
        for bolt in self.bolts:
            bolt.move(velocity)
            if bolt.off_screen(HEIGHT):
                self.bolts.remove(bolt)
            else:
                for obj in objs:
                    if bolt.collision(obj):
                        objs.remove(obj)
                        if bolt in self.bolts:
                            self.bolts.remove(bolt)

    def draw(self, window):
        super().draw(window)
        self.health_bar(window)

    def health_bar(self, window):
        pygame.draw.rect(window, (255, 0, 0), (self.pos_x, self.pos_y + self.ship_image.get_height(),
                                               self.ship_image.get_width(), 10))
        pygame.draw.rect(window, (0, 255, 0), (self.pos_x, self.pos_y + self.ship_image.get_height(),
                                               self.ship_image.get_width() * (self.health / self.max_health), 10))


# Enemy class that inherits from the ship class
class Enemy(Ship):
    SHIP_COLOR = {
        "blue": (ENEMY_SHIP_1, BOLT_LASER_BLUE),
        "red": (ENEMY_SHIP_2, BOLT_LASER_BLUE),
        "green": (BOSS_SHIP, BOLT_LASER_BLUE)
    }

    def __init__(self, pos_x, pos_y, color, health=100):
        super().__init__(pos_x, pos_y, health)
        self.ship_image, self.bolt_image = self.SHIP_COLOR[color]
        self.mask = pygame.mask.from_surface(self.ship_image)

    def shoot(self):
        if self.cooldown == 0:
            bolt = Bolt(self.pos_x + 80, self.pos_y + 300, self.bolt_image)
            self.bolts.append(bolt)
            self.cooldown = 1

    def move(self, velocity):
        self.pos_y += velocity


class Bolt:
    """All blots uses these functions"""
    def __init__(self, pos_x, pos_y, image):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.image = image
        self.mask = pygame.mask.from_surface(self.image)

    def draw(self, window):
        window.blit(self.image, (self.pos_x, self.pos_y))

    def move(self, velocity):
        self.pos_y += velocity

    def off_screen(self, height):
        return not height >= self.pos_y >= 0

    def collision(self, box):
        return collide(box, self)


def collide(obj1, obj2):
    offset_x = obj2.pos_x - obj1.pos_x
    offset_y = obj2.pos_y - obj1.pos_y
    return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) is not None


# main program
def main():
    """"The main method with primary functionality of the application."""

    # declaring variables
    run = True
    fps = 60
    level = 0
    lives = 5
    score = -100
    clock = pygame.time.Clock()

    # declaring the fonts used in the game
    main_font = pygame.font.SysFont("lucidasans", 40)
    lost_font = pygame.font.SysFont("impact", 80)

    # bolt variables
    bolt_velocity = 10

    # Player variables
    player_velocity = 10
    player = PlayerShip(325, 750)

    # enemy variables
    enemies = []
    wave_length = 0
    enemy_velocity = 2

    # setting lost to false
    lost = False
    lost_count = 0

    # Redraw function to draw UI and lost text
    def redraw_window():
        WIN.blit(BACKGROUND, (0, 0))
        level_label = main_font.render(f"Level: {level}", 1, (255, 255, 255))
        score_label = main_font.render(f"Score: {score}", 1, (255, 255, 255))
        lives_label = main_font.render(f"Lives: {lives}", 1, (255, 255, 255))

        # Placement of lives, level and score on the screen
        WIN.blit(level_label, (5, 1))
        WIN.blit(lives_label, (5, 40))
        WIN.blit(score_label, (WIDTH - level_label.get_width() - 75, 1))

        # draw the player ship on the window
        player.draw(WIN)

        # draw enemies contained in the enemies list
        for enemy in enemies:
            enemy.draw(WIN)

        # Display lost message
        if lost:
            lost_label = lost_font.render("Game Over!", 1, (255, 255, 255))
            WIN.blit(lost_label, (200, 350))

        # update window
        pygame.display.update()

    # While loop while game is running
    while run:
        clock.tick(fps)
        redraw_window()

        # Player looses if health is zero or lost all lives
        if lives <= 0 or player.health <= 0:
            lost = True
            lost_count += 1

        # used to define how long lost screen is showed
        if lost:
            if lost_count > fps * 3:
                run = False
            else:
                continue

        # create random waves of enemies and move to next level if player kills all enemies
        if len(enemies) == 0:
            level += 1
            score += 100
            wave_length += 3
            for i in range(wave_length):
                enemy = Enemy(random.randrange(500, WIDTH - 200), random.randrange(- 1500, - 200),
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
        if keys[pygame.K_s] and player.pos_y + player_velocity + player.get_height() + 10 < HEIGHT:  # move down
            player.pos_y += player_velocity
        if keys[pygame.K_SPACE]:  # player shoots bolt
            player.shoot()

        # defining enemy movement
        for enemy in enemies:
            enemy.move(enemy_velocity)
            enemy.move_bolts(bolt_velocity, player)

            # random timer for enemies to shoot
            if random.randrange(0, 120) == 1:
                enemy.shoot()

            # define what happens when player and enemy ship collides. player looses 10 health
            if collide(enemy, player):
                player.health -= 10
                enemies.remove(enemy)

            # If enemies get to the bottom of screen, lose 1 life and remove enemy ship
            if enemy.pos_y + enemy.get_height() > HEIGHT:
                lives -= 1
                enemies.remove(enemy)

        # check if player bolts hits an enemy and removes bolt and enemy
        player.move_bolts(-bolt_velocity, enemies)


def menu():
    title_font = pygame.font.SysFont("comicsans", 90)
    high_score_font = pygame.font.SysFont("comicsans", 60)
    run = True
    while run:
        # show menu
        WIN.blit(BACKGROUND, (0, 0))
        title_label = title_font.render("Press space to begin!", 1, (255, 255, 255))
        WIN.blit(title_label, (60, 200))

        high_score_label = high_score_font.render("Press mouse to show high scores", 1, (255, 255, 255))
        WIN.blit(high_score_label, (50, 350))

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                main()

    pygame.quit()


# run program
menu()
