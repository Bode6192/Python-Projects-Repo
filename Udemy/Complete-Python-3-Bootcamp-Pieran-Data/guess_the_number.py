# This is a guess the number game.
from random import *
secret_number = randint(1, 20)

allowed_guesses = 7
guesses = 0
while guesses < allowed_guesses:
    guesses += 1
    your_guess = int(input('Enter your guess: '))
    if your_guess < secret_number:
        print('your guess is low')
    elif your_guess > secret_number:
        print('your guess is high')
    else:
        break

if your_guess == secret_number:
    print(f'You guessed the number in {str(guesses)} guesses')
else:
    print('You failed to guess the number')