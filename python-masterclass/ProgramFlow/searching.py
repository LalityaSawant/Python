shopping_list = ["milk","pasta","eggs","spam","bread","rice"]

item_to_find = "spam"
found_at = None  # initialising is imp as if item not found and not initialised will go into error

# for index in range(len(shopping_list)):
#     if shopping_list[index] == item_to_find:
#         found_at = index
#         break

# this is the way of writing this logic
if item_to_find in shopping_list:
    found_at = shopping_list.index(item_to_find)

if found_at is not None:
    print('{0} found at position {1}'.format(item_to_find,found_at))
else:
    print('{0} not found'.format(item_to_find))
