# A program that finds all files with a given prefix such as
# spam001.txt, spam0012.txt and so on in numbered order and 
# can insert gaps into the numbered files so that a new file
# can be added.


import re, os, shutil

os.chdir('C:\\Users\\USER\\Desktop\\Program Test Files')

regex = re.compile(r'([A-Za-z]*)(\d*)(\.[a-z]*)')

fileList = []

for file in os.listdir():

    if regex.search(file):
        fileList.append(file)
    else:
        continue

print(fileList)

max_length = len(regex.search(fileList[-1]).group(2))

replace = int(input('At what index do you want to enter a gap? '))
gap = replace + 1

for file in fileList:

    mo = regex.search(file)
    fileNum = int(regex.search(file).group(2))

    if fileNum == replace:
        newFileName = mo.group(1) + '0'*(max_length-len(str(fileNum))) + str(gap) + mo.group(3)
        shutil.move(os.path.abspath(file), os.path.abspath(newFileName))
        new_value = replace + 1
        

        for file in fileList[(replace):]:

            mo = regex.search(file)
            fileNum = int(regex.search(file).group(2))
            new_value += 1 
            
            newFileName = mo.group(1) + '0'*(max_length-len(str(fileNum))) + str(new_value) + mo.group(3)
            shutil.move(os.path.abspath(file), os.path.abspath(newFileName))

        break

fileList = [file for file in os.listdir() if regex.search(file)]

print(fileList)





