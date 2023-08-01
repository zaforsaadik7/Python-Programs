def addNum(n):
    def adder(x):
        return n+x
    return adder

a= addNum(int(input('Enter a number: ')))

x= a(int(input("Enter subsequent number passed as an argument: ")))
print(x)
