import datetime

# The time method takes inputs: hours and minutes
mytime = datetime.time(2,20)

print(mytime.minute)

print(mytime.hour)

print(mytime)

print()

today = datetime.date.today()

print(today)

print(today.year)

print(today.ctime())

print()

mydatetime = datetime.datetime(2021, 10, 3, 14, 20, 1)

print(mydatetime)

mydatetime.replace(year= 2020)

print(mydatetime)

# DATE

date1 = datetime.date(2021, 11, 3)
date2 = datetime.date(2020, 11, 3)

result = date1 - date2

print(type(result))

print(result)

#                          year, month, day, hours, minutes
datetime1 = datetime.datetime(2021, 11, 3, 22, 0)
datetime2 = datetime.datetime(2020, 11, 3, 12, 0)

print(datetime1 - datetime2)