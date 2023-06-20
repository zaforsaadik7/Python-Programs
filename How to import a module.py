#Importing a written module
import my_module

#using a function of the module in this script
name=['Hamim', 'John', 'Nethon' ,'Jennie', 'Farhan', 'Dilip', 'Nafisa']
index=my_module.find_index(name, 'Jennie')
print(index)

#importing a module in a custome name
import my_module as m
index=m.find_index(name,'Farhan')
print(index)

#How to import just the function from the module
from my_module import find_index, test
index= find_index(name,'Nethon')
print (index)
print(test)
