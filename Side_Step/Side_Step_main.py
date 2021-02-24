import pygame, random

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600

FPS = 40

OBJECT_SPAWN_RATE = 2
OBJECT_MIN_SIZE = 4
OBJECT_MAX_SIZE = 15
OBJECT_MIN_SPEED = 2
OBJECT_MAX_SPEED = 10

PLAYER_SPEED = 5
PLAYER_SIZE = 10
PLAYER_MAX_UP = 150

BC_COLOR = pygame.Color("black")
TEXT_COLOR = pygame.Color("white")
OBJECT_COLOR = pygame.Color("darkred")
PLAYER_COLOR = pygame.Color("darkgreen")

#PLAYER
class Player:
    def __init__(self):
        self.size = PLAYER_SIZE
        self.speed = PLAYER_SPEED
        self.color = PLAYER_COLOR
        self.position = (WINDOW_WIDTH / 2, (WINDOW_HEIGHT -(WINDOW_HEIGHT /10)))

    def draw(self, surface):
        r = self.get_rect()
        pygame.draw.rect(surface, self.color, r)

    def move(self, x, y):
        newX = self.position[0] + x
        newY = self.position[1] + y
        if newX < 0 or newX > WINDOW_WIDTH - PLAYER_SIZE:
            newX = self.position[0]
        if newY < WINDOW_HEIGHT - PLAYER_MAX_UP or  newY > WINDOW_HEIGHT - PLAYER_SIZE:
            newY = self.position[1]
        self.position = (newX, newY)

    def get_rect(self):
        return pygame.Rect(self.position, (self.size, self.size))

    def did_hit(self, rect):
        r = self.get_rect()
        return r.colliderect(rect)

#FALLING OBJECTS
class Object:
    def __init__(self):
        self.size = random.randint(OBJECT_MIN_SIZE, OBJECT_MAX_SIZE)
        self.speed = random.randint(OBJECT_MIN_SPEED, OBJECT_MAX_SPEED)
        self.color = OBJECT_COLOR
        self.position = (random.randint(0, WINDOW_WIDTH-self.size), 0 - self.size)

    def draw(self, surface):
        r = self.get_rect()
        pygame.draw.rect(surface, self.color, r)

    def move(self):
        self.position = (self.position[0], self.position[1] + self.speed)

    def is_off_screen(self):
        return self.position[1] > WINDOW_HEIGHT

    def get_rect(self):
        return pygame.Rect(self.position, (self.size, self.size))

#GAME STATE
class World:
    def __init__(self):
        self.reset()

    def reset(self):
        self.player = Player()
        self.objects = []
        self.gameOver = False
        self.score = 0
        self.object_counter = 0
        self.moveUp = False
        self.moveDown = False
        self.moveLeft = False
        self.moveRight = False

    def is_game_over(self):
        return self.gameOver

    def update(self):
        self.score += 1

        if self.moveUp:
            self.player.move(0, -PLAYER_SPEED)
        if self.moveDown:
            self.player.move(0, PLAYER_SPEED)
        if self.moveLeft:
            self.player.move(0, -PLAYER_SPEED)
        if self.moveRight:
            self.player.move(0, PLAYER_SPEED)

        for o in self.objects:
            o.move()
            if self.player.did_hit(o.get_rect()):
               self.gameOver = True
            if o.is_off_screen():
                self.objects.remove(o)

        self.object_counter += 1
        if self.object_counter > OBJECT_SPAWN_RATE:
            self.object_counter = 0
            self.objects.append(Object())

    def draw(self, surface):
        self.player.draw(surface)
        for o in self.objects:
            o.draw(surface)

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
    pygame.display.set_caption("Side-Step")

    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()

    world = World()

    font = pygame.font.SysFont("moonspace", 42)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == ord("r"):
                world.reset()
            else:
                world.handle_keys(event)

    clock.tick(FPS)

    if not world.is_game_over():
        world.update()

    surface.fill(BC_COLOR)

    world.draw(surface)

    screen.blit(surface, (0, 0))
    text = font.render("Score {0}".format(world.score), 1, TEXT_COLOR)
    screen.blit(text, (5, 10))
    if world.is_game_over():
        go = font.render("GAME OVER", 1, TEXT_COLOR)
        screen.blit(go, (WINDOW_WIDTH / 3, WINDOW_HEIGHT / 2))
        hr = font.render("HIT THE R KEY TO RESET", 1, TEXT_COLOR)
        screen.blit(hr, (WINDOW_WIDTH / 3, WINDOW_HEIGHT / 2 +45))

    pygame.display.update()



if __name__ == '__main__':
    run()
    pygame.quit()