import pygame
import sys
import os
import numpy

# Initialize pygame
pygame.init()

# Screen width and height
WIDTH = 600
HEIGHT = 800

# Colors
FONTCOLOR = (192, 192, 192)
WINLINECOLOR = (255, 102, 102)
BGCOLOR = (32, 32, 32)
BOARDLINECOLOR = (64, 64, 64)

# Fonts
FONT1 = pygame.font.SysFont(None, 60)
FONT2 = pygame.font.SysFont(None, 30)

# Load and resize assets
X = pygame.image.load("tictactoe/assets/x.png")
#X = pygame.image.load(os.path.join("assets", "x.png"))
X = pygame.transform.smoothscale(X, (175, 175))
O = pygame.image.load("tictactoe/assets/o.png")
#O = pygame.image.load(os.path.join("assets", "o.png"))
O = pygame.transform.smoothscale(O, (175, 175))

# Create game screen
pygame.display.set_caption("Retrobia TicTacToe")
gameScreen = pygame.display.set_mode((WIDTH, HEIGHT))

# Board
board = numpy.zeros((3, 3))

# Score
xScore = 0
oScore = 0

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

    drawScore(xScore, oScore)

    pygame.display.update()

# Draw player moves
def drawMove():
    drawBoard()

    for boardRow in range(len(board)):
        for boardCol in range(len(board[boardRow])):
            if(board[boardRow][boardCol] == 1):
                gameScreen.blit(X, (boardCol * 200 + 17, boardRow * 200 + 17))
            elif(board[boardRow][boardCol] == 2):
                gameScreen.blit(O, (boardCol * 200 + 17, boardRow * 200 + 17))
                
    pygame.display.update()

# Draw scoreboard
def drawScore(xScore, oScore):
    pygame.draw.rect(gameScreen, BOARDLINECOLOR, (0,601,600,15))

    textString = str(xScore) + " - " + str(oScore)
    text = FONT1.render(textString, True, FONTCOLOR)
    gameScreen.blit(text, (250, 680))

    xScoreAsset = pygame.transform.smoothscale(X, (100, 100))
    oScoreAsset = pygame.transform.smoothscale(O, (100, 100))

    gameScreen.blit(xScoreAsset, (100, 650))
    gameScreen.blit(oScoreAsset, (400, 650))

    pygame.display.update()

# Draw win screen
def drawWinScreen(player):
    gameScreen.fill(BGCOLOR)
    pygame.draw.rect(gameScreen, BOARDLINECOLOR, (0,601,600,15))

    if(player == 1):
        gameScreen.blit(X, (125, 200))
    elif(player == 2):
        gameScreen.blit(O, (125, 200))

    text = FONT1.render("Wins!", True, FONTCOLOR)
    gameScreen.blit(text, (325, 270))

    text = FONT2.render("Press 'R' to restart", True, FONTCOLOR)
    gameScreen.blit(text, (225, 400))

    drawScore(xScore, oScore)

    pygame.display.update()

# Draw drawn screen
def drawDrawScreen():
    gameScreen.fill(BGCOLOR)
    pygame.draw.rect(gameScreen, BOARDLINECOLOR, (0,601,600,15))

    text = FONT1.render("Draw!", True, FONTCOLOR)
    gameScreen.blit(text, (255, 270))

    text = FONT2.render("Press 'R' to restart", True, FONTCOLOR)
    gameScreen.blit(text, (225, 400))

    drawScore(xScore, oScore)

    pygame.display.update()

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

# Check winner
def checkWin(player):
    # Row win
    for boardRow in (range(len(board))):
        if((board[boardRow][0] == player) and (board[boardRow][1] == player) and (board[boardRow][2] == player)):
            return True

    # Column win
    for boardCol in (range(len(board[0]))):
        if((board[0][boardCol] == player) and (board[1][boardCol] == player) and (board[2][boardCol] == player)):
            return True

    # Ascending diagonal win
    if((board[2][0] == player) and (board[1][1] == player) and (board [0][2] == player)):
        return True

    # Descending diagonal win
    if((board[0][0] == player) and (board[1][1] == player) and (board [2][2] == player)):
        return True

    return False

# Restart game
def restartGame():
    drawBoard()

    for boardRow in range(len(board)):
        for boardCol in range(len(board[boardRow])):
            board[boardRow][boardCol] = 0

    return 1

# Main game loop function
def main():
    # Player
    player = 1

    global xScore, oScore

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

                if (isBoardFull() == False):
                    if isBoxEmpty(boxRowClick, boxColClick):
                        if(player == 1):
                            insertMove(boxRowClick, boxColClick, player)
                            drawMove()
                            if(checkWin(player)):
                                xScore = xScore + 1
                                drawWinScreen(player)
                                pygame.event.set_blocked(1025)     
                            player = 2
                        elif(player == 2):
                            insertMove(boxRowClick, boxColClick, player)
                            drawMove()
                            if(checkWin(player)):
                                oScore = oScore + 1
                                drawWinScreen(player)
                                pygame.event.set_blocked(1025)
                            player = 1
        
            # Restart game on keypress 'R'
            if(event.type == pygame.KEYDOWN):
                if(event.key == pygame.K_r):
                    pygame.event.set_allowed(1025)
                    player = restartGame()
                
        # Draws draw screen if board is full
        if (isBoardFull() == True):
            pygame.event.set_blocked(1025)
            drawDrawScreen()

main()