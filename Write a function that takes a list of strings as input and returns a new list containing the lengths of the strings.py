if __name__ == '__main__':
    def length(lst):
        str_length = []
        split_list = lst.split(',')
        for string in split_list:
            str_length.append(len(string))
        return str_length
    
    x = input('Enter a list of strings: ')
    print(length(x))
