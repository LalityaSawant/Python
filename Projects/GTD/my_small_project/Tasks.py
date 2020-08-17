class Tasks:

    def __init__(self, task_name, task_type=None, when=None, eta=None, time_required=None):
        self.task_name = task_name
        self.task_type = task_type
        self.when = when
        self.eta = eta
        self.time_required = time_required


class TaskList:

    def __init__(self):
        self.task_list = []

    def add_tasks(self, task):
        new_task = Tasks(task)
        self.task_list.append(new_task)

    def get_tasks(self):
        return self.task_list


if __name__== "__main__":
    my_task_list = TaskList()
    while True:
        my_task = input("Enter your task: ")
        print(my_task)
        if my_task == ' ' or my_task == '':
            break
        my_task_list.add_tasks(my_task)

    for item in my_task_list.get_tasks():
        print(item.task_name, item.task_type, item.when, item.eta, item.time_required, sep='-')

