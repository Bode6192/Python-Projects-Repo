import os, zipfile, shutil


os.chdir('C://Users//USER//Desktop//Program Test Files')

f = open('fileone.txt', 'w+')
f.write('ONE FILE')
f.close()


f = open('filetwo.txt', 'w+')
f.write('TWO FILES')
f.close()


comp_file = zipfile.ZipFile('comp_file.zip', 'w')

comp_file.write('fileone.txt', compress_type=zipfile.ZIP_DEFLATED)

comp_file.write('filetwo.txt', compress_type= zipfile.ZIP_DEFLATED)

comp_file.close()

# To extract objects from the file:
zip_obj = zipfile.ZipFile('comp_file.zip', 'r')

# To extract one specific file we use the code below:
zip_obj.extract('fileone.txt', 'extracted_content')
# We could also add the specific path the file should be 
# extracted to


# To extract more than one file we use the code below:
zip_obj.extractall(os.path.abspath('extracted_content'))
# We could also add the specific path the files should be 
# extracted to


dir_to_zip = os.getcwd() + '//extracted_content'

output_filename = 'example'

print(shutil.make_archive(output_filename, 'zip', dir_to_zip))

print(shutil.unpack_archive('example.zip', 'final_unzip', 'zip'))