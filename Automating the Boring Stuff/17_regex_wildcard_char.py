import re


atRegex = re.compile(r'.at')
mo = atRegex.findall('The cat in the hat sat on the flat mat')
print(mo)

nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo1 = nameRegex.search('First Name: Al Last Name: Sweigart')
print(mo1.group(1))

print()

print(mo1.group(2))


nongreedyRegex = re.compile(r'<.*?>')
mo2 = nongreedyRegex.search('<To serve man> for dinner.>')
print(mo2.group())


greedyRegex = re.compile(r'<.*>')
mo3 = greedyRegex.search(r'<To serve man> for dinner>')
print(mo3.group())
