#A closure is an inner function that remembers and has access to variables in the local scope in which it was created, even after the outer function finished exicuting.
def outer_func():
    msg= "hi there."
    def innerFunc():
        print(msg)
    return innerFunc

myFunc=outer_func()
myFunc()

