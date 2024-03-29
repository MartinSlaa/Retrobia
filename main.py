import time
import os

#  Main loop
def main():
    # Directory of Retrobia folder
    #directory = "e:/Retrobia/"
    directory = "~/Retrobia-master"
    
    # Meny loop
    while True:
        # Get menu choice
        text()
        choice = input("\n\nEnter number to start game: ")

        printLines(50)

        # Start game of choice or quit
        if(choice == "1"):
            print("\n\nStarting TicTacToe...")
            printLines(50)
            print("\n")
            #os.system("python " + directory + "/tictactoe/tictactoe_main.py")
            os.system("python3 " + directory + "/tictactoe/tictactoe_main.py")
            printLines(50)
            print("\n\nExiting TicTacToe...")
            printLines(50)
            time.sleep(2)
        elif(choice == "2"):
            print("\n\nStarting Invaders...")
            printLines(50)
            print("\n")
            #os.system("python " + directory + "/invaders/invaders_main.py")
            os.system("python3 " + directory + "/invaders/invaders_main.py")
            printLines(50)
            print("\n\nExiting Invaders...")
            printLines(50)
            time.sleep(2)
        elif(choice == "3"):
            print("\n\nStarting Snake...")
            printLines(50)
            print("\n")
            #os.system("python " + directory + "/snake/snake.py")
            os.system("python3 " + directory + "/snake/snake.py")
            printLines(50)
            print("\n\nExiting Snake...")
            printLines(50)
            time.sleep(2)
        elif(choice == "4"):
            print("\n\nStarting Bricks...")
            printLines(50)
            print("\n")
            #os.system("python " + directory + "/Bricks/bricks_main.py")
            os.system("python3 " + directory + "/Bricks/bricks_main.py")
            printLines(50)
            print("\n\nExiting Bricks...")
            printLines(50)
            time.sleep(2)
        elif(choice == "0"):
            print("\n\nExiting...")
            printLines(50)
            print("\n")
            break
        else:
            print("\n\nInvalid...")
            printLines(50)
            time.sleep(1)
            
# Print menu text
def text():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    
    printLines(100)

    print("""\n
                ██████╗ ███████╗████████╗██████╗  ██████╗ ██████╗ ██╗ █████╗ 
                ██╔══██╗██╔════╝╚══██╔══╝██╔══██╗██╔═══██╗██╔══██╗██║██╔══██╗
                ██████╔╝█████╗     ██║   ██████╔╝██║   ██║██████╔╝██║███████║
                ██╔══██╗██╔══╝     ██║   ██╔══██╗██║   ██║██╔══██╗██║██╔══██║
                ██║  ██║███████╗   ██║   ██║  ██║╚██████╔╝██████╔╝██║██║  ██║
                ╚═╝  ╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ╚═╝╚═╝  ╚═╝""")

    printLines(100)

    print("""\n
    1. TicTacToe
    2. Invaders
    3. Snake
    4. Bricks
    0. Exit""")

    printLines(50)

# Print lines
def printLines(num):
    for i in range(num):
        print("_", end = "")

main()