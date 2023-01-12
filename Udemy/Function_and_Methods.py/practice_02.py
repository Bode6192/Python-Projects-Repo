# Write a Python Function that accepts a string and calculates
# the number of upper case letters and lower case letters

def up_low(string):
    num_uppercase = []
    num_lowercase = []
    for char in string:
        if char.isupper():
            num_uppercase.append(char)
        elif char.islower():
            num_lowercase.append(char)
    return f'''The number of uppercase letters are {len(num_uppercase)}
    while the number of lowercase letters are {len(num_lowercase)}'''

a_string = 'Hello Mr. Rogers, how are you this fine Tuesday?'

print(up_low(a_string))