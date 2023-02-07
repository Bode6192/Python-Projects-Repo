#! python3

# A program that walks through a folder tree and searches 
# for files with a certain file extension (such as .pdf or .jpg).
# Copy these files from whatever location they are in to a new 
# folder

import os, shutil, send2trash

os.chdir('C:\\Users\\USER\\Desktop')

# A function that does the selective copy, it takes two arguments
# folder_1: the path to be walked through and searched and 
# folder_2: the folder to copy the files into 
def selective_copy(folder_1, folder_2):

    # Get the absolute path of the folder to be walked through
    folder_1 = os.path.abspath(folder_1)
    print(folder_1)
    folder_2 = os.path.abspath(folder_2)
    print(folder_2 + '\n')

    # Iterate through the folder
    for foldername, subfolders, filenames in os.walk(folder_1):
        
        # Search for all file in the Folder
        for filename in filenames:
            print(filename)

            # Get the path of the file to be used in the shutil 
            # function and add only functions ending with .jpg 
            # or .pdf
            filename = os.path.join(folder_1, filename)
            if os.path.basename(filename).endswith('.pdf') or os.path.basename(filename).endswith('.jpg'):
                shutil.copy(filename, folder_2)

selective_copy('My Documents', 'Program Test Files')