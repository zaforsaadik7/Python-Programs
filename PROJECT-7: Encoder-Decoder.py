import os
import zipfile
import csv

def encode_file(file_path):
    file_name, file_ext = os.path.splitext(file_path)
    if file_ext == '.zip':
        print('The file is already encoded.')
        return
    try:
        file_size = os.path.getsize(file_path)
        part_size = file_size // 10
        with open(file_path, 'rb') as f:
            for i in range(1, 11):
                part_file_name = f'{i}th.txt'
                with open(part_file_name, 'wb') as part_file:
                    part_file.write(f.read(part_size))
                    part_file.write(b'garbageval')
        with open('file information.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['file name', 'file format', 'actual file size'])
            writer.writerow([file_name, file_ext, file_size])
        password = input('Enter a password to secure the encoded file: ')
        zip_file_name = f'encoded_{file_name}.zip'
        with zipfile.ZipFile(zip_file_name, 'w') as zf:
            for i in range(1, 11):
                part_file_name = f'{i}th.txt'
                zf.write(part_file_name, compress_type=zipfile.ZIP_DEFLATED)
                os.remove(part_file_name)
            zf.write('file information.csv', compress_type=zipfile.ZIP_DEFLATED)
            os.remove('file information.csv')
        os.remove(file_path)
    except Exception as e:
        print(f'An error occurred: {e}')

def decode_file(file_path):
    file_name, file_ext = os.path.splitext(file_path)
    if file_ext != '.zip':
        print('The file is not encoded.')
        return
    try:
        with zipfile.ZipFile(file_path) as zf:
            zf.extractall(file_name)
        with open(os.path.join(file_name, 'file information.csv'), newline='') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)
            row = next(reader)
            decoded_file_name = f'decoded_{row[0]}{row[1]}'
            decoded_file_size = int(row[2])
        with open(decoded_file_name, 'wb') as f:
            for i in range(1, 11):
                part_file_name = os.path.join(file_name, f'{i}th.txt')
                with open(part_file_name, 'rb') as part_file:
                    data = part_file.read()[:-10]
                    f.write(data)
                    os.remove(part_file_name)
        os.rmdir(file_name)
    except Exception as e:
        print(f'An error occurred: {e}')

def main():
    directory = input('Enter the directory name of the file: ')
    os.chdir(directory)
    while True:
        option = input('Do you want to encode or decode a file? (encode/decode): ')
        if option == 'encode':
            file_path = input('Enter the name of the file to encode: ')
            encode_file(file_path)
        elif option == 'decode':
            file_path = input('Enter the name of the file to decode: ')
            decode_file(file_path)

if __name__ == '__main__':
    main()
"""
create a Python program for encoding and decoding files, that will-

1. ask the user to input a directory name of a file
2. give the user option to encode or decode the file
3. for encoding the file, there will be a function where-
*if the file type is ‘.zip’ tell the user, the file is already encoded otherwise-
 3.1.  take the file as input of the function.
 3.2.  measure the size of the file.
 3.3.  divide the size by 10.
 3.4.  start a loop where the actual file will be copied and divided into 10 files. the size of each file will be 1/10th of the actual file 10 bytes. the first file will contain 1/10th of the data of the actual file and the second file will start copying from where the first file ended up copying and the iteration will continue until the actual file gets copied into these 10 files. these files have to be sorted from the first to the 10th file, name these files '1st.txt', '2nd.txt',.......'10th.txt'. in the extra 10 bytes and add some garbage value at the end of each file.
 3.5.  add an 11th file, the name of that file will be 'file information.csv', this file will contain information of the actual file such as "file name", "file format: mp4, mp3, txt, jpg, gif, etc.", "actual file size".
 3.6.  save these 10 files as '.txt' files and the 11th '.csv' file and ".zip" them into one file, and secure them with a password, this password will be given by the user. so ask the user for the password. the '.zip' file name should be like this- "encoded_acutal file name".
 3.7.  replace the actual file with the '.zip' file in the same directory.
 3.8   if error happens somewhere give an error message.

4. for decoding the file there will be a function where-
* if the file is anything other than '.zip' it'll tell the user that the file isn't yet, otherwise-
 4.1.  take the file as input of the function.
 4.2.  unzip the file in a new folder which name will be like- "actual name" of the file. the folder should be created in the same directory.
 4.2.  create a file with file name like this- "decoded_actual file name". you can determine the size of the file and format of the file from the 11th file from the folder name 'file information.csv'.
 4.3.  create a loop where you'll delete the last 10 bytes from the text files and copy them newly created file with the actual format and size in ascending order of the file names. do not incude the 'csv' file into the loop.
 4.5.  delete the folder where you unziped the zip file and replace it with the new file. 
 4.6.   if error happens somewhere give an error message.
"""
