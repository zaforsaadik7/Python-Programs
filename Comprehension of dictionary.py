name = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
hero = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']

my_dict = {}
for n, h in zip(name, hero):
    my_dict[n] = h
print(my_dict)

# Issue: Reusing the variable name 'name' in the loop overwrites the original 'name' list.
# This causes unexpected behavior in the comprehension below.

# Using dictionary comprehension
dictionary = {n: h for n, h in zip(name, hero)}
print(dictionary)
