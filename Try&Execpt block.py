# If we can anticipate sections of our code that might throw an error, then we can use the try and except blocks to handle them in a way we want.
try:
    f = open("textfile.txt")
except FileNotFoundError as e:
    print(e)
    #print("File not found.")

# If the file doesn't give an error and we want to execute the file, we'll use 'else'
else:
    print(f.read())
    f.close()

# If we want to run the file no matter what, whether the code is successful or not. We'll use "finally" clause.
finally:
    print("Executing finally.")

# If you need to raise an exception on your own then you need to do this. It will raise an exception even though the file does exist.
try:
    f = open('text.txt')
    if f.name == 'text.txt':
        raise Exception
except Exception as e:
    print(e)
    print("An exception occurred.")
