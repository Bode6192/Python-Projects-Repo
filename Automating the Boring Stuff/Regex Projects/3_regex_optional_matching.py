import re

# The ? matches 0 or 1(It is Optional) 
batRegex = re.compile(r'(Bat)(wo)?(man)')
mo1 = batRegex.search('The Adventures of Batman')
print(mo1.group())

print()

mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group())

print()

# The * matches 0 or more 
batRegex = re.compile(r'Bat(wo)*man')
mo3 = batRegex.search('The Adventures of Batman')
print(mo3.group())

print()

mo4 = batRegex.search('The Adventures of Batwoman')
print(mo4.group())

print()

mo5 = batRegex.search('The Adventures of Batwowowoman')
print(mo5.group())

print()

# The + matches 1 or more
batRegex = re.compile(r'Bat(wo)+man')
mo1 = batRegex.search('The Adventures of Batwoman')
print(mo1.group())

print()

mo2 = batRegex.findall('The Adventures of Batman')
print(mo2 == None)