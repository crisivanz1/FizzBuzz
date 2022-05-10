fizz = "Fizz"
buzz = "Buzz"
fizzbuzz = fizz + buzz
increment3 = 3
increment5 = 5

def VsCPU():
    playerTurn = True
    print("Hello player! Hope you know how to play FizzBuzz! Your opponent today is a machine!")
    for i in range(1,101):
        failed = False
        if playerTurn == True:
            playerEntry = str(input("Your turn: "))
            if i % increment3 == 0 and i % increment5 == 0:
                if playerEntry.upper() != (fizzbuzz.upper()):
                    failed = True
                else:
                    print(fizzbuzz)
                    playerTurn = False
            elif i % increment3 == 0:
                if playerEntry.upper() != (fizz.upper()):
                    failed = True
                else:
                    print(fizz)
                    playerTurn = False
            elif i % increment5 == 0:
                if playerEntry.upper() != (buzz.upper()):
                    failed = True
                else:
                    print(buzz)
                    playerTurn = False
            else:
                if playerEntry != str(i):
                    failed = True
                else:
                    print(i)
                    playerTurn = False
            if failed == True:
                print("Whoops, wrong answer. You lose!")
                break

            if i == 100:
                print("\nYou win!")
                
        else:
            if i % increment3 == 0 and i % increment5 == 0:
                print(fizzbuzz)
                playerTurn = True
            elif i % increment3 == 0:
                print(fizz)
                playerTurn = True
            elif i % increment5 == 0:
                print(buzz)
                playerTurn = True
            else:
                print(i)
                playerTurn = True


    print("\nThanks for playing FizzBuzz!")

