#STRING  FORMATING
tag='h1'
text='this is a heading.'
sentence='<{0}>{1}/<{0}>'.format(tag,text)
print(sentence)


greeting=input('Enter greeting:')
name=input('Enter a name:')
sentence='{0},{1}.How can I help you today?'.format(greeting,name)
print(sentence)
