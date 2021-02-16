import os
import pygame
from pygame import Rect
from pygame.math import Vector2

os.environ['SDL_VIDEO_CENTERED'] = '1'


class Unit:
    def __init__(self, state, position, tile):
        self.state = state
        self.position = position
        self.tile = tile

    def move(self, moveVector):
        pass


class Tank(Unit):
    def move(self, moveVector):
        # Compute new tank position
        newTankPos = self.position + moveVector

        # Don't allow positions outside the world
        if newTankPos.x < 0 or newTankPos.x >= self.state.worldWidth \
                or newTankPos.y < 0 or newTankPos.y >= self.state.worldHeight:
            return

        # Don't allow tower positions
        for unit in self.state.units:
            if newTankPos == unit.position:
                return

        self.position = newTankPos


class Tower(Unit):
    def move(self, moveVector):
        raise RuntimeError("Towers can't move")


class GameState():
    def __init__(self):
        self.worldSize = Vector2(16, 10)
        self.ground = [
            [Vector2(5, 1), Vector2(5, 1), Vector2(5, 1), Vector2(5, 1), Vector2(5, 1), Vector2(6, 2), Vector2(5, 1),
             Vector2(5, 1), Vector2(5, 1), Vector2(5, 1), Vector2(5, 1), Vector2(5, 1), Vector2(5, 1), Vector2(5, 1),
             Vector2(5, 1), Vector2(5, 1)],
            [Vector2(5, 1), Vector2(5, 1), Vector2(7, 1), Vector2(5, 1), Vector2(5, 1), Vector2(6, 2), Vector2(7, 1),
             Vector2(5, 1), Vector2(5, 1), Vector2(5, 1), Vector2(6, 1), Vector2(5, 1), Vector2(5, 1), Vector2(6, 4),
             Vector2(7, 2), Vector2(7, 2)],
            [Vector2(5, 1), Vector2(6, 1), Vector2(5, 1), Vector2(5, 1), Vector2(6, 1), Vector2(6, 2), Vector2(5, 1),
             Vector2(6, 1), Vector2(6, 1), Vector2(5, 1), Vector2(5, 1), Vector2(5, 1), Vector2(5, 1), Vector2(6, 2),
             Vector2(6, 1), Vector2(5, 1)],
            [Vector2(5, 1), Vector2(5, 1), Vector2(5, 1), Vector2(5, 1), Vector2(6, 1), Vector2(6, 2), Vector2(5, 1),
             Vector2(5, 1), Vector2(5, 1), Vector2(5, 1), Vector2(5, 1), Vector2(5, 1), Vector2(5, 1), Vector2(6, 2),
             Vector2(5, 1), Vector2(7, 1)],
            [Vector2(5, 1), Vector2(7, 1), Vector2(5, 1), Vector2(5, 1), Vector2(5, 1), Vector2(6, 5), Vector2(7, 2),
             Vector2(7, 2), Vector2(7, 2), Vector2(7, 2), Vector2(7, 2), Vector2(7, 2), Vector2(7, 2), Vector2(8, 5),
             Vector2(5, 1), Vector2(5, 1)],
            [Vector2(5, 1), Vector2(5, 1), Vector2(5, 1), Vector2(5, 1), Vector2(6, 1), Vector2(6, 2), Vector2(5, 1),
             Vector2(5, 1), Vector2(5, 1), Vector2(5, 1), Vector2(5, 1), Vector2(5, 1), Vector2(5, 1), Vector2(6, 2),
             Vector2(5, 1), Vector2(7, 1)],
            [Vector2(6, 1), Vector2(5, 1), Vector2(5, 1), Vector2(5, 1), Vector2(5, 1), Vector2(6, 2), Vector2(5, 1),
             Vector2(5, 1), Vector2(7, 1), Vector2(5, 1), Vector2(5, 1), Vector2(5, 1), Vector2(5, 1), Vector2(6, 2),
             Vector2(7, 1), Vector2(5, 1)],
            [Vector2(5, 1), Vector2(5, 1), Vector2(6, 4), Vector2(7, 2), Vector2(7, 2), Vector2(8, 4), Vector2(5, 1),
             Vector2(5, 1), Vector2(5, 1), Vector2(5, 1), Vector2(5, 1), Vector2(5, 1), Vector2(5, 1), Vector2(6, 2),
             Vector2(5, 1), Vector2(5, 1)],
            [Vector2(5, 1), Vector2(5, 1), Vector2(6, 2), Vector2(5, 1), Vector2(5, 1), Vector2(7, 1), Vector2(5, 1),
             Vector2(5, 1), Vector2(6, 1), Vector2(5, 1), Vector2(5, 1), Vector2(5, 1), Vector2(5, 1), Vector2(7, 4),
             Vector2(7, 2), Vector2(7, 2)],
            [Vector2(5, 1), Vector2(5, 1), Vector2(6, 2), Vector2(6, 1), Vector2(5, 1), Vector2(5, 1), Vector2(5, 1),
             Vector2(5, 1), Vector2(5, 1), Vector2(5, 1), Vector2(5, 1), Vector2(5, 1), Vector2(5, 1), Vector2(5, 1),
             Vector2(5, 1), Vector2(5, 1)]
        ]
        self.units = [
            Tank(self, Vector2(5, 4), Vector2(1, 0)),
            Tower(self, Vector2(10, 3), Vector2(0, 1)),
            Tower(self, Vector2(10, 5), Vector2(0, 1))
        ]

    @property
    def worldWidth(self):
        return int(self.worldSize.x)

    @property
    def worldHeight(self):
        return int(self.worldSize.y)

    def update(self, moveTankCommand):
        self.units[0].move(moveTankCommand)


class UserInterface():
    def __init__(self):
        pygame.init()

        # Game state
        self.gameState = GameState()

        # Rendering properties
        self.cellSize = Vector2(64, 64)
        self.unitsTexture = pygame.image.load(os.path.join("./tank_tut/units.png"))
        self.groundTexture = pygame.image.load(os.path.join("./tank_tut/ground.png"))

        # Window
        windowSize = self.gameState.worldSize.elementwise() * self.cellSize
        self.window = pygame.display.set_mode((int(windowSize.x), int(windowSize.y)))
        pygame.display.set_caption("Discover Python & Patterns - https://www.patternsgameprog.com")
        pygame.display.set_icon(pygame.image.load("./tank_tut/icon.png"))
        self.moveTankCommand = Vector2(0, 0)

        # Loop properties
        self.clock = pygame.time.Clock()
        self.running = True

    @property
    def cellWidth(self):
        return int(self.cellSize.x)

    @property
    def cellHeight(self):
        return int(self.cellSize.y)

    def processInput(self):
        self.moveTankCommand = Vector2(0, 0)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                break
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                    break
                elif event.key == pygame.K_RIGHT:
                    self.moveTankCommand.x = 1
                elif event.key == pygame.K_LEFT:
                    self.moveTankCommand.x = -1
                elif event.key == pygame.K_DOWN:
                    self.moveTankCommand.y = 1
                elif event.key == pygame.K_UP:
                    self.moveTankCommand.y = -1

    def update(self):
        self.gameState.update(self.moveTankCommand)

    def renderGround(self, position, tile):
        # Location on screen
        spritePoint = position.elementwise() * self.cellSize

        # Texture
        texturePoint = tile.elementwise() * self.cellSize
        textureRect = Rect(int(texturePoint.x), int(texturePoint.y), self.cellWidth, self.cellHeight)
        self.window.blit(self.groundTexture, spritePoint, textureRect)

    def renderUnit(self, unit):
        # Location on screen
        spritePoint = unit.position.elementwise() * self.cellSize

        # Unit texture
        texturePoint = unit.tile.elementwise() * self.cellSize
        textureRect = Rect(int(texturePoint.x), int(texturePoint.y), self.cellWidth, self.cellHeight)
        self.window.blit(self.unitsTexture, spritePoint, textureRect)

        # Weapon texure
        texturePoint = Vector2(0, 6).elementwise() * self.cellSize
        textureRect = Rect(int(texturePoint.x), int(texturePoint.y), self.cellWidth, self.cellHeight)
        self.window.blit(self.unitsTexture, spritePoint, textureRect)

    def render(self):
        self.window.fill((0, 0, 0))

        # Ground
        for y in range(self.gameState.worldHeight):
            for x in range(self.gameState.worldWidth):
                self.renderGround(Vector2(x, y), self.gameState.ground[y][x])

        # Units
        for unit in self.gameState.units:
            self.renderUnit(unit)

        pygame.display.update()

    def run(self):
        while self.running:
            self.processInput()
            self.update()
            self.render()
            self.clock.tick(60)


userInterface = UserInterface()
userInterface.run()

pygame.quit()
