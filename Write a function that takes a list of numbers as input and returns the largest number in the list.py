def maximum(list):
    return max(list)
string=input('enter a list of nember seperated by comma:')
new_list=string.split(',')
new_list=[int(num) for num in new_list]
print('the list:',new_list)
largest=maximum(new_list)
print("the largest nember is:",largest)
