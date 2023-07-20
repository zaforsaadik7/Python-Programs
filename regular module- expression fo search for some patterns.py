#finditer() method returns the matches with extra information. findall() will just return the matches with a list. match() method will determine if the regular expression matches at the beggining of the sting.
#search() of we want to search the entire string for a pattern we can we search method

import re
text_to_search = '''
abcsefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa
Metacahratcters(need to be escaped):
_^$*+-?{}[]\()|
saadik.com
Mr smith
Ms davis
Mrs. Rabinson 
Mr. T
321-555-4321
123.555.1234
123*555*1234
900-555-1234
cat 
mat 
bat
'''
sentence = 'start a sentense and then bring it to an end.'
pattern=re.compile(r'')
matches=pattern.finditer(text_to_search)
for match in matches:
    print (match)
pattern= re.compile(r'saadik\.com')
matches=pattern.finditer(text_to_search)
for match in matches:
    print (match)


# If we want to match a phone number with multiple string
pattern=re.compile(r'\d\d\d.\d\d\d.\d\d\d')
#\d will match any digits and the dot will match any type of metacharacters.
matches=pattern.finditer(text_to_search)
for match in matches:
    print (match)

# If we want to match specific metacharacters
pattern=re.compile(r'\d\d\d[-.]\d\d\d[-.]\d\d\d')
matches=pattern.finditer(text_to_search)
for match in matches:
    print (match)


# we can use quantifiers to match more than one character at once
pattern=re.compile(r'\d{3}.\d{3}.\d{4}')
matches=pattern.finditer(text_to_search)
for match in matches:
    print(match)

# If we want to search for a range of numbers or letters
pattern=re.compile(r'[1-5]')
matches=pattern.finditer(text_to_search)
for match in matches:
    print (match)

pattern=re.compile(r'[a-z]')
matches=pattern.finditer(text_to_search)
for match in matches:
    print (match)

pattern= re.compile(r"[a-zA-Z]")
match=pattern.finditer(text_to_search)
for match in match:
    print(match)


# If you use carat "^" within a character set, it'll neglates the set and matches everything that isn't in thar cahracter set.
pattern=re.compile(r'[^b]at')
match=pattern.finditer(text_to_search)
for match in match:
    print(match)


# #To print the names at the last of the string
pattern=re.compile(r'Mr\.?\s[A-Za-z]\w*')
matches= pattern.finditer(text_to_search)
for match in matches:
    print(match)

pattern=re.compile(r'(Mr|Ms|Mrs)\.?\s[A-Za-z]\w*')
matches=pattern.finditer(text_to_search)
for match in matches:
    print(match)


emails='''
CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-321-schafer@my-work.net
'''
pattern=re.compile(r'[a-zA-Z0-9.-]+\@[a-zA-Z-]+\.(com|edu|net)')
matches=pattern.finditer(emails)
for match in matches:
    print(match)


url = '''
https://www.google.com
http://coreyms.com
'''

pattern = re.compile(r'https?://(www\.)?(\w+)\.(\w+)')
matches = pattern.finditer(url)

for match in matches:
    print(match)

#subtitution method
subbed_url=pattern.sub(r'\2\3',url)
print(subbed_url)
# googlecom
# coreymscom

