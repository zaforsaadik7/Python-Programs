# Use the sorted function to sort the list in ascending order and then return the second last element.
number= input('Enter a list of numbers:')
num_list=number.split(',')
num_list.sort()
maximum_value=max(num_list)
v=num_list[0]
for i in range(len(num_list)):
    if num_list[i]>v and num_list[i]<maximum_value:
        v= num_list[i]
second_maximum=v
print('The second maximum number is ', second_maximum)
