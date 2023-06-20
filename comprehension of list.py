# comperihension is an easier and more readable way to copy a list.


#copying list through loop
num=[1,2,3,4,5,6,7,8,9,10]
copied_list=[]
for n in num:
    copied_list.append(n)
print(copied_list)

#coping through comperihension
my_list=[]
my_list=[n for n in num]
print(my_list)

squired=[]
squired=[n*n for n in num]
print(squired)
