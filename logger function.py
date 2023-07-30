def myLogger(ogFunc):
    import logging
    logging.basicConfig(filename= '{}.log'.format(ogFunc.__name__), level= logging. INFO)
    def wrapper(*args, **kwargs):
        logging.info('Ran with args: {} and kwargs:{}.'.format(args, kwargs))
        return ogFunc(*args, **kwargs)
    return wrapper

@myLogger
def displayInfo(name, age):
    print('my name is {}. I am {} years old.'.format(name, age))

displayInfo('saadik', 13)
