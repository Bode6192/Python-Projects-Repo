import re


# You could use re.I or re.IGNORECASE
robocop = re.compile(r'robocop', re.IGNORECASE)
mo = robocop.search('RoboCop is part man, part machine, all cop.').group()
print(mo)

mo1 = robocop.search('ROBOCOP protects the innocent.').group()
print(mo1)

mo2 = robocop.search('Al, why does your programming book talk about robocop so much?').group()
print(mo2)