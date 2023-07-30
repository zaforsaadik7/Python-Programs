def timer(ogFunc):
    import time
    def wrapper(*args, **kwargs):
        t1=time.time()
        result= ogFunc(*args, **kwargs)
        t2= time.time()- t1
        print('{} ran in: {} seconds.'.format(ogFunc.__name__, t2))
        return result
    return wrapper

import time
@timer
def displayInfo(name, age):
    time.sleep(1)
    print('my name is {}. I am {} years old.'.format(name, age))

displayInfo('saadik', 13)
