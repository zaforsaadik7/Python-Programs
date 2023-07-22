import csv

#read csv file
with open ('names.csv', 'r') as csv_file:
    csv_reader= csv.reader(csv_file)

    for line in csv_reader:
        print(line) 
        print(line[2])


#write csv file
with open ('names.csv','r') as csv_file: 
    csv_reader= csv.reader(csv_file)
    with open ('name2.csv', 'w') as new_csv_file:
        csv_writer= csv.writer(new_csv_file, delimiter= '-')
        for line in csv_reader:
            csv_writer.writerow(line)


#for reading, if you use any other delimiter other than comma. You've to pass in the delimiter.
with open ('name2.csv', 'r') as csv_file:
    csv_reader= csv.reader(csv_file, delimiter= '-')
    for line in csv_file :
        print(line)

#working with csv data within dictionary reader or writer 
with open ('names.csv', 'r') as csv_file:
    csv_reader= csv.DictReader(csv_file)
    for line in csv_reader:
        email= line['email'] 
        #this will access the specific key name email on the dictionaries of the csv file
        print(email)

#dictionary writer 
import csv

with open ('names.csv', 'r') as csv_file:
    csv_reader=csv.reader(csv_file)

    with open('names_dict.csv', 'w') as new_file:
        fieldnames=['First Name', 'Last Name', 'Email']
        csv_writer= csv.DictWriter(new_file, fieldnames= fieldnames)
        csv_writer.writeheader()
        for line in csv_reader:
            csv_writer.writerow({'First Name': line[0], 'Last Name': line[1], 'Email': line[2]})
