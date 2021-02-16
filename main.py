import time

def main():
    while True:
        text()
        choice = input("\n\nEnter choice: ")

        printLines(50)

        if(choice == "1"):
            print("\n\nStarting [Game Name]...")
            printLines(50)
            print("\n\nExiting [Game Name]...")
            printLines(50)
            time.sleep(1)
        elif(choice == "2"):
            print("\n\nStarting [Game Name]...")
            printLines(50)
            print("\n\nExiting [Game Name]...")
            printLines(50)
            time.sleep(1)
        elif(choice == "3"):
            print("\n\nStarting [Game Name]...")
            printLines(50)
            print("\n\nExiting [Game Name]...")
            printLines(50)
            time.sleep(1)
        elif(choice == "0"):
            print("\n\nExiting...")
            printLines(50)
            break
        else:
            print("\n\nInvalid...")
            printLines(50)
            time.sleep(1)
            

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
[About us]
[How to start]
[etc...]""")

    printLines(100)

    print("""\n
    1. [Game 1]
    2. [Game 2]
    3. [etc...]
    0. Exit""")

    printLines(50)

def printLines(num):
    for i in range(num):
        print("_", end = "")

main()