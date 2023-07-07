import os 
directory= '/path/to/directory'
suffix= '_suffex'
prefix= 'prefix_'

for filename in os.listdir(directory):
    new_filename= prefix + filename + suffix
    old_path= os.path.join(directory, filename)
    new_path= os.path.join(directory, new_filename)
    os.rename(filename, new_filename)
