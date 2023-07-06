def sort(list):
    return sorted(list)

names= input('Enter names seperated by comma to make a list:')
name_list=names.split(',')
sorted_names= sort(name_list)
print(sorted_names)
