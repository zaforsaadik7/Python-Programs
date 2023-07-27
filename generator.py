def square(num):
    result=[]
    for i in num:
        result.append(i*i)
    return result

#Doing with generator
def generator(num):
    for i in  num:
        yield(i*i)

my_list= square([1,2,3,4,5])
for num in my_list:
    print(num)

my_list= generator([1,2,3,4,5])
for num in my_list:
    print(num)
