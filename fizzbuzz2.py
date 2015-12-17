import sys

# make sure user entered a number at command line (ignore other arguments if more than one)
if len(sys.argv) > 1:
    try:
        upper = int(sys.argv[1])
    except ValueError:
         while 1:
            try:
                upper = int(input("Please enter an integer: "))
                break
            except ValueError:
                print("Try again...")
# if no command line arguments provided, request user for a number
else:
    while 1:
        try:
            upper = int(input("Please enter an integer: "))
            break
        except ValueError:
            print("Try again...")

# print number provided by user
print("Fizz Buzz counting up to {0}".format(upper))

# play Fizz Buzz
for number in range(1, upper + 1):
    if number % 3 == 0 and number % 15 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)