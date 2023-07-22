import csv
with open ('people.csv','r') as csvfile:
    csv_reader=csv.DictReader(csvfile)

    age_list=[]
    salary_list= []
    working_hour_list=[]
    for line in csv_reader:
        age_list.append(int (line['age']))
        salary_list.append(float (line['salary']))  
        working_hour_list.append(int(line['working hour']))
print(f'Average age: {sum(age_list)/len(age_list)}')
print(f'Maximum age: {max(age_list)}')
print(f'Minimum age: {min(age_list)}')

print(f'Average salary: {sum(salary_list)/len(salary_list)}')
print(f'Maximum salary: {max(salary_list)}')
print(f'Minimum salary: {min(salary_list)}')

print(f'Average working hour: {sum(working_hour_list)/len(working_hour_list)}')
print(f'Maximum working hour: {max(working_hour_list)}')
print(f'Minimum working hour: {min(working_hour_list)}')
