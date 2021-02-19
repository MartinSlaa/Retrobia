import pygame
import sys
import numpy

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

# Get assets
O = pygame.image.load("tictactoe/assets/o.png")
X = pygame.image.load("tictactoe/assets/x.png")

# Create game screen
pygame.display.set_caption("Retrobia TicTacToe")
gameScreen = pygame.display.set_mode((WIDTH, HEIGHT))

# Board
board = numpy.zeros((3, 3))

# Draw board
def drawBoard():
    #  Background
    gameScreen.fill(BGCOLOR)
    
    # Horizontal
    pygame.draw.line(gameScreen, BOARDLINECOLOR, (0, 200), (600, 200), 15)
    pygame.draw.line(gameScreen, BOARDLINECOLOR, (0, 400), (600, 400), 15)

    # Vertical
    pygame.draw.line(gameScreen, BOARDLINECOLOR, (200, 0), (200, 600), 15)
    pygame.draw.line(gameScreen, BOARDLINECOLOR, (400, 0), (400, 600), 15)

# Draw player moves
def drawMove():
    for boardRow in range(len(board)):
        for boardCol in range(len(board[boardRow])):
            if(board[boardRow][boardCol] == 1):
                
                #pygame.draw.circle(gameScreen, OCOLOR, [int(boardCol * 200 + 100), int(boardRow * 200 + 100)], 60, 15)
            elif(board[boardRow][boardCol] == 2):
                #pygame.draw.line(gameScreen, XCOLOR, (boardCol * 200 + 55, boardRow * 200 + 200 - 55), (boardCol * 200 + 200 - 55, boardRow * 200 - 55), 55)

# Function for filling the game board (player move)
def insertMove(boardRow, boardCol, player):
    board[boardRow][boardCol] = player

# Function that checks if box is empty (legal or illigal move)
def isBoxEmpty(boardRow, boardCol):
    if(board[boardRow][boardCol] == 0):
        return True
    else:
        return False

# Funtion that checks if board is full (game over)
def isBoardFull():
    for boardRow in range(len(board)):
        for boardCol in range(len(board[boardRow])):
            if(board[boardRow][boardCol] == 0):
                return False
    
    return True

# Main game loop function
def main():
    # Player
    player = 1

    drawBoard()

    # Game loop
    while(True):
        for event in pygame.event.get():
            # Exit game
            if(event.type == pygame.QUIT):
                sys.exit()

            # Move on mouseclick
            if(event.type == pygame.MOUSEBUTTONDOWN):
                mouseClickX = event.pos[0]
                mouseClickY = event.pos[1]

                boxRowClick = int(mouseClickY // 200)
                boxColClick = int(mouseClickX // 200)

                if isBoxEmpty(boxRowClick, boxColClick):
                    if(player == 1):
                        insertMove(boxRowClick, boxColClick, player)
                        player = 2
                    else:
                        insertMove(boxRowClick, boxColClick, player)
                        player = 1

                drawMove()

        pygame.display.update()

main()