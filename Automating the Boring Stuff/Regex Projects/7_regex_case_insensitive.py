import re


# You could use re.I or re.IGNORECASE
robocop = re.compile(r'robocop', re.IGNORECASE)
mo = robocop.search('RoboCop is part man, part machine, all cop.').group()
print(mo)

mo1 = robocop.search('ROBOCOP protects the innocent.').group()
print(mo1)

mo2 = robocop.search('Al, why does your programming book talk about robocop so much?').group()
print(mo2)

# Substituting Strings with the Sub() method
namesRegex = re.compile(r'Agent \w+')
mo3 = namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.')
print(mo3)

agentNameRegex = re.compile(r'Agent (\w)\w*')
mo4 = agentNameRegex.sub(r'\1', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.')
print(mo4)

# Combining re.IGNORECASE, re.DOTALL, and re.VERBOSE
someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL | re.VERBOSE)
mo5 = someRegexValue.findall('''Foo has amnesia 
and foo doesn't want to go to the Hospital''')
print(mo5)