import pygame
import os
import time
import numpy

# Initialize pygame
pygame.init()

# Screen width and height
WIDTH = 600
HEIGHT = 800

# Centers screen
os.environ['SDL_VIDEO_CENTERED'] = '1'

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
#X = pygame.image.load(os.path.join("tictactoe/assets", "x.png"))
X = pygame.transform.smoothscale(X, (175, 175))
O = pygame.image.load("tictactoe/assets/o.png")
#O = pygame.image.load(os.path.join("tictactoe/assets", "o.png"))
O = pygame.transform.smoothscale(O, (175, 175))
LOGO = pygame.image.load("tictactoe/assets/logo.png")
#LOGO = pygame.image.load(os.path.join("tictactoe/assets", "logo.png"))

# Game screen
pygame.display.set_caption("Retrobia TicTacToe")
gameScreen = pygame.display.set_mode((WIDTH, HEIGHT))

# Board
board = numpy.zeros((3, 3))

# Score
xScore = 0
oScore = 0

# Draw loading screen
def drawLoading():
    # Fill background
    gameScreen.fill(BGCOLOR)

    # Display logo
    gameScreen.blit(LOGO, (200, 200))

    # Display text
    textString = "Loading..."
    text = FONT1.render(textString, True, FONTCOLOR)
    gameScreen.blit(text, (210, 600))

    # Update game screen
    pygame.display.update()

# Draw board
def drawBoard():
    # Fill background
    gameScreen.fill(BGCOLOR)

    # Fill horizontal
    pygame.draw.line(gameScreen, BOARDLINECOLOR, (0, 200), (600, 200), 15)
    pygame.draw.line(gameScreen, BOARDLINECOLOR, (0, 400), (600, 400), 15)

    # Fill vertical
    pygame.draw.line(gameScreen, BOARDLINECOLOR, (200, 0), (200, 600), 15)
    pygame.draw.line(gameScreen, BOARDLINECOLOR, (400, 0), (400, 600), 15)

    drawScore(xScore, oScore)

    # Update game screen
    pygame.display.update()

# Draw player moves
def drawMove():
    drawBoard()

    # Display player asset based on the board 
    for boardRow in range(len(board)):
        for boardCol in range(len(board[boardRow])):
            if(board[boardRow][boardCol] == 1):
                gameScreen.blit(X, (boardCol * 200 + 17, boardRow * 200 + 17))
            elif(board[boardRow][boardCol] == 2):
                gameScreen.blit(O, (boardCol * 200 + 17, boardRow * 200 + 17))

    # Update game screen                
    pygame.display.update()

# Draw scoreboard
def drawScore(xScore, oScore):
    # Fill rectangle
    pygame.draw.rect(gameScreen, BOARDLINECOLOR, (0,601,600,15))

    # Temp variables for scores
    xScoreStr = "00" 
    oScoreStr = "00"

    # X score must have 2 characters
    if(xScore < 10):
        xScoreStr = "0" + str(xScore)
    elif(xScore > 99):
        xScoreStr = "99"
    else:
        xScoreStr = str(xScore)
    
    # O score must have 2 characters
    if(oScore < 10):
        oScoreStr = "0" + str(oScore)
    elif(oScore > 99):
        oScoreStr = "99"
    else:
        oScoreStr = str(oScore)

    # Display scoreboard score text
    textString = xScoreStr + " - " + oScoreStr
    text = FONT1.render(textString, True, FONTCOLOR)
    gameScreen.blit(text, (235, 680))

    # Display player asset for scoreboard 
    xScoreAsset = pygame.transform.smoothscale(X, (100, 100))
    gameScreen.blit(xScoreAsset, (100, 650))
    oScoreAsset = pygame.transform.smoothscale(O, (100, 100))
    gameScreen.blit(oScoreAsset, (400, 650))

    # Update game screen
    pygame.display.update()

# Draw win screen
def drawWinScreen(player):
    # Fill background
    gameScreen.fill(BGCOLOR)

    # Display winner game asset
    if(player == 1):
        gameScreen.blit(X, (125, 200))
    elif(player == 2):
        gameScreen.blit(O, (125, 200))

    # Display text
    text = FONT1.render("Wins!", True, FONTCOLOR)
    gameScreen.blit(text, (325, 270))

    # Display text
    text = FONT2.render("Press 'R' to restart", True, FONTCOLOR)
    gameScreen.blit(text, (225, 400))

    drawScore(xScore, oScore)

    # Update game screen
    pygame.display.update()

# Draw draw screen
def drawDrawScreen():
    # Fill background
    gameScreen.fill(BGCOLOR)

    # Display text
    text = FONT1.render("Draw!", True, FONTCOLOR)
    gameScreen.blit(text, (255, 270))

    # Display text
    text = FONT2.render("Press 'R' to restart", True, FONTCOLOR)
    gameScreen.blit(text, (225, 400))

    drawScore(xScore, oScore)

    # Update game screen
    pygame.display.update()

# Filling the game board (player move)
def insertMove(boardRow, boardCol, player):
    board[boardRow][boardCol] = player

# Checks if box is empty (legal or illigal move)
def isBoxEmpty(boardRow, boardCol):
    if(board[boardRow][boardCol] == 0):
        return True
    else:
        return False

# Checks if board is full (draw)
def isBoardFull():
    for boardRow in range(len(board)):
        for boardCol in range(len(board[boardRow])):
            if(board[boardRow][boardCol] == 0):
                return False
    
    return True

# Check if a player won
def checkWin(player):
    # Check win in row
    for boardRow in (range(len(board))):
        if((board[boardRow][0] == player) and (board[boardRow][1] == player) and (board[boardRow][2] == player)):
            return True

    # Check win in column
    for boardCol in (range(len(board[0]))):
        if((board[0][boardCol] == player) and (board[1][boardCol] == player) and (board[2][boardCol] == player)):
            return True

    # Check win in right diagonal
    if((board[0][0] == player) and (board[1][1] == player) and (board [2][2] == player)):
        return True

    # Check win in left diagonal
    if((board[2][0] == player) and (board[1][1] == player) and (board [0][2] == player)):
        return True

    # False if no player has won
    return False

# Restart game (set board to 0 and sets player to 1)
def restartGame():
    drawBoard()

    # Sets board to all 0's 
    for boardRow in range(len(board)):
        for boardCol in range(len(board[boardRow])):
            board[boardRow][boardCol] = 0

    # Sets player to 1
    return 1

# Main game loop
def main():
    # Global score variables
    global xScore, oScore

    # Game loop bool
    loopBool = True

    # Player (1 = X, 2 = O)
    player = 1

    # Mouse button down event ID
    mouseButtonDownID = ""

    drawLoading()
    time.sleep(2)

    drawBoard()

    # Game loop
    while(loopBool):
        # Loop for events (Key presses and mouse clicks)
        for event in pygame.event.get():
            # Exit game when window is closed
            if(event.type == pygame.QUIT):
                loopBool = False

            # Capture mouse click which determines player move
            if(event.type == pygame.MOUSEBUTTONDOWN):
                mouseButtonDownID = event.type

                mouseClickX = event.pos[0]
                mouseClickY = event.pos[1]

                boxRowClick = int(mouseClickY // 200)
                boxColClick = int(mouseClickX // 200)

                # If board is not full
                if (isBoardFull() == False):
                    # If box is empty
                    if isBoxEmpty(boxRowClick, boxColClick):
                        # If player X ...
                        if(player == 1):
                            insertMove(boxRowClick, boxColClick, player)
                            drawMove()
                            # If player X won
                            if(checkWin(player)):
                                # Calculate score
                                xScore = xScore + 1
                                drawWinScreen(player)
                                # Block mouse press event (until 'R' is pressed)
                                pygame.event.set_blocked(mouseButtonDownID)
                            # Set player to O     
                            player = 2
                        # ... or player O
                        elif(player == 2):
                            insertMove(boxRowClick, boxColClick, player)
                            drawMove()
                            # If player O won
                            if(checkWin(player)):
                                # Calculate score
                                oScore = oScore + 1
                                drawWinScreen(player)
                                # Block mouse press event (until 'R' is pressed)
                                pygame.event.set_blocked(mouseButtonDownID)
                            # Set player to X
                            player = 1
        
            # Restart game on keypress 'R'
            if(event.type == pygame.KEYDOWN):
                # If 'R' key is clicked
                if(event.key == pygame.K_r):
                    # Allow key press event (undo the block)
                    pygame.event.set_allowed(mouseButtonDownID)
                    # Set player to 1 and reset board
                    player = restartGame()
                
        # Draws draw screen if board is full
        if (isBoardFull() == True):
            # Block mouse press event (until 'R' is pressed)
            pygame.event.set_blocked(mouseButtonDownID)
            drawDrawScreen()

    pygame.quit()

main()