import os, re


# os.chdir('C://Users//USER//Desktop//example')

regex = re.compile(r'\d{3}-\d{3}-\d{4}')

for foldername, subfolders, filenames in os.walk('C://Users//USER//Desktop//example//extracted_content'):

    for filename in filenames:

            # print(os.getcwd())

            full_path = foldername + '//' + filename
        
            file = open(full_path, 'r')
            text = file.read()
            file.close()
            
            if regex.search(text):
                print(filename)
                print(full_path)
                break



