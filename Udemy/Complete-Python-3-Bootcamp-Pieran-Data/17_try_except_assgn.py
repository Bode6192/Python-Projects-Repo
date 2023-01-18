# Problem 1

try:
    for i in ['a', 'b', 'c']:
        print(i**2)
except TypeError:
    print("Whoops! Can't square an integer and a string")


# Problem 2

try:
    x = 5
    y = 0

    z = x/y
except ZeroDivisionError:
    print("Whoops! Can't divide a number by 0")


# Problem 3

def ask():
    while True:
        try:
            num = int(input('Enter an integer: '))
            answer = num ** 2
        except TypeError:
            print("Whoops! Can't square an integer and a string")
        else:
            print(f'Thank you, your number is: {answer}')
            break

ask()