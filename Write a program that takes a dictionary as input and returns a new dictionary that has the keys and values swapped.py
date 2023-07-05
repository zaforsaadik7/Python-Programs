def swaping_function(dictionary):
    return{value:key for key,value in dictionary.items()}

user_input= input('Enter the keys and values for the dictionary(key:value,key:value):')
split_pair=user_input.split(',')
my_dict={}
for pair in split_pair:
    key,value=pair.split(':')
    my_dict[key.strip()]= value.strip()
print(my_dict)
swaped_dictionary=swaping_function(my_dict)
print(swaped_dictionary)
