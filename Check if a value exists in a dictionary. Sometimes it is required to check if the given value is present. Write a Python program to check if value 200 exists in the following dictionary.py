student={'name':'Jennie','class':'6','age':'12','courses':['math','english','science']}
print(student.get('courses','not found'))
print(student.get('phone','not found'))
if 'name' in student:
    print('name exist in the dictionary')
else:
    print('name does not exist in the dictionary')

if 'phone' in student:
    print('phone exist in the dictionary')
else:
    print('phone does not exist in the dictionary')
