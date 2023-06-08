def prime_number(string):
    list=string.split(',')
    list=[int(num) for num in list]
    print(list)
    prime=[]
    for num in list:
        is_prime = True
        for i in range(2,num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            prime.append(num)
    return prime
input_string=input('enter some numbers:')
print(prime_number(input_string))
