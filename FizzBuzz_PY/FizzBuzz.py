#created by crisivanz1
#originally created 5/8/22
#this version created 5/11/22

class FizzBuzz:

    _fizz = "Fizz"
    _buzz = "Buzz"
    _fizzbuzz = _fizz + _buzz
    _increment3 = 3
    _increment5 = 5

    def Menu(self):
        #menu system, only public class function
        menuOptions = ("1. Play FizzBuzz (1 Player)", "2. Play FizzBuzz (2 Player)",
        "3. Play FizzBuzz (against the computer)", "4. Let the computer play FizzBuzz")
        menuChoices = {"1": self.__OnePlayer, "2": self.__TwoPlayer, "3": self.__VsCPU, "4": self.__default}
        
        print("Welcome to the FizzBuzz program, Python Edition!")
        for i in menuOptions:
            print(i)

        while True:
            userInput = str(input("Choose a menu option: "))
            if userInput not in menuChoices.keys():
                print("Invalid Answer. Please type another one.")
            else:
                menuChoices[userInput]()
                break

    def __CPU(self, i):
        #computer, runs its turn of the game
        if i % self._increment3 == 0 and i % self._increment5 == 0:
            print(self._fizzbuzz)
        elif i % self._increment3 == 0:
            print(self._fizz)
        elif i % self._increment5 == 0:
            print(self._buzz)
        else:
            print(i)
        
    def __default(self):
        #the computer playing the entire game
        for i in range(0, 101):
            self.__CPU(i)
    
    def __Player(self, i, failed):
        #allows the user to play, checks their answer and if they got it wrong
        playerEntry = str(input())
        if i % self._increment3 == 0 and i % self._increment5 == 0:
            if playerEntry.upper() != self._fizzbuzz.upper():
                failed = True
        elif i % self._increment3 == 0:
            if playerEntry.upper() != self._fizz.upper():
                failed = True
        elif i % self._increment5 == 0:
            if playerEntry.upper() != self._buzz.upper():
                failed = True
        else:
            if playerEntry != str(i):
                failed = True
        return failed

    def __VsCPU(self):
        #player plays against the computer
        playerTurn = True
        failed = False
        print("Hello player! Hope you know how to play FizzBuzz! Your opponent today is a machine!")
        for i in range(1,101):
            if playerTurn == True:
                print("Player 1, your turn: ") 
                failed = self.__Player(i, failed)
            elif playerTurn == False:
                self.__CPU(i)

            if failed == True:
                self.__failedState(False)
                break
            playerTurn = not playerTurn

    def __OnePlayer(self):
        #player plays against themselves
        failed = False
        print("Hello player! Hope you know how to play FizzBuzz!")
        for i in range(1,101):
            failed = self.__Player(i, failed)
            if failed == True:
                self.__failedState()
                break

    def __TwoPlayer(self):
        #two players play against themselves
        currentPlayer = True
        failed = False
        print("Hello players! Hope you know how to play FizzBuzz! Today you're facing each other!")
        for i in range(1,101):
            if currentPlayer == True:
                print("Player 1, your turn: ") 
                failed = self.__Player(i, failed)
            elif currentPlayer == False:
                print("Player 2, your turn: ") 
                failed = self.__Player(i, failed)
            if failed == True:
                self.__failedState(True, currentPlayer)
                break
            currentPlayer = not currentPlayer

    def __failedState(self, twoPlayer = False, currentPlayer = True):
        #only called if a player has failed, checks which player has failed if two player
        if twoPlayer == False:
            print("Whoops, wrong answer! You Lose!")
        else:
            if currentPlayer == True:
                print("Whoops, wrong answer Player 1!")
                print("Player 2, you win!")
            else:
                print("Whoops, wrong answer Player 2!")
                print("Player 1, you win!")
        print("Thanks for playing FizzBuzz!")

FB = FizzBuzz()
FB.Menu()