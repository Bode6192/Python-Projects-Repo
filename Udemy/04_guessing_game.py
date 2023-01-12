from random import randint
num = randint(1, 100)
print(num)

guesses = [0]

while True:
    guess = int(input('Please enter your guess: '))
    guesses.append(guess)
    if guess < 0 or guess > 100:
        print('OUT OF BOUNDS! Please enter a valid guess')
        continue

    if guess == num:
        print('You got it correctly')
        print(f'You got it in {len(guesses)} guesses')
        break
        
    if len(guesses) < 3:
        if abs(guess - num) <= 10:
            print('WARM! Please try again.')
        else:
            print('COLD! Please try again')
    
    if len(guesses) >= 3:
        if abs(guess-num) < abs(guesses[-2]-num):
            print('WARMER!')
        else:
            print('COLDER!')