shopping_list = ["milk","pasta","eggs","spam","bread","rice"]

# for item in shopping_list:
#     if item != 'spam':
#         print("Buy "+ item)

print('_'*20)

for item in shopping_list:
    if item == "spam":
        continue

    print("Buy "+ item)

print('_' * 20)

for item in shopping_list:
    if item == "spam":
        break

    print("Buy "+ item)
