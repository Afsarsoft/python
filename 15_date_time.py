# pyright: strict

#  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#   Working with date and time
#  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# pyright is giving error for pytz!, investigate later
#import pytz
from datetime import date, datetime, timedelta

#  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# from datetime import datetime
now: datetime = datetime.now()
formatted_now: str = now.strftime("%Y-%m-%d %H:%M:%S")
message: str = f'Current date and time: {formatted_now},\n'
message += f'Year={now.year}, Month={now.month}, Day={now.day},\n'
message += f'Hour={now.hour}, Minute={now.minute}, Second={now.second}'
print(message)
#  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# from datetime import date, datetime
some_date_input: str = '05/18/1999'
some_date: date = datetime.strptime(some_date_input, "%m/%d/%Y")
print(f'some_date_input = {some_date_input} and some_date = {some_date}')


#  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# from datetime import date
some_date: date = date(2018, 2, 25)
print(f'some_date is {some_date}')


#  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# from datetime import date
today: date = date.today()
print(f'Today = {today}')
print(f"Today's year = {today.year}")
print(f"Today's month = {today.month}")
print(f"Today's day = {today.month}")
print(f'today.weekday() is {today.weekday()}')    # Monday 0 - Sunday 6
print(f'today.isoweekday() is {today.isoweekday()}')  # Monday 1 - Sunday 7
#  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


#  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# from datetime import date, timedelta
today: date = date.today()
delta: timedelta = timedelta(days=7)
week_next_today: date = today + delta
week_last_today: date = today - delta
print(f"Today's date = {today} and week from today is {week_next_today}")
print(f"Today's date = {today} and last week was {week_last_today}")
#  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
my_time: datetime = datetime(year=1965, month=2, day=28, hour=9,
                             minute=30, second=45, microsecond=100000)
print(f'my_time = {my_time}')
print(type(my_time))

print(f'my_time.year = {my_time.year}')
print(f'my_time.month = {my_time.month}')
print(f'my_time.day = {my_time.day}')
print(f'my_time.hour =  {my_time.hour}')
print(f'my_time.minute =  {my_time.minute}')
print(f'my_time.second = {my_time.second}')
print(f'my_time.microsecond = {my_time.microsecond}')
#  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


#  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# from datetime import datetime
today_time: datetime = datetime.today()

print(f'today_time= {today_time}')
print(type(today_time))

print(f'today_time.year = {today_time.year}')
print(f'today_time.month  = {today_time.month}')
print(f'today_time.day =  {today_time.day}')
print(f'today_time.hour = {today_time.hour}')
print(f'today_time.minute = {today_time.minute}')
print(f'today_time.second = {today_time.second}')
print(f'today_time.microsecond = {today_time.microsecond}')
#  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


#  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# from datetime import datetime
today_time: datetime = datetime.today()
now_time = datetime.now()  # similar to today() and option to pass zone time
now_time_utc = datetime.utcnow()  # current UTC time

print(f'today_time = {today_time}')
print(f'now_time = {now_time}')
print(f'now_time_utc = = {now_time_utc}')
#  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


'''
#  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Surush, work on this later
#  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# python -m pip install pytz
# from datetime import datetime
# import pytz
now_pacific = datetime.now()  # Got a none aware time zone
print(now_pacific)

# Simply convert it
dt_eastern = dt_pacific.astimezone(pytz.timezone('US/Eastern'))
print(dt_eastern)

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# For above, we used to go through the following workaround
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Got a none aware time zone
dt_pacific = datetime.datetime.now()

# Get a timezone
pacific_tz = pytz.timezone('US/Pacific')
print(pacific_tz)

# localizing it
dt_pacific = pacific_tz.localize(dt_pacific)
print(dt_pacific)

# Convert it
dt_eastern = dt_pacific.astimezone(pytz.timezone('US/Eastern'))
print(dt_eastern)

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Displaying the datetime
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Curret datetime with timezone aware
dt_pacific = datetime.datetime.now(tz=pytz.timezone('US/Pacific'))

# For complete list, take a look at https://docs.python.org/2/library/datetime.html#strftime-strptime-behavior

print(dt_pacific.strftime('%B %d, %Y'))  # December 26, 2018
print(dt_pacific.strftime('%m/%d/%Y'))  # 12/26/2018
print(dt_pacific.strftime('%m/%d/%Y, %H:%M:%S'))  # 12/26/2018, 14:35:15
print(dt_pacific.strftime('%H:%M:%S'))  # 14:35:15

print(dt_pacific.strftime('%d %b, %Y'))  # 26 Dec, 2018
print(dt_pacific.strftime('%d %B, %Y'))  # 26 December, 2018
print(dt_pacific.strftime('%I%p'))  # 02PM
print(dt_pacific.strftime('%I:%M, %p'))  # 02:39, PM

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Coverting datetime to string and string to the datetime
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Curret datetime with timezone aware
dt_pacific = datetime.datetime.now(tz=pytz.timezone('US/Pacific'))
print(dt_pacific)
print(type(dt_pacific))

# strftime -> Datetime to String
# Coverting datetime to string
dt_str = dt_pacific.strftime('%B %d, %Y')
print(dt_str)
print(type(dt_str))

# strptime -> String to Datetime
dt = datetime.datetime.strptime(dt_str, '%B %d, %Y')
print(dt)
print(type(dt))
'''
