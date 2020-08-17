from .models import ToDolist,MangedDay
import datetime


def get_priorities(category):
    default_priorities = {
        "Health":1,
        "Office":2,
        "Study":3,
        "Carrer":4
    }
    return default_priorities.get(category,0)


def get_status(status):
    int_status = {
        "Cancelled":0,
        "Pending":1,
        "Inprogress":2,
        "Completed":4
    }
    return int_status.get(status,0)


def create_no_task_day():
    x = datetime.datetime.now()
    HH = 0
    MM = 0
    ampm = 'a.m.'
    todays_date = x.strftime(f"%B %d, %Y")
    start_time = (f'{todays_date} {HH}:{MM} {ampm}')
    end_time = x.strftime("%B %d, %Y 12:30 p.m.")

    while start_time != end_time:
        start_time = (f'{todays_date} {HH}:{MM} {ampm}')
    #print(start_time)
    #create new todoitem
    blank_item = MangedDay(task_start_time=start_time,content = None, status = None, category = None, priority= None)
    #save
    blank_item.save()
    MM += 30
    if MM == 60:
        HH += 1
        MM = 0
        if HH == 12 and ampm == 'a.m.':
            ampm = 'p.m.'
