#A decorators is a function that takes another function as an aargument and add some kind of functionality and returns another function. All of this is without altering the source code that you have passed in.
def decorator(ogFunc):
    def wrapperFunc(*args,**kwargs): #It'll allow us to take any amount of arguments
        print('this is how you modify the original fuction without altering the code.')
        return ogFunc(*args, **kwargs)
    return wrapperFunc

def display():
    print('The display function has been exicuted.')

variable= decorator(display)
variable()

@decorator #variableNew= decorator(displayNew)
def displayNew():
    print('this is another way to exicute a decorator.')
displayNew()

@decorator
def displayInfo(name, age):
    print('my name is {}. I am {} years old.'.format(name, age))

displayInfo('saadik', 13)
