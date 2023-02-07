#! python3
# backupToZip.py - Copies an entire folder and it's contents 
# into a ZIP file whose filename increments.

import zipfile, os

os.chdir('C:\\Users\\USER\\Desktop')

def backuptoZip(folder):
    # Backup the entire contents of "folder" into a ZIP file.

    folder = os.path.abspath(folder) # makes sure folder is absolute

    # Figure out the filename this code should use based on 
    # what files already exists.

    number = 1

    while True:
        zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
         