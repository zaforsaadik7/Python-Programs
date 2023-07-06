num= input('Enter number for a list:')
num_list= num.split(',')
print(num_list)
new_list=[]
for num in num_list:
    num= int()
    if num% 2 == 0:
        new_list.append(num)
print(new_list)
