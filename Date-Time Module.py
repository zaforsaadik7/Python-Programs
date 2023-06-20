import datetime

# NIAVE TIME 
# Get the current date and time
current_datetime = datetime.datetime.today()
print(current_datetime)

# Get only the current date
current_date = datetime.date.today()
print(current_date)

# Get only the current time
current_time = datetime.datetime.now().time()
print(current_time)

# Get the current month
current_month = datetime.date.today().month
print(current_month)

# Get the current year
current_year = datetime.date.today().year
print(current_year)

#Get the day of the week 
current_day_of_the_week=datetime.datetime.today().weekday()
print(current_day_of_the_week) #for weekday method week starts with monday=0....sunday=6

current_iso_weekday=datetime.datetime.today().isoweekday()
print(current_iso_weekday)   #for isoweekday method week starts with monday=1....sunday=7

# Uses of time delta
tday=datetime.date.today()
tdelta=datetime.timedelta(days=7)
print(tday+tdelta)

#Using datetime find out how many days are left till my brithday
bday=datetime.date(2023,12,12)
till_bday=bday-tday
print(till_bday.days,'days are left till my birthday.')

#How to use time method for naive time
t=datetime.time(10,46,45,10000)
print(t)
print(t.hour)

#How to input both date and time
dt=datetime.datetime(2023,6,20,10,49,47,100000)
print(dt)
print(dt.time())
print(dt.date())

dt_today=datetime.datetime.today()
print(dt_today) #It returns the current local time with a time zone set to none.
dt_now=datetime.datetime.now()
print(dt_now) #It gives an option to pass a time zone but if you don't then dt_today and dt_now are the same.
dt_UTC=datetime.datetime.utcnow()
print(dt_UTC) # It gives us the UTC time but the UTC info is set to none.

#AWARE DATETIME
import pytz

dt=datetime.datetime(2023,6,20,11,17,50,10000,tzinfo=pytz.UTC)
print(dt)
dt_now=datetime.datetime.now(pytz.UTC)
print(dt_now)
dt_utcnow=datetime.datetime.today().replace(tzinfo=pytz.UTC)
print(dt_utcnow)
# Aware time for bangladesh
dt_bangladesh=datetime.datetime.now(tz=pytz.UTC).astimezone(pytz.timezone())
print(dt_bangladesh)

#How to see the time zones
for tz in pytz.all_timezones:
    print(tz)

#Convert naive datetimme to aware datetime
dt=datetime.datetime.now()
print(dt)
bn_tz=pytz.timezone('Asia/Dhaka')
dt=bn_tz.localize(dt)
print(dt)

dt=datetime.datetime(2023,6,20,11,52,53,100000)
print(dt)
bn_tz=pytz.timezone()
dt=bn_tz.localize(dt)
print(dt)

# Convertion of a string to a datetime and make it aware 
dt_str = input("Enter a date (name of the month, date, year( June,20,23)): ")
dt = datetime.datetime.strptime(dt_str, "%B,%d,%y")
print(dt)

tz = pytz.timezone('Asia/Dhaka')
dt_localized = dt.astimezone(tz)
print(dt_localized)

#Convert datetime to string
print(dt_localized.strftime('%B,%d,%y'))

# Displaying datetime in iso format
dt=datetime.datetime.now(tz=pytz.timezone('Asia/Dhaka'))
print(dt.isoformat())
