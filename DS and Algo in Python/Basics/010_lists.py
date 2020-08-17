my_list = [15,6,7,8,35,12,14,4,10,14,15]
my_str_list = ["comp sci", "physics", "elec engr", "philosophy"]
my_new_list = ["art","econ"]

# Things we can do with list object
# 1.Sort the values
# 2.Find values in list or its details
# 3.Insert or remove values
# 4.grab sub my_list
# 5.Iterarte though list and perform check/fuctions

print(f'my_list : {my_list}')

print("sorting....")
sorted_list = sorted(my_list) #not in place sorting
print(f'sorted_list = sorted(my_list) : {sorted_list}')
print(f'sorted(my_list) : {my_list}')
my_list.sort() #in place sorting
print(f'my_list.sort() : {my_list}')
print('-'*30)

print("finding....")
print('physics' in my_str_list)
print(my_str_list.index("physics"))
print(35 in my_list)
print(len(my_list)-1)
print(len(my_str_list)-1)
print(f'min value {min(my_list)}')
print(f'count occurance of 14 in list : {my_list.count(14)}')
print("add/remove...")
# append(), insert(), extend()
my_list.append(25)
print(my_list)
my_list.insert(4,25)
print(my_list)
my_str_list.append(my_new_list)
print(my_str_list)
my_str_list.extend(my_new_list)
print(my_str_list)

print("remove.....")
# pop(), remove()
print(my_str_list)
my_str_list.remove("comp sci")
print(my_str_list)
print(my_str_list.pop()) # returns a value which was popped
print(my_str_list)

print("Sublist....")
print(my_list[-1])
my_list[-1] = 1000
print(my_list)
print(my_list[0:5])
print(my_list[0::3])
print(my_list[::-1])
my_list.reverse()
print(my_list)

for item in my_list:
    print(item)
