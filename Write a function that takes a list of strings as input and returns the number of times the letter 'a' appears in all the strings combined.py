def a_counter(list):
    combin_string=''.join(list)
    counter=0
    for char in combin_string:
        if char== 'a':
            counter+=1
    return counter
input_list=input('enter a list of string:')
print(a_counter(input_list))
