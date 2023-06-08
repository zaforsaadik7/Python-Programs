def filter(list):
    vowel=['a', 'e', 'i', 'o', 'u']
    result=[]
    for string in list:
        if string[0] in vowel:
            result.append(string)
    return result
input_string=input('Enter a list of string:')
input_list=input_string.split(',')
print(filter(input_list))
