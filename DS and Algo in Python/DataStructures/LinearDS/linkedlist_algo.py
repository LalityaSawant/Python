class Node:

    def __init__(self,data=None):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data) #or f'{self.data}'

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def append_val(self,x):
        '''add x to the end of the list'''
        if not isinstance(x,Node):
            x = Node(x)

        if self.head == None:
            self.head = x
        else:
            self.tail.next = x
        self.tail = x

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

    def add_to_start(self,x):
        '''add x to the left of the list making it head'''
        if not isinstance(x,Node):
            x = Node(x)

        if self.head == None:
            self.head = x
            self.tail = x
        else:
            x.next = self.head
            self.head = x


    def search_val(self, x):
        '''return indices where x was found'''
        curr = self.head
        counter = 0
        while curr is not None:
            if curr.data == x:
                return counter
            else:
                counter += 1
            curr = curr.next


    def remove_val_by_index(self, x):
        '''remove and return value at index x provided as parameter'''
        curr = self.head

        #head remove
        # self.head = curr.next
        # curr.next = None

        #tail remove
        while curr is not None:
            if curr.next == self.tail:
                curr.next = None
            curr = curr.next

    def length(self):
        '''return the length of the list, rep'd by number of nodes'''
        curr = self.head
        counter = 0
        while curr is not None:
            counter += 1
            curr = curr.next
        return counter

    def reverse_list_recur(self, current, previous):
        '''reverse the sequence of node pointers in the linked list'''
        if self.head == None:
            return
        elif current.next == None:
            self.tail = self.head
            current.next = previous
            self.head = current
        else:
            next = current.next
            current.next = previous
            self.reverse_list_recur(next,current)


#callers functions for above project
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
#print(node1)

my_list = LinkedList()
print(my_list)
print('append starts')
print('-------------')

my_list.append_val(node1)
print(my_list)

my_list.append_val(node2)
print(my_list)

my_list.append_val(node3)
print(my_list)

my_list.append_val(node4)
print(my_list)

my_list.append_val(5)
print(my_list)


my_list.reverse_list_recur(my_list.head,None)
print(my_list)

my_new_list = LinkedList()
my_new_list.add_to_start(6)
my_new_list.add_to_start(7)
my_new_list.add_to_start(8)
print(my_new_list)

print(my_new_list.search_val(9))
print(my_new_list.length())
print(my_list.length())

my_new_list.remove_val_by_index(1)
my_new_list.remove_val_by_index(1)
print(my_new_list)
