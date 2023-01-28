import re 

# Because of the Pipe Char (|) the .search method would match just
# one of many expressions
heroRegex = re.compile(r'Batman|Tina Fey')
mo1 = heroRegex.search('Tina Fey and Batman.')

print(mo1.group())
print()


mo2 = heroRegex.search('Batman and Tina Fey')
print(mo2.group())
print()


# Note: if there's a need to match the Pipe Character
# we escape with the backslash (\)
batRegex = re.compile(r'Bat(Man|mobile|copter)')
mo = batRegex.search('Batcopter lost a wheel')

print(mo.group())