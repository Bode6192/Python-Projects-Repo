birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 14'}

while True:
    name = input('Enter a name: (Leave blank to quit)')
    if name == '':
        break
    elif name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)
    else: 
        print("I do not have birthday information for ' + name +' but i'll add their info to the Database")
        bday = input('What is their birthday?: ')
        birthdays[name] = bday
        print(bday + ' has been included to the birthday database')

    

list1 = list(birthdays.items())
print(list1)