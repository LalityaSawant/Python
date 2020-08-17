class Tasks:

    def __init__(self, name, type=None, when=None, eta=None, required_time=None):
        self.name = name
        self.type = type
        self.when = when
        self.eta = eta
        self.required_time = required_time

class Tasks_list:

    def __init__(self, task):
        self.task_list = []

    def add_tasks(self):
        self.task_list.append(task)

if __name__ = __main__:
    my_task = Tasks(input("Enter a task: "))
    print(my_task)
