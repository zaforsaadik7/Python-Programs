string= input('Enter a string to count the number of vowels:')
string= string.strip()
word_list= string.split(' ')
c=0
for word in word_list:
    for letter in word:
        if letter.lower() in 'aeiou':
            c+= 1
print(c)
