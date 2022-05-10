fizz = "Fizz"
buzz = "Buzz"
fizzbuzz = fizz + buzz
increment3 = 3
increment5 = 5

def OnePlayer():
    failed = False
    print("Hello player! Hope you know how to play FizzBuzz!")
    for i in range(1,101):
        playerEntry = str(input("Your turn: "))
        if i % increment3 == 0 and i % increment5 == 0:
            if playerEntry.upper() != (fizzbuzz.upper()):
                failed = True
            else:
                print(fizzbuzz)
        elif i % increment3 == 0:
            if playerEntry.upper() != (fizz.upper()):
                failed = True
            else:
                print(fizz)
        elif i % increment5 == 0:
            if playerEntry.upper() != (buzz.upper()):
                failed = True
            else:
                print(buzz)
        else:
            if playerEntry != str(i):
                print("Whoops, wrong answer. You lose!")
                break
            else:
                print(i)
        if failed == True:
            print("Whoops, wrong answer. You lose!")
            break
        if i == 100:
            print("\nYou win!")
        
    print("\nThanks for playing FizzBuzz!")
                