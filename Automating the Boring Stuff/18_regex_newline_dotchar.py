import re


noNewlineRegex = re.compile(r'.*')
mo = noNewlineRegex.search('''Search the public trust. 
Protect the innocent.
Uphold the law.''').group()
print(mo)

print()

newlineRegex = re.compile('.*', re.DOTALL)
mo1 = newlineRegex.search('''Search the public trust. 
Protect the innocent.
Uphold the law.''').group()
print(mo1)
