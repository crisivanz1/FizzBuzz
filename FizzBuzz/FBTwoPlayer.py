fizz = "Fizz"
buzz = "Buzz"
fizzbuzz = fizz + buzz
increment3 = 3
increment5 = 5


def TwoPlayer():
    currentPlayer = True
    failed = False
    print("Hello players! Hope you know how to play FizzBuzz! Today you're facing each other!")
    for i in range(1,101):
        if currentPlayer == True:
            playerEntry = str(input("Player 1's turn: "))
        else:
            playerEntry = str(input("Player 2's turn: "))
        if i % increment3 == 0 and i % increment5 == 0:
            if playerEntry.upper() != (fizzbuzz.upper()):
                failed = True
            else:
                print(fizzbuzz)
                currentPlayer = not currentPlayer
        elif i % increment3 == 0:
            if playerEntry.upper() != (fizz.upper()):
                failed = True
            else:
                print(fizz)
                currentPlayer = not currentPlayer
        elif i % increment5 == 0:
            if playerEntry.upper() != (buzz.upper()):
                failed = True
            else:
                print(buzz)
                currentPlayer = not currentPlayer
        else:
            if playerEntry != str(i):
                failed = True
            else:
                print(i)
                currentPlayer = not currentPlayer
        if failed == True:
            if currentPlayer == True:
                print("Whoops, wrong answer Player 1!")
                print("Player 2, you win!")
                break
            else:
                print("Whoops, wrong answer Player 2!")
                print("Player 1, you win!")
                break

    print("\nThanks for playing FizzBuzz!")
                