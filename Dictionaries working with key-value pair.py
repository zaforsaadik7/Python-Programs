student={'name':'john','age':25,'courses':['math','physics']}
print(student)
print (student.get('courses'))
print(student.get('phone','not found'))
student['phone']='0123456789'
student['name']='Jennie'
print(student)
student.update({'courses':['arts','literature','grammer','accounting'], 'name':'Omar'})
print(student)
print(len(student))
print(student.keys())
print(student.values())
print(student.items())
for keys in student:
    print(keys)


del student['age']
courses=student.pop('courses')
print(student)
print(courses)



for key,values in student.items():
    print(key,values)
for key, values in enumerate(student):
    print(key,values)
