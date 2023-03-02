import os

os.chdir('C://Users//USER//Desktop//example//extracted_content')

file = open('Instructions.txt', 'r')
text = file.read()
file.close()

print(text)