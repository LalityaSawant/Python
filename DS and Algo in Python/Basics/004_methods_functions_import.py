import string
from string import ascii_lowercase
greeting = 'hello'
user = 'lsawant'
message = "welcome to the Algorithms course"
#few functions in python there are many more
print(greeting,user,message)
print(len(greeting))
print(len(user))
print(len(message))
print(type(message))
print(type(8))
print(id(message))
print(id(user))

#methos in python
#methods are tied to the objects itself

print(greeting,user.capitalize(),message)
print(greeting,user.capitalize(),message)
print(greeting.upper(),user.capitalize(),message)
#print(dir(user)) gives all methods related to this object
print(greeting.upper(),user.capitalize(),message)
print(greeting.upper(),user.capitalize(),message.lower())
message = "     welcome to the Algorithms course  "
print(message)
print(message.strip().lower()) # method chaining
print(message.find('course'))
print(message.find('z'))
message = message.strip()
#split distributes string to list
print(message.split())
print(message.split('m'))
#join joins the list or any other iterable collection
my_list = ['Python','Java','Oracle']
print("-".join(my_list))
print(string.ascii_lowercase) # after improting string module
print(ascii_lowercase)
