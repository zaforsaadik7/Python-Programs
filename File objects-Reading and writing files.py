
#How to open a file
file=open('test.txt','r')
print(file.name)
file.close()

#Opening a  file using context manager

#The main purpose of a context manager is to define a specific block of code where a resource is used, guaranteeing that the resource is automatically set up before the block is executed and properly cleaned up afterward.
#This way, you don't have to worry about explicitly opening and closing the resource or handling any potential errors.

with open('test.txt','r') as file:
    content=file.read()
    print(content)

#Printing every lines of the file in a list
with open('test.txt','r') as file:
    content=file.readlines()
    print(content)
#Printing from a large file, a line at a time
with open('test.txt','r') as file:
    for line in file:
        print(line,end='')
    

#Printing a chunk from the file at a time using while loop
with open('test.txt','r') as file:
    size_to_read = 100
    content = file.read(size_to_read)
    while len(content) > 0:
        print(content, end='')
        content = file.read(size_to_read)
    print(file.tell())#This will print out the total size of the file as a counter.

#How to write a file 
#Using write mode we can write a file. Now if the file dosen't exist it'll create a new file, otherwise it'll overwrite the file.
with open('test2.txt', 'w') as file:
    content=file.write('Hello there, this is saadik. I am creating a new text file where every thing I write here will be saved as text.')
    print(content)

#How to copy a file
with open('test.txt','r') as read_file:
    with open('test2.txt','w') as write_file:
        for line in read_file:
            write_file.write(line)

#How to a picture file 
#Copying a picture file, we need to do it in bineary mode. For that in 'read' and 'write' mode instead of 'r' and 'w' we will use 'br' and 'bw'
with open('friends.jpg','br') as main_picture:
    with open('friends_copy.jpg','bw') as copied_picture:
        for line in main_picture:
            copied_picture.write(line)

#Copying portion of a picture
with open('friends.jpg','br') as rphoto:
    with open ('friends_copy.jpg','bw') as cphoto:
        portion=20054
        content=rphoto.read(portion)
        while len(content)>0:
            cphoto.write(content)
            content=rphoto.read(portion)

#How to reaname mmultiple files:
#To rename multiple file we are going to create some file
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
sort = [1, 2, 3, 4, 5, 6, 7, 8]
for planet,i in zip(planets,sort):
    file_name='{}-Our Solar System-#{}.txt'.format(planet,i)
    with open(file_name,'w') as file:
        context='this is file number {}'.format(i)
        file.write(context)
#After creating the files, create a new folder and copy them to there and use that directory in the next

import os 

os.chdir('c:\\Users\\Zafor Saadik\\test folder')
for file in os.listdir():
    print(file)
    file_name,extentionn=os.path.splitext(file)
    print(file_name)
    file_title,course_name,file_num=file_name.split('-')
    file_title=file_title.strip()
    course_name=course_name.strip()
    file_num=file_num.strip()
    #strip() method will take care of any unnecessary speaces.
    new_file='{}-{} {}'.format(file_num,course_name,file_title)
    os.rename(file,new_file)
