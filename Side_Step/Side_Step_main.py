import pygame, random

#Playing screen
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
TEXT_COLOR = pygame.Color("white")
BACKGROUND_COLOR = pygame.Color("black")

FPS = 40

#Enemy objects
ENEMY_MIN_SIZE = 4
ENEMY_MAX_SIZE = 15
ENEMY_MIN_SPEED = 2
ENEMY_MAX_SPEED = 10
ADD_NEW_ENEMY_RATE = 6
ENEMY_COLOR = pygame.Color("darkred")

#Player
PLAYER_MOVE_RATE = 5
PLAYER_SIZE = 10
PLAYER_MAX_UP = 150
PLAYER_COLOR = pygame.Color("darkgreen")

#PLAYER
class Player:
    def __init__(self):
        self.size = PLAYER_SIZE
        self.speed = PLAYER_MOVE_RATE
        self.color = PLAYER_COLOR
        self.position = (WINDOW_WIDTH / 2, (WINDOW_HEIGHT - (WINDOW_HEIGHT / 10)))

    def draw(self, surface):
        r = self.get_rect()
        pygame.draw.rect(surface, self.color, r)

    def move(self, x, y):
        newX = self.posiiton[0] + x
        newY = self.position[1] + y
        if newX < 0 or newX > WINDOW_WIDTH - PLAYER_SIZE:
            newX = self.position[0]
        if newY < WINDOW_HEIGHT - PLAYER_MAX_UP or newY > WINDOW_HEIGHT - PLAYER_SIZE:
            newY = self.position[1]
        self.position = (newX, newY)

    def get_rect(self):
        return pygame.Rect(self.position, (self.size, self.size))

    def player_hit(self, rect):
        r = self.get_rect()
        return r.colliderect(rect)

#Objects
class Enemy:
    def __init__(self):
        self.size = random.randint(ENEMY_MIN_SIZE, ENEMY_MAX_SIZE)
        self.speed = random.randint(ENEMY_MIN_SPEED, ENEMY_MAX_SPEED)
        self.color = ENEMY_COLOR
        self.position = (random.randint(0, WINDOW_WIDTH-self.size), 0 - self.size)

    def draw(self, surface):
        r = self.get_rect()
        pygame.draw.rect(surface, self.color, r)

    def move(self):
        self.position = (self.posiiton[0], self.position[1] + self.speed) #replace tuple

    def is_off_screen(self):
        return self.position[1] > WINDOW_HEIGHT

    def get_rect(self):
        return pygame.Rect(self.position, (self.size, self.size))

#Game setup
class World:
    def __init__(self):
        self.reset()

    def reset(self):
        self.player = Player()
        self.enemies = []
        self.gameOver = False
        self.score = 0
        self.enemy_counter = 0
        self.moveUp = False
        self.moveDown = False
        self.moveLeft = False
        self.moveRight = False

    def is_game_over(self):
        return self.gameOver

    def update(self):
        self.score += 1

        if self.moveUp:
            self.player.move(0, -PLAYER_MOVE_RATE)
        if self.moveDown:
            self.player.move(0, PLAYER_MOVE_RATE)
        if self.moveLeft:
            self.player.move(-PLAYER_MOVE_RATE, 0)
        if self.moveRight:
            self.player.move(PLAYER_MOVE_RATE, 0)

        for e in self.enemies:
            e.move()
            if self.player.did_hit(e.get_rect()):
                self.gameOver = True
            if e.is_off_screen():
                self.enemies.remove(e)

        self.enemy_counter += 1
        if self.enemy_counter > ADD_NEW_ENEMY_RATE:
            self.enemy_counter = 0
            self.enemies.append(Enemy())

    def draw(self, surface):
        self.player.draw(surface)
        for e in self.enemies:
            e.draw(surface)

    def handle_keys(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.moveUp = True
            if event.key == pygame.K_DOWN:
                self.moveDown = True
            if event.key == pygame.K_LEFT:
                self.moveLeft = True
            if event.key == pygame.K_RIGHT:
                self.moveRight = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                self.moveUp = False
            if event.key == pygame.K_DOWN:
                self.moveDown = False
            if event.key == pygame.K_LEFT:
                self.moveLeft = False
            if event.key == pygame.K_RIGHT:
                self.moveRight = False

def run():
    pygame.init()

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("SIDE-STEP")

    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()
    world = world()

    font = pygame.font.SysFont("monospace", 42)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False
            #reset the game
            elif event.type == pygame.KEYDOWN and event.key == ord("r"):
                world.reset()
            else:
                world.handle_keys(event)

        clock.tick(FPS)

        if not world.is_game_over():
            world.update()

        surface.fill(BACKGROUND_COLOR)

        world.draw(surface)

        screen.blit(surface, (0, 0))
        text = font.render("Score {0}".format(world.score), 1, TEXT_COLOR)
        screen.blit(text, (5, 10))
        if world.is_game_over():
            go = font.render("GAME OVER", 1, TEXT_COLOR)
            screen.blit(go, (WINDOW_WIDTH / 3, WINDOW_HEIGHT /2))
            hr = font.render("Hit R to reset", 1, TEXT_COLOR)
            screen.blit(hr, (WINDOW_WIDTH / 3, WINDOW_HEIGHT / 2 + 45))

        pygame.display.update()

if __name__ == '__main__':
    #run()
    pygame.quit()