# Write a function that takes in a single letter,
# and returns a 5* representation of that letter


letter_patterns = {'a':['  *  ',' * * ','*****','*   *','*   *'],
                'b':['***  ','*  * ','***  ','*  * ','***'],
                'c':['  ***',' *   ','*    ',' *   ','  ***'],
                'd':['***','*  *','*   *','*  *','***'],
                 'e':['*****','*','*****','*','*****']}

def print_big(letter):
    for pattern in letter_patterns[letter]:
        print(pattern)

print_big('e')