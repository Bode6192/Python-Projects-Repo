#! python3
# A program to delete exceptionally large file or folders


import os, send2trash


os.chdir('C:\\Users\\User\\Desktop')


def Unneded_folder_files_deletion(folder):
    
    folder = os.path.abspath(folder)

    for foldername, subfolders, filenames in os.walk(folder):
        
        for filename in filenames:

            filename = os.path.join(folder, filename)

            if os.path.getsize(filename) > 70000000:
                print(f'deleting {filename}')
                # send2trash.send2trash(filename)



Unneded_folder_files_deletion('Deep Learning MIT')

