num=[1,2,3,4,5,6,7,8,9,10]
copied_list=[]

for n in num:
    if n%2 == 0:
        copied_list.append(n)
print(copied_list)

#Through comperihension 
even_num=[]
even_num=[n for n in num if n % 2 == 0]
print(even_num)


