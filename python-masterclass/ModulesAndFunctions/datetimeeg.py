import time
import datetime

print(time.gmtime())

time_here = time.localtime()
print(time_here)

year = time_here[0]
print(year)

print("local time is " + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))

print(time.timezone/60/24)

print(datetime.datetime.today())
print(datetime.datetime.utcnow())
print(datetime.datetime.now())