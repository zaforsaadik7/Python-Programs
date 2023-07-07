import os
def file_organizer(directory):
    directiry= os.path.abspath(directory)
    for filename in os.listdir(directory):
        file_path= os.path.join(directory, filename)
        
        if os.path.isdir(file_path):
            continue
        file_type= filename.split('.')[-1]

        folder_path= os.path.join(directory,file_type)
        
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        new_file_path= os.path.join(folder_path, filename)
        os.rename(file_path, new_file_path)

        print(f'Organized {len(os.listdir(directory))} files in {directory}')

insert= input('Enter a directory from your computer to organize the files: ')
file_organizer(insert)
