import re

def regex_strip(string, specified_char = ' '):
    # This Function does the same thing as the strip method.
    # If no other arguments are passed other than the string to strip,
    # then the whitespace characters will be removed
    # from the beginning and end of the string. 
    # Otherwise, the chars specified in the second argument
    # to the function will be removed from the string.

    left_char = re.compile(f'^[{specified_char}]*')
    strip = left_char.sub('', string)
    right_char = re.compile(f'[{specified_char}]*$')
    new_strip = right_char.sub('', strip)        

    return new_strip

string = 'www.example.com'
print(regex_strip(string, 'cmowz.'))
# returns: 'example'

comment_string = '#....... Section 3.2.1 Issue #32 .......'
print(regex_strip(comment_string, '.#! '))
# returns: 'Section 3.2.1 Issue #32'

string2 = 'SpamSpamBaconSpamEggsSpamSpam'
print(regex_strip(string2, 'pSam'))