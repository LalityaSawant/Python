import datetime

x = datetime.datetime.now()
HH = 0
MM = 0
ampm = 'a.m.'
todays_date = x.strftime(f"%B %d, %Y")
start_time = (f'{todays_date} {HH}:{MM} {ampm}')
end_time = x.strftime("%B %d, %Y 11:30 p.m.")

while start_time != end_time:
    start_time = (f'{todays_date} {HH}:{MM} {ampm}')
    print(start_time)
    MM += 30
    if MM == 60:
        if HH == 12 and MM == 60 and ampm == 'p.m.':
            HH = 1
        else:
            HH += 1
        MM = 0
    if HH == 12 and MM == 00 and ampm == 'a.m.':
        ampm = 'p.m.'

print('End')
