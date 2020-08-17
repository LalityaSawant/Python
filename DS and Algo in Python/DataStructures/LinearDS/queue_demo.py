class Node:

    def __init__(self,data=None):
        self.data = data
        self.next = None

class Queue:

    def __init__(self):
        print('queue created')
        self.head = None
        self.tail = None

    def add(self,x):
        if not isinstance(x,Node):
            x = Node(x)

        if self.head == None:
            self.head = x
        else:
            self.tail.next = x

        self.tail = x

    def remove(self):
        if not self.is_empty():
            curr = self.head
            self.head = self.head.next
            curr.next = None
            return curr.data
        else:
            return 'queue list'


    def peak(self):
        if self.is_empty:
            return None

        return self.head.data

    def is_empty(self):
        return self.head == None

    def __str__(self):
        #return "[]"
        #[5-->4-->10-->1] we have to construct list here
        to_print = ""
        curr = self.head
        while curr is not None:
            to_print += str(curr.data) + ','
            curr = curr.next
        if to_print:
            return "["+to_print[:-1]+"]"
        else:
            return "[]"

my_queue = Queue()
print(my_queue.is_empty())
print(my_queue.peak())
my_queue.add(1)
my_queue.add(2)
my_queue.add(3)
my_queue.add(4)
print('after add:' + str(my_queue))
my_queue.remove()
print('after remove:' + str(my_queue))
my_queue.add(5)
print('after add:' + str(my_queue))
my_queue.remove()
my_queue.remove()
print('after remove:' + str(my_queue))
my_queue.add(6)
print('after add:' + str(my_queue))


print(my_queue)
