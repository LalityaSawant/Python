class Node:

    def __init__(self,data=None):
        self.data = data
        self.next = None

class Stack:

    def __init__(self):
        print('stack created')
        self.stack_pointer = None

    def push(self,x):
        if not isinstance(x,Node):
            x = Node(x)

        if self.is_empty():
            self.stack_pointer = x
        else:
            x.next = self.stack_pointer
            self.stack_pointer = x

    def pop(self):
        if not self.is_empty():
            curr = self.stack_pointer
            self.stack_pointer = self.stack_pointer.next
            curr.next = None
            return curr.data
        else:
            return 'empty list'

    def peak(self):
        return self.stack_pointer.data

    def is_empty(self):
        return self.stack_pointer is None

    def __str__(self):
        to_print = ""
        curr = self.stack_pointer

        while curr is not None:
            to_print += str(curr.data) + ','
            curr = curr.next
        if to_print:
            return '[' + to_print[:-1] + ']'

        return "[]"

my_stack = Stack()
print(my_stack.is_empty())
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)
my_stack.push(4)
print(my_stack)
print(my_stack.is_empty())
print(my_stack.peak())
print(my_stack.pop())
print(my_stack)
