import re

haRegex = re.compile(r'(Ha){3,}')
mo1 = haRegex.search('HaHaHa')
print(mo1.group())

mo2 = haRegex.search('Ha')
print(mo2)


# Greedy and Non-Greedy Matching
greedyHaRegex = re.compile(r'(Ha){3,5}')
mo1 = greedyHaRegex.search('HaHaHaHaHa')
print(mo1.group())

nongreedyHaRegex = re.compile(r'(Ha){3,5}?')
mo1 = nongreedyHaRegex.search('HaHaHaHaHa')
print(mo1.group())

# The Findall Method
# Note: The Search method would return 
# a match object of the first matched text in the searched string

# Using the Search Method
phoneNumRegex = re.compile(r'\d{3}-\d{3}-\d{3}')
mo = phoneNumRegex.search('Cell: 415-555-9998 Work: 212-555-0000')
print(mo.group())

# Using the Findll Method
phoneNumberRegex = re.compile(r'\d{3}-\d{3}-\d{4}') # has no groups
mo = phoneNumberRegex.findall('Cell: 415-555-9998 Work: 212-555-0000')
print(mo)

phoneNumberRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)') # has groups
mo = phoneNumberRegex.findall('Cell: 415-555-9998 Work: 212-555-0000')
print(mo)