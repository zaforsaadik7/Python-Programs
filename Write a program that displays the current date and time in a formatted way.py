import datetime
import pytz
#for tz in pytz.all_timezones:
    #print(tz)
dt_now=datetime.datetime.now(tz=pytz.timezone('Asia/Dhaka'))
current_time=datetime.datetime.now().time()
current_date=dt_now.strftime('%B,%d,%y')
print('Today is {}. The time is {}'.format(current_date,current_time))


