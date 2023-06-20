person_1=['Jennie',26]
person_2=['Lisa',24]
sentense='{0[0]} and {1[0]} are close friend.{0[0]} is {0[1]} years old and {1[0]} is {1[1]} years old'.format(person_1,person_2)
print(sentense)

friend_1=[]
friend_2=[]

n=int(input('Enter the number of the input for the first list:'))
m=int(input('Enter the number of the input for the second list:'))
for i in range(n):
    value=input('Enter the value of the first list:')
    friend_1.append(value)
print(friend_1)

for i in range(m):
    value=input('Enter the value of the second list:')
    friend_2.append(value)
print(friend_2)
sentense='{0[0]} and {1[0]} are close friend.{0[0]} is {0[1]} years old and {1[0]} is {1[1]} years old'.format(friend_1,friend_2)
print(sentense)
