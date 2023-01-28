# A madlibs project that reads in text files and lets the 
# user add their own text anywhere the word ADJECTIVE, NOUN, 
# ADVERB, or VERB appears in the text file. 

import re 

file = open('madlibs.txt')
text = file.read()
file.close()

regex = re.compile(r'ADJECTIVE|NOUN|ADVERB|VERB').findall(text)

for word in regex:
    madLibsRegex = re.compile(word)
    if madLibsRegex.search(text):
        text = madLibsRegex.sub(input(f'Enter an {word.lower()}: '), text, 1)



newFile = open('newtext.txt', 'w')
newFile.write(text)
newFile.close()







