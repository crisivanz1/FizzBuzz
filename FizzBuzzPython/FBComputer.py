fizz = "Fizz"
buzz = "Buzz"
fizzbuzz = fizz + buzz
increment3 = 3
increment5 = 5

def Default():
    for i in range(1,101):
        if i % increment3 == 0 and i % increment5 == 0:
            print(fizzbuzz)
        elif i % increment3 == 0:
            print(fizz)
        elif i % increment5 == 0:
            print(buzz)
        else:
            print(i)
