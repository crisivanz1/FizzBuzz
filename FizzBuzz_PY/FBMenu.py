from FBComputer import Default
from FBOnePlayer import OnePlayer
from FBTwoPlayer import TwoPlayer
from FBPlayerVsCPU import VsCPU

menuOptions = ["1", "2", "3", "4"]
print("Welcome to the FizzBuzz program, Python Edition!")

while True:
    userInput = str(input("Choose a menu option: "))
    if userInput not in menuOptions:
        print("bruh, choose again")
    else:
        if userInput == menuOptions[0]:
            Default()
        elif userInput == menuOptions[1]:
            OnePlayer()
        elif userInput == menuOptions[2]:
            VsCPU()
        elif userInput == menuOptions[3]:
            TwoPlayer()
        break