import datetime
my_date=datetime.datetime(2023,6,18,1,48,59)
print(my_date)

update='{:%A,%B %d,%Y}'.format(my_date)
print(update)
statement='Today is {:%B %d,%Y} fell on {:%A} and {:%j} days of the year has passed.'.format(my_date)
print(statement)
