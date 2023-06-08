def summation(list):
    sum=0
    for num in list:
        sum=sum+num
    return sum
number_string=input('Enter a string of number')
number_list=number_string.split(',')
number_list=[int(num) for num in number_list]
print('converted list:',number_list)
print(summation(number_list))
