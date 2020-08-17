my_dictionary = {'name':'LS','age':'35'}

print(my_dictionary)

my_dictionary = {'name':'LS',
                 'age':'35',
                 'address':{'street':'starflower',
                            'state':'CA'}}

print(my_dictionary)
print(my_dictionary['name'])
print(my_dictionary['address'])
print(my_dictionary['address']['state'])

for i in my_dictionary:
    print(i)