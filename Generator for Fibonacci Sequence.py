def fibonacci(n):
    a= 0
    b=1
    for num in range(n):
        yield a
        a=b
        b=a+b
a=int(input('Enter a number: '))
x= fibonacci(a)
for num in x:
    print(num)
