person={'name':'jennie','age':26, 'country':'Korea'}
sentence="hello, my name is {name}. I'm {age} years old. I'm from {country}.".format(**person)
print(sentence)

my_dict={}
n=int(input('Enter the number of value-key pair:'))
for i in range(n):
    key=input("Enter a key:")
    value=input('Enter the value of the key:')
    my_dict[key]=value
print(my_dict)
sentence="hello, my name is {0}. I'm {1} years old. I'm from {2}."
formatted_sentence=sentence.format(*my_dict.values())
print(formatted_sentence)


