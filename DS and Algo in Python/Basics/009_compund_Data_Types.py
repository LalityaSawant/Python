# string interger floats are scalar data types (1 object)

# compund datatypes are as below having collections of elements
# list
# dictionary
# sets
# tuples

# tools to work with these are
# Iterators
# for loops
# while loops etc

node_1 = "custom_object"
# list is ordered collection of element,
# **** indexed
list = [1,2,False,4,"lsawant",None,node_1,5.0,2]
print(type(list))
print(list)
print(list[4])
print('-'*20)

# dictionaires are key : value pair
# keys can be number or string it should be immutable data_types
#list is not agood option for key as its mutable
# eg: dict= {'name':'lsawant','course':'python'}
# **** not indexed
# **** no duplicate keys , it overrides
# from python 3.4 or 3.6 dictories maintain order
dict = {1:"hello", 2: "lsawant", 3: None, 4: node_1, 5: 5.0, 2: 'None'}
print(type(dict))
print(dict)
print(dict[2]) # have to pass key not indexed
print('-'*20)

# **** NO Duplicate values and are simialr to lists
# **** unordered
# **** no indexing
set = {1,2,False,4,'lsawant',None, node_1,5.0,1,'lsawant'}
print(type(set))
print(set)
print('-'*20)

# Tuples are similar to lists
# **** they are immuatble
# **** Indexed
tup = (1,2,False,4,'lsawant',None,node_1,5.0,1,'lsawant')
print(type(tup))
print(tup)
print(tup[5])
#tup[5] = 'Python'
