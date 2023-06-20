#Using function
#If we use the 'sorted' function, it'll give the sorted list as return value. Hence we take'll take a variable for the returned value. 
list=[9,3,8,5,1,6,4,2,7]
sorted_list=sorted(list)
reverse_list=sorted(list, reverse= True)
print(sorted_list)
print(reverse_list)

#Using sort method
# Methkod always returns zero as the return value. Sort method will sort the original values of the list
list.sort()
print(list)
list.sort(reverse= True)
print(list)


list=[-8,-6,-4,-3,-1,2,5,7,9]
print(sorted(list))
print(sorted(list, key=abs))
print(sorted(list, key=abs, reverse= True))
