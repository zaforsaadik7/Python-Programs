import random
value = random.random()
print('random method value:', value)

# Using uniform method, we can set a range to get random values within the range
value = random.uniform(1, 10)
print('uniform method value:', value)

# To get innteger number
value = random.randint(1, 6)
print('integer value:', value)
# Here 1 and 6 both are incllusive

# Choice method picks a random value from a list of values.
greetings = ['Hi', 'Hello', 'Hey', 'Howdy', 'Hola']
value = random.choice(greetings)
print(value+', saadik.How are you?')

#It's poddible to get multiple random values from a list. To do that instead of using choice we'll use choices.
colors=['red','green','blue']
result=random.choices(colors, k=10)
#k=number of multiple choice
print(result)
#Now we can controll the random selection through weight, where we'll give a number of probability for each value to select randomly.
result=random.choices(colors,weights=[6,6,5],k=10)
print(result)
#How to shuffle a list of number randomly
deck=list(range(1,53))
#print(deck)
random.shuffle(deck)
print(deck)
#Now we want to shuffle between 5 of the cards. To do this we won't use choices method because it can select same number multiple time, for that we are going to use sample method.
hand=random.sample(deck,k=5)
print(hand)
