spam = ['apples', 'bananas', 'tofu', 'cats']

def list_to_string(list1):
    new_list = []
    for i in range(len(list1) - 1):
        new_list.append(spam[i])
    first_string = ', '.join(new_list)
    return str(first_string) + ' and ' + str(list1[-1]) 

new_string = list_to_string(spam)

print(new_string)

# name = 'bob'

# print(name + spam[-1])


