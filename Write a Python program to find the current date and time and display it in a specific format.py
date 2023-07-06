import datetime
import pytz
dt_bangladesh= datetime.datetime.now(tz=pytz.timezone('asia/dhaka'))
print('Current Date: ', dt_bangladesh.strftime('%B, %d, %Y'))
print('Current Time: ', dt_bangladesh.strftime('%I: %M: %S %p'))
