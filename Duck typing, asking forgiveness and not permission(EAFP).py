# Duck typing: In this concept you assume that if something walks like a duck or quacks like a duck then it's a duck. It means, we simply don't care what type of object we are working with.
# We only care if our object can do what we ask it to do.

class Duck:
    def quack(self):
        print("Quack, quack")

    def fly(self):
        print("Flap, Flap!")


class Person:
    def quack(self):
        print("I'm quacking like a duck.")

    def fly(self):
        print("I'm flapping my arms.")


def quack_and_fly(object):
    # Duck-typed (Pythonic)
    object.quack()
    object.fly()

# non pythonic way
# This code is an example of a non-Pythonic way to implement duck typing. Instead of assuming that the object passed to the function has the required methods and calling them directly,
# this code checks for the existence and callability of the methods before calling them. This approach is more verbose and less readable than simply calling the methods directly and handling
# any exceptions that may occur.
def quack_and_fly(thing):
    if hasattr(thing, 'quack'):
        if callable(thing.quack):
            thing.quack()
    if hasattr(thing, 'fly'):
        if callable(thing.fly):
            thing.fly()



#pythonic way
#This code is an example of a more Pythonic way to implement duck typing. Instead of checking for the existence and callability of the methods before calling them, this code simply calls 
# the methods and handles any exceptions that may occur. This approach is more concise and readable than the previous example.
def quack_and_fly(thing):
    try:
        thing.quack()
        thing.fly()
        thing.bark()
    except AttributeError as e:
        print(e)



d = Duck()
quack_and_fly(d)

p = Person()
quack_and_fly(p)

#extented use of asking forgiveness for dictionaries in 
#non pythonic way
person_1={'name':'Maria','age': 23, 'job':'programmer'}
person={'name':'jessica', 'age':21}

if 'name' in person_1 and 'age' in person_1 and 'job' in person_1:
    print("I'm {name}. I'm {age} years old and I'm a {job}.".format(**person_1) )

else:
    print("missing some keys.")


if 'name' in person and 'age' in person and 'job' in person:
    print("I'm {name}. I'm {age} years old and I'm a {job}".format(**person) )

else:
    print("missing some keys.")

#pythonic way
try:
    print("I'm {name}. I'm {age} years old and I'm a {job}.".format(**person_1) )

except KeyError as e:
    print("missinf {} key.".format(e))

try:
    print("I'm {name}. I'm {age} years old and I'm a {job}.".format(**person) )

except KeyError as e:
    print("missinf {} key.".format(e))

##extented use of asking forgiveness for lists in 
# non pythonic way

my_list=[1,2,3,4,5]
if len(my_list)>=6:
    print(my_list[5])
else:
    print("index doesn't exist.")

#pythonic wat
try:
    print(my_list[5])

except IndexError as e:
    print("index doesn't exist.")
