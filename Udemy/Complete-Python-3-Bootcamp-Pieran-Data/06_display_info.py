def display(row1,row2,row3):
    print(row1)
    print(row2)
    print(row3)

row1 = [' ',' ',' ']
row2 = [' ',' ',' ']
row3 = [' ',' ',' ']
display(row1,row2,row3)

def user_input():

    choice = 'wrong'
    acceptable_number = False

    while choice.isdigit() == False or acceptable_number == False:
        choice = input('Please enter a number from (0-10): ')

        #DIGIT CHECK
        if choice.isdigit() == False:
            print('Sorry, thats not a digit')

        #RANGE CHECK

        if choice.isdigit() == True:
            if int(choice) not in range(0,11):
                print('Sorry your choice is not in accaptable range (0-10) ')
                acceptable_number == False
            else:
                acceptable_number == True


    return int(choice)

print(user_input())

