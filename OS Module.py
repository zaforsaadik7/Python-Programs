import os


print (dir(os))
#This will show all the functions and methods that we can access through the module.

current_directory=os.getcwd()
print('current directory:', {current_directory})

#To change or nevigate the directory of os module
os.chdir('\Users\Zafor Saadik')

#To see the folder list of a directory
print(os.listdir('c:'))

#to create a folder
os.makedirs('c:\ Test Folder using OS Module')

#To delete a directory
os.rmdir('c:\ test')

#To rename a file or a filder
os.rename('Relation between os module and underlying operating system','Relation between os module and underlying operating system.txt')

#For information of a file
print(os.stat('Relation between os module and underlying operating system.txt'))

#If we want to see the entire directory tree and files within the disltop, we can use the os.walk method. 
# #It yeilds three values of tuples. For each directory it'll yield the directory path, the other directory within that path and the files within the path.
for dirpath, dirname, filename in os.walk(os.getcwd()):
    print('current directory:',dirpath)
    print('directory:',dirname)
    print('files:',filename)
    print()

#Access home directory by home environment variable
#When a user logs into a computer system, their home directory is automatically set as the current working directory. This allows the user to easily access and manage their files.
home_directory=os.environ.get('USERPROFILE')
print('Home Directory:',{home_directory})

#How to combine a directory with a file name
print(os.path.join(os.environ.get('USERPROFILE'),'text.txt'))

#How to extract the basename from a given path
print('basename:',os.path.basename('\\Users\\Zafor Saadik\\Downloads\\text.txt'))

#How to peint the name of the directory
print('directory:', os.path.dirname('\\Users\\Zafor Saadik\\Downloads\\text.txt'))

#How to print base/file name and directory name
print(os.path.split('\\Users\\Zafor Saadik\\Downloads\\text.txt'))

#How to check if a path/ directory exist
print(os.path.exists('\\Users\\Zafor Saadik\\Downloads\\text.txt'))

#How to spllit the root of the pah and the extension
print(os.path.splitext('\\Users\\Zafor Saadik\\Downloads\\text.txt'))
