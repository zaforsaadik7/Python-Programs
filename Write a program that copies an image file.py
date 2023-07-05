with open('friends.jpg', 'rb') as read_file:
    with open('friends_copy.jpg', 'wb') as write_file:
        portion_size = 4000
        read_portion = read_file.read(portion_size)
        size = 0

        while len(read_portion) > 0:
            write_file.write(read_portion)
            size += len(read_portion)
            read_portion = read_file.read(portion_size)

        print('File size is {} bytes'.format(size))
        if size == 0:
            print('The file is not found.')
        else:
            print('File copied successfully.')
