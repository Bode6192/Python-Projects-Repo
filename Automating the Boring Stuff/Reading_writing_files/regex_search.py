# A program that opens all .txt files in a flder and searches
# for any line that matches a user-supplied regex. The results
# should be printed to the screen.

import os, re

folder = os.getcwd()
print(folder)

matches = []

for file in os.listdir(folder):

    files = open(file, 'r')
    text = files.read()
    files.close()

    regex = re.compile(r'\d+')
    match = regex.findall(text)
    matches += match


print(matches)