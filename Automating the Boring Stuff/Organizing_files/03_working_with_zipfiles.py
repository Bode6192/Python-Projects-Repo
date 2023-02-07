# to create a zip object - zipfile.ZipFile()

import zipfile, os

os.chdir('C:\\Users\\USER\\Desktop')

exampleZip = zipfile.ZipFile('test_file.zip')
print(exampleZip.namelist())

print()

print(exampleZip.getinfo('test_file/myfile.txt'))

print()

spamInfo = exampleZip.getinfo('test_file/myfile.txt')
print(spamInfo.file_size)

print(spamInfo.compress_size)
exampleZip.close()

