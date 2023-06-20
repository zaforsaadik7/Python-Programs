class Person():
    def __init__(self, name, age):
        self.name= name
        self.age= age
name=input('Enter name:')
age=input('Enter age:')
p1=Person(name,age)

sentence='Hello, everyone. My name is {0.name}. I am {0.age} years old'.format(p1)
print(sentence)
