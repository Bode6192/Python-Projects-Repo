import re


xmasRegex = re.compile(r'\d+\s\w+')
mo = xmasRegex.findall('''12 drummers, 11 pipers, 10 lords, 9 ladies,
8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge''')
print(mo)


# You can define your own Character Classes that are 
# not as broad as the shorthand character classes
vowelRegex = re.compile(r'[aeiouAEIOU]')
mo1 = vowelRegex.findall('RoboCop eats baby food. BABY FOOD.')
print(mo1)

# Negative Character Class 
# Note: The caret symbol's function is different in Char classes
consonantRegex = re.compile(r'[^aeiouAEIOU]')
mo2 = consonantRegex.findall('RoboCop eats baby food. BABY FOOD.')
print(mo2)

# The Caret Char (^) matches strings that start with the 
# Character after it
beginsWithHello = re.compile(r'^Hello')
mo3 = beginsWithHello.search('Hello world!')
print(mo3)
mo4 = beginsWithHello.search('He said hello.') # == None
print(mo4)

# The Dollar Char matches strings that end with the character
# before it
endsWithNumber = re.compile(r'\d$')
mo5 = endsWithNumber.search('Your number is 42')
print(mo5)
mo6 = endsWithNumber.search('Your number is Forty two.') 
print(mo6 == None)


wholeStrigIsNum = re.compile(r'^\d+$')
mo7 = wholeStrigIsNum.search('1234567890')
print(mo7.group())
print(wholeStrigIsNum.search('12345xyz67890') == None)
print(wholeStrigIsNum.search('12   34567890') == None)