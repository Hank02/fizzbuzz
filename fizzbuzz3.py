
def fbz(number):
    answer = ""
    if number % 3 == 0 and number % 15 == 0:
        answer += "FizzBuzz"
    elif number % 3 == 0:
        answer += "Fizz"
    elif number % 5 == 0:
        answer += "Buzz"
    else:
        answer += str(number)
    return answer