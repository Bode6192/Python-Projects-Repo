import re
from unicodedata import digit 

def password_check(password):
    # To check if the password string is strong
    # It must have at least eight characters,
    # contain both uppercase and lowercase chars,
    # and has at least one digits
    
    # Note: Password must be a string 

    if len(password) < 8:
        return  '''Password must be at least eight characters.
        Try again'''
    
    uppercase_letter = re.compile(r'[A-Z]')
    lowercase_letter = re.compile(r'[a-z]')
    digit = re.compile(r'[0-9]{1,}')

    uppercase_search = uppercase_letter.findall(password)
    print(uppercase_search)
    lowercase_search = lowercase_letter.findall(password)
    digit_search = digit.findall(password)

    if uppercase_search == []:
        return '''Your password must contain at least one uppercase letter
        Try again '''
    elif lowercase_search == []:
        return '''Your password must contain at least one lowercase letter
        Try again'''
    elif digit_search == []:
        return '''Your password must contain at least one digit char
        Try again'''
    else:
        return '''Password Approved'''


password  = input('Enter your password: ')

print(password_check(password))



    
    