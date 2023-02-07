# To delete files - os.unlink(path)
# To delete folders - os.rmdir(path)
# To delete folders and all Files/folders in it - 
# shutil.rmtree(path). Note: These functions are irreversible
# Note: Shutil is a module for Organizing Files
# It has functions - move(), copy(), copytree() etc

import os, shutil, send2trash

for filename in list(os.listdir()):
    if filename.endswith('.pdf'):
        # delete permanently with os.unlink(filename) or
        # temporarily with send2trash.send2trash(filename)
        print(filename)
