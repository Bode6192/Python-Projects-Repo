import os 

for folderName, subFolders, fileNames in os.walk('C:\\Users\\USER\\Desktop\\Python'):
    print('The current Folder is ' + folderName)

    print()

    for subfolder in subFolders:
        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)

    for filename in fileNames:
        print('FILE INSIDE ' + folderName + ': ' + filename)

    print()