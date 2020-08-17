fruit = {"apple": "keeps healthy",
         "grape": "small green sweet",
         "watermelon": "red,green,watery"
}

print(fruit)

# while True:
#     dict_key = input("Please enter a fruit: ")
#     if dict_key == "quit":
#         break
#
#     if dict_key in fruit:
#         description = fruit.get(dict_key)
#         print(description)
#     else:
#         print("We dont have {}".format(dict_key))

fruit["orange"] = "Orange in color"

print(fruit)

order_keys = list(fruit.keys())
order_keys.sort()
for f in order_keys:
    print(f + " - " + fruit[f])

print(fruit.keys())
print(fruit.values())
print('-' * 40)

print(fruit.items())

fruit_tuple = tuple(fruit.items())
for snack in fruit_tuple:
    key,value = snack
    print('{} is {}'.format(key, value))

print(dict(fruit_tuple))



