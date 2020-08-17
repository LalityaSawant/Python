class Tasks:

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
        return "Task {0.task_name}\t List {0.task_type}\t expected completion {0.eta}".format(self)


class TaskList:

    def __init__(self):
        self.task_list = []

    def add_tasks(self, task):
        new_task = Tasks(task)
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
                print(item.task_name)
                actionable = input("Is this task actionable ? <'Y' OR 'N'> ").capitalize()
                if actionable == 'N':
                    actionable = input("Does this task belongs to a wish list ? <'Y' OR 'N'> ").capitalize()
                    if actionable == 'N':
                        reference = input("Is this task for reference or information sake ? <'Y' OR 'N'> ").capitalize()
                        if reference == 'N':
                            delete = input("Can we delete this for good ? <'Y' OR 'N'> ").capitalize()
                            if delete == 'Y':
                                print("{} removed".format(item.task_name))
                                my_task_list.remove_task(item)
                            else:
                                # print("Review later list Thanks!")
                                print("")
                                item.task_type = 'Review Later'
                                item.task_reviewed = True
                        else:
                            # print("Information list Thanks!")
                            print("")
                            item.task_type = 'Reference-Information'
                            item.task_reviewed = True
                    else:
                        # print("SomeDayMayBe list Thanks!")
                        print("")
                        item.task_type = 'SomeDayMayBe'
                        item.task_reviewed = True
                else:
                    print("")
                    item.task_type = 'TODO'
                    item.task_reviewed = True
                    project = input("Is it a project.. means you need more tasks to do this one task ?").capitalize()
                    if project == 'N':
                        minimal_task = input("Does it takes less than 2 min do do it ?").capitalize()
                        if minimal_task == 'Y':
                            item.task_type = 'Quick-DoIT'
                            item.task_reviewed = True
                        else:
                            delegate = input("Can it be delegated to some one ?").capitalize()
                            if delegate == 'Y':
                                item.task_type = 'Delegated'
                                item.task_reviewed = True
                                delgated_to = input("Whom to delegate").lower()
                                item.delegated = delgated_to
                                print("When he needs to complete ")
                                month = input("Month: ")
                                day = input("Day of {} ".format(month))
                                year = input("Year for {}-{} ".format(month, day))
                                item.eta = "{}-{}-{}".format(month, day, year)
                                set_reminder = input("Do you need reminder to check on this with {} ?"
                                                     .format(delgated_to)).capitalize()
                                if set_reminder == 'Y':
                                    print("When to ask {} for status?".format(delgated_to))
                                    month = input("Month: ")
                                    day = input("Day of {} ".format(month))
                                    year = input("Year for {}-{} ".format(month, day))
                                    item.reminder = "{}-{}-{}".format(month, day, year)
                                else:
                                    pass  # Do nothing
                            else:
                                meeting_event = input("Is this a meeting or event ?").capitalize()
                                if meeting_event == 'Y':
                                    item.task_type = 'Event'
                                    item.task_reviewed = True
                                    planned = input(" is it already planned ?").capitalize()
                                    if planned == 'Y':
                                        item.task_type = 'Event-Planned'
                                        print("When is this event?")
                                        month = input("Month: ")
                                        day = input("Day of {} ".format(month))
                                        year = input("Year for {}-{} ".format(month, day))
                                        item.time_required = "{}-{}-{}".format(month, day, year)
                                    else:
                                        wish_to_plan = input("Do you like to plan it now ?").capitalize()
                                        if wish_to_plan == 'Y':
                                            item.task_type = 'Event-Planned'
                                            print("When would you like plan this event for?")
                                            month = input("Month: ")
                                            day = input("Day of {} ".format(month))
                                            year = input("Year for {}-{} ".format(month, day))
                                            item.time_required = "{}-{}-{}".format(month, day, year)
                                        else:
                                            item.task_type = 'Event-UnPlanned'
                                else:
                                    item.task_type = 'NextAction'
                                    item.task_reviewed = True
                                    print("Lets set some time of completion for this task")
                                    eta_setting = input("Do you wish to do it now ?").capitalize()
                                    if eta_setting == 'Y':
                                        month = input("Month: ")
                                        day = input("Day of {} ".format(month))
                                        year = input("Year for {}-{} ".format(month, day))
                                        item.eta = "{}-{}-{}".format(month, day, year)
                                    else:
                                        item.task_type = 'NextAction-UnPlanned'
                                        item.task_reviewed = True
                    else:
                        pass
                        # TODO: create a list of task list or a project list

        elif entry == 3:
            print("Your tasks...")
            print("")
            print("Task List\t\tTask\t\tComplete by\t\tStatus\t\tDelegated To\t\tRemind for status")
            for item in my_task_list.get_tasks():
                print("{}\t\t{}\t\t{}\t\t{}\t\t{}\t\t{}".
                      format(item.task_type,item.task_name, item.eta,
                             item.task_status, item.delegated, item.reminder))

        elif entry == 9:
            print("Exiting program...")
            break

        else:
            print("Only 1/2 and 9 are valid choices")
