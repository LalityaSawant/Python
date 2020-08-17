import shelve

with shelve.open('shelftest') as fruit:
    fruit['orange'] = 'a sweet orange fruit'
    fruit['apple'] = 'keeps doctor away'


with shelve.open('shelftest') as fruit:
    orange = fruit['orange']
    print(orange)
    for key in fruit:
        print(fruit[key])

    while True:
        shelf_key = input("Enter fruit you like :")
        if shelf_key == 'quit':
            break

        description = fruit.get(shelf_key,"We don't have a "+ shelf_key)
        print(description)
