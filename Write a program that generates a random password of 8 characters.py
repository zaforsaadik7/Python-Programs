#The password should contain at least one uppercase letter, one lowercase letter, one digit, and one special character.
#Use the random module to choose the characters from a string of possible characters.

import random

uppercase = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
lowercase = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
digit = ['1','2','3','4','5','6','7','8','9','0'] #convert integers to string
special_character = ['!','@','#','$','%','&','*','()','_','-','=','+',':',';','/','?','.',',']
# Select one character from each category
password = [random.choice(lowercase), random.choice(uppercase), random.choice(digit), random.choice(special_character)]
# Select remaining characters
remaining_length = 8 - len(password)
remaining_character = uppercase + lowercase + digit + special_character
remaining_password = random.choices(remaining_character, k=remaining_length)
# Combine the selected characters
password += remaining_password
# Shuffle the password
random.shuffle(password)
# Convert the password to a string
str_password = ''.join(password)
print(str_password)
