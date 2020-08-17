#strings are immutable
# cannot be changed

message = "The price of the stock is:"
print(id(message))
price = "$1100"
new_message = message + " " + price
print(new_message)
message = message + " " + price
print(id(message))

#Indexing but we cannot reassign any value as strings are immutable
name = 'Interstellar'
print(name[0])
print(name[6])
print(name[-1])

#Slicing
print(name[0:5])
print(name[:5])
print(name[5:])
print(name[0:8:2])
print(name[::-1])
