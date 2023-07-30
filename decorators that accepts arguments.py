

def prefixDec(prefix):
    def decorator(ogFunc):
        def wrapper(*args, **kwargs):
            print(prefix, "Executed before:", ogFunc.__name__)
            result = ogFunc(*args, **kwargs)
            print(prefix, "Executed after:", ogFunc.__name__)
            return result
        return wrapper
    return decorator

@prefixDec("TESTING:")
def personInfo(name, age):
    print('Your name is {}. And you are {} years old.'.format(name, age))

personInfo('zafor saadik', 21)
