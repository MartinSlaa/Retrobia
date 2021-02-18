import pygame
import sys

# Screen width and height
WIDTH = 600
HEIGHT = 600

# Colors
XCOLOR = (102, 178, 255)
OCOLOR = (178, 102, 255)
WINLINECOLOR = (255, 102, 102)
BGCOLOR = (64, 64, 64)
BOARDLINECOLOR = (32, 32, 32)

# Initialize pygame
pygame.init()

# Create game screen
gameScreen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Retrobia TicTacToe")

# Background
gameScreen.fill(BGCOLOR)

# Board lines
def createBoard():
    # Horizontal
    pygame.draw.line(gameScreen, BOARDLINECOLOR, (0, 200), (600, 200), 15)
    pygame.draw.line(gameScreen, BOARDLINECOLOR, (0, 400), (600, 400), 15)

    # Vertical
    pygame.draw.line(gameScreen, BOARDLINECOLOR, (200, 0), (200, 600), 15)
    pygame.draw.line(gameScreen, BOARDLINECOLOR, (400, 0), (400, 600), 15)

# Main game loop function
def main():
    createBoard()

    while(True):
        for i in pygame.event.get():
            if(i.type == pygame.QUIT):
                sys.exit()

        pygame.display.update()

main()