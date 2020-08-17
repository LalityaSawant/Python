class Task:
    """ General class for holding Task object"""


    def __init__(self, task_name):
        self.task_name = task_name
        self.task_type = None
        # self.when = None
        self.eta = None
        self.time_required = None
        self.task_reviewed = False
        self.task_status = 'New'  # for tickler status updates
        self.delegated = None
        self.reminder = None

    def __str__(self):
        return "Bucket: {0.task_type}\t Task: {0.task_name}\t  Expected Completion:{0.eta}\t " \
               "Status: {0.task_status}\t Delegated To: {0.delegated}\t " \
               "Status Check Reminder: {0.reminder}".format(self)


class TaskList:

    def __init__(self):
        self.task_list = []

    def add_tasks(self, task):
        new_task = Task(task)
        self.task_list.append(new_task)

    def get_tasks_to_review(self):
        review_list = []
        for list_item in self.task_list:
            if not list_item.task_reviewed:
                review_list.append(list_item)
        return review_list

    def get_tasks(self):
        return self.task_list

    def remove_task(self, task):
        self.task_list.remove(task)


def review_update_type(add_to_list, task):
    """ General method to update the task once its reviewed

        add_to_list(str): name of list the task should be categorized
        task(Task): object task passed from the client to process
    """
    task.task_type = add_to_list
    task.task_reviewed = True


months = {'01': 'Jan', '1': 'Jan', 'January': 'Jan',
          '02': 'Feb', '2': 'Feb', 'February': 'Feb',
          '03': 'Mar', '3': 'Mar', 'March': 'Mar',
          '04': 'Apr', '4': 'Apr', 'April': 'Apr',
          '05': 'May', '5': 'May', 'May': 'May',
          '06': 'Jun', '6': 'Jun', 'June': 'Jun',
          '07': 'Jul', '7': 'Jul', 'July': 'Jul',
          '08': 'Aug', '8': 'Aug', 'August': 'Aug',
          '09': 'Sep', '9': 'Sep', 'September': 'Sep',
          '10': 'Oct', 'October': 'Oct',
          '11': 'Nov', 'November': 'Nov',
          '12': 'Dec', 'December': 'Dec'
          }


def schedule():
    month = None
    mon = input("Month: ")
    if mon in months:
        month = months[mon]
    day = input("Day of {} ".format(month))
    year = input("Year for {}-{} ".format(month, day))
    return "{}-{}-{}".format(month, day, year)


if __name__ == "__main__":
    print('''
    Welcome to (G)etting (T)hings (D)one Project - GTD
    1. Enter your thoughts
    2. Review your thoughts''')
    my_task_list = TaskList()

    while True:
        print("")
        print('''Please choose from the options below
        * Press 1 to enter your thoughts/todo's/events/ideas/projects etc
        * Press 2 to start reviewing your items
        * Press 3 to view your items
        * Press 9 to Exit application''')

        selection = input("-->  ")

        try:
            entry = int(selection)
        except ValueError:
            print("Please enter a number between 1 and 2")
            continue

        if entry == 1:
            print("Do you want to enter Multiple Thoughts?")
            selection = input("<'Y' OR 'N'> ").capitalize()

            if selection == 'Y':
                while True:
                    my_task = input("Your thought--> ")
                    if my_task == ' ' or my_task == '':
                        break
                    my_task_list.add_tasks(my_task)

            else:
                my_task = input("Your thought--> ")
                my_task_list.add_tasks(my_task)
            print("Thanks for capturing your ideas,thoughts,todo's etc...")
            print('-' * 50)

        elif entry == 2:
            print("We will be reviewing your items for prioritisation !!")
            for item in my_task_list.get_tasks_to_review():
                print("")
                print(item.task_name)
                actionable = input("Is this task actionable? <'Y' OR 'N'> ").capitalize()
                if actionable == 'N':
                    actionable = input("Does this task belongs to a wish list? <'Y' OR 'N'> ").capitalize()
                    if actionable == 'N':
                        reference = input("Is this task for reference or information sake? <'Y' OR 'N'> ").capitalize()
                        if reference == 'N':
                            delete = input("Can we delete this for good? <'Y' OR 'N'> ").capitalize()
                            if delete == 'Y':
                                print("{} removed".format(item.task_name))
                                my_task_list.remove_task(item)
                            else:
                                review_update_type('ReviewLater', item)
                        else:
                            review_update_type('Ref-Information', item)
                    else:
                        review_update_type('SomeDayMayBe', item)
                else:
                    review_update_type('TODO', item)
                    project = input("Is it a project.. means you need more tasks to do this one task?  <'Y' OR 'N'> ")\
                        .capitalize()
                    if project == 'N':
                        minimal_task = input("Does it takes less than 2 min do do it?  <'Y' OR 'N'> ").capitalize()
                        if minimal_task == 'Y':
                            review_update_type('QuickDoIt', item)
                        else:
                            delegate = input("Can it be delegated to some one?  <'Y' OR 'N'> ").capitalize()
                            if delegate == 'Y':
                                review_update_type('Delegated', item)
                                delegated_to = input("Whom to delegate").lower()
                                item.delegated = delegated_to
                                print("When he needs to complete ")
                                item.eta = schedule()
                                set_reminder = input("Do you need reminder to check on this with {}?  <'Y' OR 'N'> "
                                                     .format(delegated_to)).capitalize()
                                if set_reminder == 'Y':
                                    print("When to ask {} for status?".format(delegated_to))
                                    item.reminder = schedule()
                                else:
                                    pass  # Do nothing
                            else:
                                meeting_event = input("Is this a meeting or event?  <'Y' OR 'N'> ").capitalize()
                                if meeting_event == 'Y':
                                    review_update_type('EventMeeting', item)
                                    planned = input(" is it already planned?  <'Y' OR 'N'> ").capitalize()
                                    if planned == 'Y':
                                        review_update_type('Event-Planned', item)
                                        print("When is this event?")
                                        item.time_required = schedule()
                                    else:
                                        wish_to_plan = input("Do you like to plan it now? <'Y' OR 'N'> ").capitalize()
                                        review_update_type('Event-UnPlanned', item)
                                        if wish_to_plan == 'Y':
                                            review_update_type('Event-Planned', item)
                                            print("When would you like plan this event for?")
                                            item.time_required = schedule()
                                else:
                                    review_update_type('NextAction-UnPlanned', item)
                                    print("Lets set some time of completion for this task")
                                    eta_setting = input("Do you wish to do it now?  <'Y' OR 'N'> ").capitalize()
                                    if eta_setting == 'Y':
                                        item.eta = schedule()
                                        review_update_type('NextAction-Planned', item)
                    else:
                        review_update_type('Project', item)
                        # TODO: create a list of task list or a project list

        elif entry == 3:
            print("Your tasks...")
            print("")
            for item in my_task_list.get_tasks():
                print(item)

        elif entry == 9:
            print("Exiting program... Thanks!")
            break

        else:
            print("Not a valid choice...")
