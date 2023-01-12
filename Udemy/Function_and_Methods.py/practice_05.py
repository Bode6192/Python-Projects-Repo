# write a Function to check whether a string is pangram or not

import string

def ispangram(str1, alphabet=string.ascii_lowercase):
    str1 = str1.replace(' ','').lower()
    for char in str1:
        if char not in alphabet:
            return False
    else:
        return True 

print(ispangram('The quick brown fox jumps over the lazy dog'))