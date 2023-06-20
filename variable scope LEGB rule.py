#How to set a value for the global variable from within the function
x='global variable.'
print(x)
def test():
    global x
    x='Converted within the function.'
    print(x)
test()
print(x)

#How to import and see the built-in functions

import builtins
print(dir(builtins))

#Enclosing function: It has to do with nested function

def outer():
    x='outer x.'
    def inner():
        print(x)
    inner()
    print(x)

outer()
