records = [ ('mashurur@exaple.com','Hello World'),
            ('johndoe@example.com','Hello to you too'),
            ('janedoe@exampl.com','Python is awesome')
            ]

for index,record in enumerate(records):
    key,value = record
    if key == 'johndoe@example.com':
        break
    #print(index,key,value)

print(records[index])
