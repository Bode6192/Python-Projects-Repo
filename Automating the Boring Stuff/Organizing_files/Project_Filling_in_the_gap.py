# A program that finds all files with a given prefix, such 
# as spam001.txt and so on, in a folder and locates any gaps
# in the numbering (such as if there is a spam001.txt and 
# spam003.txt but no spam002.txt). The program rename all the
# later files to close this gap.


import os, shutil, re

os.chdir('C:\\Users\\USER\\Desktop\\Program Test Files')

regex = re.compile(r'([A-Za-z]*)(\d*)(\.[A-Za-z]*)')

fileList = []

for file in os.listdir():

    if regex.match(file):

        fileList.append(file)

fileList = sorted(fileList)

print(fileList)

start = int(regex.search(fileList[0]).group(2))
count = start
max_length = len(regex.search(fileList[-1]).group(2))


for file in fileList:

    mo = regex.search(file)
    fileNum = int(mo.group(2))

    if fileNum != count:
        newFileName = mo.group(1) + '0'*(max_length-len(str(fileNum))) + str(count) + mo.group(3)
        shutil.move(os.path.abspath(file), os.path.abspath(newFileName))

    count += 1

print([file for file in os.listdir() if regex.search(file)])

