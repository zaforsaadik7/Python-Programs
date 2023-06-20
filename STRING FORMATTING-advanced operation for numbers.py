for i in range (1,11):
    a='{:02}'.format(i)
    print(a)

pi=3.14159265
a='{:.4f}'.format(pi)
print(a)

statement='1GB is equal to {:,.2f} bytes'.format(1000000)
print(statement)
