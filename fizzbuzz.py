upper = 100
print("Fizz buzz counting up to {0}".format(upper))

number = 1
while number < upper + 1:
    if number % 3 == 0 and number % 15 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
    number += 1
