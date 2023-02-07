# Write a function that checks whether a word or phrase 
# is a palindrome or not.

def palindrome(s):
    s = s.replace(' ', '')
    if s == s[::-1]:
        return True
    else:
        return False

a_string = 'nurses run'
print(palindrome(a_string))