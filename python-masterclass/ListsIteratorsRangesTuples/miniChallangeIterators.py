# iterating a list by suing next

my_list = [1,2,3,4,5,6,7,8,9,0]

my_iterator = iter(my_list)

for i in range(0, len(my_list)):
    next_item = next(my_iterator)
    print(next_item)
