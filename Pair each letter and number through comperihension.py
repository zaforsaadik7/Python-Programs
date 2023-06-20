pair=[]

for  num in range (1,4):
    for letter in 'abcd':
        pair.append((letter, num))
print(pair)

comperihension=[]
comperihension=[(letter,num) for letter in 'abcd' for num in range(1,4)]
print(comperihension)
