import re

phoneNumberRegex = re.compile(r'(\(\d{3}\)) (\d{3}-\d{4})')
mo = phoneNumberRegex.search('My numbers are (717) 825-0145 and 455-627-0012.')

print('Phone number found: ' + mo.group())
areaCode, mainNumber = mo.groups()

print(areaCode, mainNumber)
