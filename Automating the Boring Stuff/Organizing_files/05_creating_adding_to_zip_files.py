import os, zipfile

os.chdir('C:\\Users\\USER\\Desktop')

newZip = zipfile.ZipFile('new.zip', 'a')

newZip.write('spam.txt', compress_type=zipfile.ZIP_DEFLATED)

newZip.close()