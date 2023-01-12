import pyperclip

text = pyperclip.paste()

# TODO: Add * in front of every text line as a bullet point
lines = text.split('\n')

for line in range(len(lines)):
    lines[line] = '* ' + lines[line]

text = '\n'.join(lines)
print(text)

pyperclip.copy(text)
