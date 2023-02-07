import os, zipfile

os.chdir('C:\\Users\\USER\\Desktop')

exampleZip = zipfile.ZipFile('test_file.zip')

# extracts the file into the cwd or the path passed into the extractall method
exampleZip.extractall('C:\\Users\\USER\\Desktop\\Programming Tutorials')

# Using the extract method
# It extracts the specified file into the path passed in as 
# the second argument.

print(exampleZip.extract('test_file/myfile.txt', 'C:\\Users\\USER\\Desktop\\test_folder'))

exampleZip.close()