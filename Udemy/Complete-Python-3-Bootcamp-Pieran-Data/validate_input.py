def user_choice():
    choice = 'WRONG'
    acceptable_range = range(0, 10)
    within_range = False
    
    while choice.isdigit() == False or within_range == False:
        choice = input('Please enter an integer between (0-10), 0 inclusive: ')
        print()

        if not choice.isdigit():
            print("Sorry that is not a digit")

        if choice.isdigit():
            if int(choice) in acceptable_range:
                within_range = True
            else:
                print('Sorry, you are out of acceptabl range (0 - 10)')
                within_range = False
        
    
    return int(choice)

user_choice()