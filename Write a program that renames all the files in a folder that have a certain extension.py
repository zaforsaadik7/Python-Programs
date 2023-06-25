#For example, if the folder contains files with .txt, .py, and .jpg extensions, the program should rename all the .txt files to have a .bak extension.
# Use the os module to access the files and rename them.


import os
os.chdir('Downloads')#name of the directory of the files
new_ext = '.py'

for file in os.listdir():
    print(file)
    file_name, file_ext = os.path.splitext(file)
    print(file_name)
    print(file_ext)
    if file_ext == '.txt':
        new_file = '{}{}'.format(file_name, new_ext)
        os.rename(file, new_file)
