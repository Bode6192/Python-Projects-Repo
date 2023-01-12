while True:
    age = input('Enter your age: ')
    if age.isdecimal():
        break
    print('Please enter a number for your age.')

while True:
    password = input('Select a new password (letters and numbers only): ')
    if len(password) < 6:
        print('You must have a password length of at least 6')
        continue
    elif password.isalnum():
        break
    print('Passwords can only have letters and numbers')

    

