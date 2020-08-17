# tuples are immutable

my_random_tuple = ('first',1,7,6,4,5,8,'hi there',2,3,1,5,2,1,9,10)
my_tuple =('first_value','second_value','third_value')

print(my_random_tuple[0])
print(my_random_tuple[-1])
print(my_random_tuple[::-1])#reverse view

print(len(my_random_tuple))
print(my_random_tuple.count(5))

print(my_random_tuple.index('hi there'))
