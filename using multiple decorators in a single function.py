from functools import wraps

def myLogger(ogFunc):
    import logging
    logging.basicConfig(filename= '{}.log'.format(ogFunc.__name__), level= logging. INFO)
    @wraps(ogFunc)
    def wrapper(*args, **kwargs):
        logging.info('Ran with args: {} and kwargs:{}.'.format(args, kwargs))
        return ogFunc(*args, **kwargs)
    return wrapper

def timer(ogFunc):
    import time
    @wraps(ogFunc)
    def wrapper(*args, **kwargs):
        t1=time.time()
        result= ogFunc(*args, **kwargs)
        t2= time.time()- t1
        print('{} ran in: {} seconds.'.format(ogFunc.__name__, t2))
        return result
    return wrapper
import time
@myLogger
@timer
def displayInfo(name, age):
    time.sleep(1)
    print('my name is {}. I am {} years old.'.format(name, age))

print(displayInfo.__name__)
displayInfo('saad kibriya', 26)
