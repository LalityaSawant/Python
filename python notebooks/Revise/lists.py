my_list = [1,2,3]

my_list = ['String',100,23.2]

print(len(my_list))
my_list = ['One','Two','Three']

print(my_list[0])

print(my_list[1:])

another_list = ['four','five']

print(my_list+another_list)

new_list = my_list+another_list

print(new_list)

my_string = 'One'

print(my_string[0])

#my_string[0] = 't' we cannot do this

new_list[0] = 'ONE ALL CAPS'
print(new_list)

new_list.append('SIX')

print(new_list)

poped_item = new_list.pop()

print(f'popped "{poped_item}" from {new_list}')

poped_item =new_list.pop(3)

print(f'popped "{poped_item}" from {new_list}')

print(new_list.sort())  # inplace cannot be assigned to any variable

print(new_list)

print(sorted(my_list,reverse=True))
print(my_list)

print(my_list.reverse())