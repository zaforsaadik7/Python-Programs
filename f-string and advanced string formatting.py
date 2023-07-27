#We can run functions and methods directly within f-string 
first_name= "Emam"
last_name= 'Zafor'
sentence= f'My name is {first_name} {last_name}.'
print (sentence)

sentence= f'My name is {first_name.upper()} {last_name.upper()}.'
print (sentence)

person= {'name': 'John', 'age': '39'}
sentence= f"My name is {person['name']} and I am {person['age']} years old."
print(sentence)

print(f'4 times 11 is eqauls to {4*11}')

for n in range (1, 11):
    print(f'the value is {n:02} and {n+1}')

pi=3.14159265
print(f'the value of pi is equals to {pi:04}')

from datetime import datetime
birthday= datetime(1990,1,12)
print(f"Jenn's birthday is on {birthday: %B, %d, %Y}.")
