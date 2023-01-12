def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    else:
        print(3 * number + 1)
        return 3 * number + 1


try:
    your_number = int(input('Enter a number: '))
    num = collatz(your_number)
    while num != 1:
        new = collatz(num)
        num = new 
except ValueError:
    print('Invalid Input')



